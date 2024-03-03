from django import forms

from shop_app.models import Product


class AddProductForm(forms.ModelForm):
    model = Product

    class Meta:
        fields = "__all__"
        model = Product
