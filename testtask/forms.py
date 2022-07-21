from django import forms
from .models import Product

PRODUCT_TYPES = (
    (None, 'Please select product type'),
    ('DVD', 'DVD'),
    ('Book', 'Book'),
    ('Furniture', 'Furniture')
    )


class ProductCreateForm(forms.ModelForm):

    producttype = forms.CharField(
        widget=forms.Select(
            choices=PRODUCT_TYPES,
            attrs={'class': 'form-select w-25', 'id': 'producttype'}),
        label='Type Switcher'
    )

    class Meta:
        model = Product

        fields = ('sku', 'name', 'price', 'size', 'weight', 'height', 'width', 'length')
        widgets = {
            'sku': forms.TextInput(attrs={'class': 'form-control w-25', 'id':'sku'}),
            'name': forms.TextInput(attrs={'class': 'form-control w-25', 'id':'name'}),
            'price': forms.NumberInput(attrs={'min': 0,'class': 'form-control w-25', 'id':'price'}),
            'size': forms.NumberInput(attrs={'min': 0, 'class': 'form-control w-25', 'id':'size'}),
            'weight': forms.NumberInput(attrs={'min': 0,'class': 'form-control w-25', 'id':'weight'}),
            'height': forms.NumberInput(attrs={'min': 0,'class': 'form-control w-25', 'id':'height'}),
            'width': forms.NumberInput(attrs={'min': 0,'class': 'form-control w-25', 'id':'width'}),
            'length': forms.NumberInput(attrs={'min': 0,'class': 'form-control w-25', 'id':'length'}),
        }
        labels = {
            'sku': 'SKU',
            'name': 'Name',
            'price': 'Price',
            'size': 'Size (MB)',
            'height': 'Height (CM)',
            'width': 'Width (CM)',
            'length': 'Length (CM)',
            'weight': 'Weight (KG)',
        }

