from django.urls import path
from .views import AddProduct, HomePage, ProductDetailView, UpdateProduct, DeleteProduct

urlpatterns = [
    path('', HomePage.as_view(), name='home_page'),
    path('add_product/', AddProduct.as_view(), name='add_product'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('product/<int:pk>/update_product/', UpdateProduct.as_view(), name='update_product'),
    path('product/<int:pk>/delete_product/', DeleteProduct.as_view(), name='delete_product'),
]
