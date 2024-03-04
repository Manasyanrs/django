from django.urls import path

from .views import AddToOrder, UserOrderList, OrderDataExportView

urlpatterns = [
    path('add_to_order/<int:pk>/', AddToOrder.as_view(), name='add_to_order'),
    path('users/<int:user_id>/orders/', UserOrderList.as_view(), name='user_orders'),
    path('users/<int:user_id>/orders/export/', OrderDataExportView.as_view(), name='export_order_data'),
    path('user_orders/', UserOrderList.as_view(), name='my_orders'),
]
