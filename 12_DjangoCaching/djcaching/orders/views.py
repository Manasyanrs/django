from django.contrib.auth.models import User
from django.core.cache import cache
from django.http import HttpResponseRedirect, Http404, JsonResponse, HttpRequest
from django.views import View
from django.views.generic import CreateView, ListView

from orders.models import Order
from shop_app.models import Product


class AddToOrder(CreateView):
    model = Order

    def get(self, request, *args, **kwargs):
        order = Order.objects.create(user=self.request.user)
        order.items.add(Product.objects.get(id=self.kwargs.get("pk")))
        order.save()
        return HttpResponseRedirect("/")


class UserOrderList(ListView):
    model = Order
    template_name = "orders/order_list.html"
    context_object_name = "my_orders"
    __owner = None

    def get_queryset(self):
        try:
            if self.kwargs.get("user_id") and self.request.user.is_authenticated:
                self.__owner = User.objects.get(id=self.kwargs.get("user_id"))
            else:
                self.__owner = User.objects.get(id=self.request.user.id)

            user_orders = Order.objects.filter(user=self.__owner).order_by("-id")
            items = user_orders.values_list('items', flat=True)
            products = Product.objects.filter(id__in=items)
            return products

        except User.DoesNotExist:
            raise Http404("User not authenticated permission denied!")

    def get_context_data(self, **kwargs):
        context = super(UserOrderList, self).get_context_data(**kwargs)
        context["user"] = self.__owner
        return context


class OrderDataExportView(View):
    def get(self, request: HttpRequest, *args, **kwargs) -> JsonResponse:
        try:
            if self.kwargs.get("user_id") and self.request.user.is_authenticated:
                owner = User.objects.get(id=self.kwargs.get("user_id"))
                cache_key = f"order_data_export{owner.id}"
                order_data = cache.get(cache_key)

                if order_data is None:
                    orders = Order.objects.filter(user=owner).order_by("-id")
                    order_data = [
                        {
                            "pk": order.pk,
                            "user": {
                                "first_name": order.user.first_name,
                                "last_name": order.user.last_name,
                                "email": order.user.email,
                            },
                            "items": [
                                {
                                    "name": item.name,
                                    "description": item.description,
                                    "price": item.price,
                                    "author": {
                                        "product_author": item.author.first_name
                                    }
                                }
                                for item in order.items.all()
                            ]
                        }
                        for order in orders
                    ]
                    cache.set(cache_key, order_data, 60 * 2)
                return JsonResponse({"orders": order_data})

        except User.DoesNotExist:
            raise Http404("User not authenticated permission denied!")
