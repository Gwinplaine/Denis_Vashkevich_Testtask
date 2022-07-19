from django.forms import ModelForm
from .models import Product

class ProductCreateForm(ModelForm):
    class Meta:
        model = Product
        fields = ('sku', 'name', 'price', 'size', 'weight', 'height', 'width', 'length')
        #widjets = {} # можно определить виджеты (типы полей) и аттрибуты (анпример стили или классы)
        labels = {
        'sku': 'что бы это не значило',
        'name': 'Name',
        'price': 'Price',
        'size': 'Size',
        }
    def clean_fields(self):
        # проверять что нужные поля заполнены в зависимости от типа продукта
        # data = self.cleaned_data
        # msg = "This field is required"
        # for field_name, value in data.items():
        #     if ! value:
        #         self.add_error(field_name, msg)
        return self