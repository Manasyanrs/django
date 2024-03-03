from django.core.paginator import Paginator
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

from shop_app.models import Product


class HomePage(ListView):
    __per_page = 20
    template_name = "shop_app/home_page.html"
    queryset = Product.objects.all().order_by('-id')

    def get(self, request, *args, **kwargs):
        page_number = request.GET.get("page")
        paginator = Paginator(self.queryset, self.__per_page)
        return render(request, "shop_app/home_page.html", context={
            "all_products": paginator.get_page(page_number),
            "pages": paginator.page_range,
            "count_page": paginator.num_pages
        })


class AddProduct(CreateView):
    template_name = "shop_app/add_product.html"
    model = Product
    fields = "__all__"


class ProductDetailView(DetailView):
    model = Product
    template_name = "shop_app/product_detail.html"
    context_object_name = "product_detail"

    def get_context_data(self, **kwargs):
        context = super(ProductDetailView, self).get_context_data(**kwargs)
        return context


class UpdateProduct(AddProduct, UpdateView):
    template_name = "shop_app/update_product.html"


class DeleteProduct(DeleteView):
    def get(self, request, *args, **kwargs):
        Product.objects.filter(pk=self.kwargs.get("pk")).delete()
        return HttpResponseRedirect("/")
