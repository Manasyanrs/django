from django import forms

from shopapp.models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = "name", "price", "description", "discount", "preview"

    images = forms.ImageField(
        widget=forms.ClearableFileInput(attrs={"multiple": True}),
    )


class OrderForm(forms.Form):
    json_order = forms.FileField()
