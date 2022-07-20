from django.db import IntegrityError
from django.shortcuts import render, redirect
from .models import Product
from .forms import ProductCreateForm


def index(request):
    all_products = Product.objects.order_by('id')
    context = {'all': all_products}
    return render(request, 'DVscandiweb/index.html', context)


def add_product(request):
    if request.method == 'GET':
        context = {'add_product_form': ProductCreateForm()}
        return render(request, 'DVscandiweb/add-product.html', context)
    elif request.method == 'POST':
        product_form = ProductCreateForm(request.POST)
        if product_form.is_valid():
            product_form.save()
        else:
            context = {'add_product_form': product_form}
            return render(request, 'DVscandiweb/add-product.html', context)
    return redirect('index')


def mass_delete(request):
    if request.method == 'POST':
        to_delete = request.POST.getlist('products')
        Product.objects.filter(id__in=to_delete).delete()
    return redirect('index')
