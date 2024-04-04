
from django import forms

from FastFoodApp.form_mixins.form_mixins import ReadonlyFieldsFormMixin
from FastFoodApp.products.models import Product


class ProductBaseForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = "__all__"
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'price': forms.NumberInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'description': forms.Textarea(
                attrs={
                    'class': 'form-control'
                }
            ),
            'image': forms.FileInput(
                attrs={
                    'class': 'form-control'
                }
            ),
        }


class ProductCreateForm(ProductBaseForm):
    pass


class ProductUpdateForm(ProductBaseForm):
    pass


class ProductDeleteForm(ReadonlyFieldsFormMixin, ProductBaseForm):
    pass
