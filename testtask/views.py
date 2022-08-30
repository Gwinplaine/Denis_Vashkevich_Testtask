from django.db import IntegrityError
from django.shortcuts import render, redirect
from .models import Product
from .forms import ProductCreateForm
from django.contrib.auth.decorators import login_required

# view of the index page with all products from the database
def index(request):
    all_products = Product.objects.order_by('id')
    context = {'all': all_products}
    return render(request, 'DVscandiweb/index.html', context)

# view for add products including the adding form
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

#view to remove instances selected by choosen checkboxes
def mass_delete(request):
    if request.method == 'POST':
        to_delete = request.POST.getlist('products')
        for product_id in to_delete:
            product = Product.objects.get(id=product_id)
            if request.user in product.like.all():
                product.like.remove(request.user)
            else:
                continue
    return redirect('favourites')



# функция представления страницы избранного
@login_required
def favourites(request):
    favourites = Product.objects.filter(like=request.user)
    context = {'favourites': favourites}

    return render(request, 'DVscandiweb/favourites.html', context)


# функция добавления статьи в избранное
@login_required
def add_to_fav(request):
    if request.method == 'POST':
        to_add = request.POST.getlist('products')
        print(to_add)
        
        for product_id in to_add:
            product = Product.objects.get(id=product_id)
            if request.user not in product.like.all():
                product.like.add(request.user)
            else:
                continue
    return redirect('favourites')