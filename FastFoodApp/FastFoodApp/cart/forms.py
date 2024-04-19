from django import forms

from FastFoodApp.cart.models import DeliveryAddress


class DeliveryAddressForm(forms.ModelForm):
    class Meta:
        model = DeliveryAddress
        exclude = ("user",)
        labels = {
            "city": "City",
            "neighborhood": "Neighborhood",
            "street": "Street",
            "building_street_number": "Building/Street Number",
        }
        widgets = {
            "city": forms.Select(attrs={"class": "form-control"}),
            "neighborhood": forms.TextInput(attrs={"class": "form-control"}),
            "street": forms.TextInput(attrs={"class": "form-control"}),
            "building_street_number": forms.TextInput(attrs={"class": "form-control"}),
        }


