
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
    # readonly_fields = "__all__"

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self._apply_readonly_on_fields()

    # def save(self, commit=True):
    #     if commit:
    #         self.instance.delete()
    #     return self.instance