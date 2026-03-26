from django import forms
from .models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            "name",
            "sku",
            "category",
            "location",
            "quantity",
            "unit_price",
            "status",
            "description",
        ]
        widgets = {
            "description": forms.Textarea(attrs={"rows": 4}),
        }


class PasswordResetMockForm(forms.Form):
    email = forms.EmailField(label="Correo institucional")
