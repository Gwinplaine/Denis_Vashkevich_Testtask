from django.shortcuts import render, redirect
#from django import forms
from .models import Product
#from django.http import HttpResponsePermanentRedirect
#from django.urls import reverse
from django import forms
from django.db import models

class ProductCreateForm(forms.ModelForm):

    class Meta:
        model = Product

        fields = ('sku', 'name', 'price', 'size', 'weight', 'height', 'width', 'length')
        widgets = {
            'sku': forms.TextInput(attrs={'class': 'form-control w-25', 'id':'#sku'}),
            'name': forms.TextInput(attrs={'class': 'form-control w-25', 'id':'#name'}),
            'price': forms.NumberInput(attrs={'min': 0, 'class': 'form-control w-25', 'id':'#price'}),
            #'producttype': forms.Select(attrs={'class': 'form-control w-25', 'id':'producttype', 'value':'producttype'}),
            'size': forms.NumberInput(attrs={'min': 0, 'class': 'form-control w-25', 'id':'size', 'value':'size'}),
            'weight': forms.NumberInput(attrs={'min': 0, 'class': 'form-control w-25', 'id':'#weight'}),
            'height': forms.NumberInput(attrs={'min': 0, 'class': 'form-control w-25', 'id':'#height'}),
            'width': forms.NumberInput(attrs={'min': 0, 'class': 'form-control w-25', 'id':'#width'}),
            'length': forms.NumberInput(attrs={'min': 0, 'class': 'form-control w-25', 'id':'#length'}),
        } # можно определить виджеты (типы полей) и аттрибуты (анпример стили или классы)
        labels = {
        'sku': 'sku',
        'name': 'name',
        'price': 'price',
        'size': 'size',
        }
    def clean_fields(self):
        # проверять что нужные поля заполнены в зависимости от типа продукта
        # data = self.cleaned_data
        # msg = "This field is required"
        # for field_name, value in data.items():
        #     if ! value:
        #         self.add_error(field_name, msg)
        return self


'''class SearchForm(forms.Form):
    sku = forms.CharField()
    name = forms.CharField()
    price = forms.IntegerField(min_value=0) 
    size = forms.IntegerField(min_value=0)   #list1
    weight = forms.IntegerField(min_value=0)   #list2
    height = forms.IntegerField(min_value=0)   
    width = forms.IntegerField(min_value=0) 
    length = forms.IntegerField(min_value=0)

'''

def index(request):
    all = Product.objects.order_by('id')
    context = {'all':all}
    return render(request, 'DVscandiweb/index.html', context)

def add_product(request):
    if request.method == 'GET':
        # тут рендерим форму, если она рендерится на индексе - надо поменять тот метод 
        # или выделить отдельную страницу с формой от индекса
        context = {'add_product_form': ProductCreateForm()}
        return render(request, 'DVscandiweb/add-product.html', context)
    elif request.method == 'POST':
        #form = SearchForm(request.POST)
        product_form = ProductCreateForm(request.POST)
        print(product_form)
        if product_form.is_valid():
            product_form.save()
            # если надо ещё что-то с обьектом сделать, кроме заполнения полей инфой с фронта:
            # product = product_form.save(commit=false)
            # product.счастье_тракториста = 300
            # product.save()
        else:
            context = {'add_product_form': product_form}
            return render(request, 'DVscandiweb/add-product.html', context)
    return redirect('index')

def mass_delete(request):
    if request.method=='POST':
        to_delete = request.POST.getlist('products')
        Product.objects.filter(id__in=to_delete).delete()
    return redirect('index')






'''
def delete(request, *args, **kwargs):
    if request.method=='POST':
        product_ids=request.POST.getlist('id[]')
        print (product_ids)
        for id in product_ids:
            product = Product.objects.get(pk=id)
            product.delete()
    return HttpResponseRedirect(reverse('index'))'''
    

'''
def mass_delete(request):
    delete_item = request.POST.get('delete_item', None)

    if request.POST.get('delete'):
        product = Product.objects.filter(id__in=request.POST.getlist('items')).delete()
    elif request.POST.get('save'):
        form = Form(request.POST)
    
    if request.method == 'POST':
        form = forms.OrderForm(request.POST, instance = order)
        if form.is_valid() and save_item is not None:
            form.save(True)
            request.user.message_set.create(message = "The order has been updated successfully.")
            return HttpResponse("<script language=\"javascript\" type=\"text/javascript\">window.opener.location = window.opener.location; window.close();</script>")

        if status is not None and contact is not None and save_status is not None and delete_item is not None:
            try:
                for id in status_items:
                    item = models.StorageItem.objects.get(pk = id)
                    delete = item
                    delete.delete()
                    current_status = models.ItemStatusHistory(item = item, contact = contact, status = status,
                                                    user = request.user)
                    current_status.save()
            except:
                pass
            request.user.message_set.create(message = "Status successfully changed for {0} items".format(len(status_items)))

if request.POST.get('delete'):
   Items.objects.filter(id__in=request.POST.getlist('items')).delete()
elif request.POST.get('save'):
   form = Form(request.POST)

"""def index(request):
    top = Entry.objects.order_by('-date_added')[:5]
    for entry in top:
        if entry.text is not None:
            topic = entry.topic
            id = topic.id
            context = {'top': top, 'read_more': read_more, 'topic': topic, 'id': id}
        if len(entry.text) > 50:
            entry.text = f"{entry.text[:50]}"
        if len(entry.title) > 50:
            entry.title = f"{entry.title[:50]}..."
    for blogentry in blogtop:
        if len(blogentry.blogtext) > 110:
            blogentry.blogtext = blogentry.blogtext[:110]

    return render(request, 'learning_logs/index.html', context)"""
    
    
    from django.views.generic import View

    class Product_view(View):
        def get(self, request):
            allproduct=Prosuct.objects.all()
            context={'products":allproduct}
        return render(request, "product/index.html", context)
    
    button class = btn_delete

    в html
    <script src="https://code.jquery.com/jquery-2.2.4.min.js"></script>

    <script>
      $(document).ready(function(){
        $('delete_btn').click(function()){
            if(confirm("sure?"))
            var id = [];
            var csrf=$('input[name=csrfmiddlewaretoken').val();
            $(':checkbox:checked').each(function(i){
                id[i]=$(this).val()
            })
            if(id.length===0){
                alert("please select item")
            }else{
                console.log(id)
                $.ajax({
                    url:"mass_delete/",
                    method:"POST",
                    data:{
                        id,
                        csrfToken:csrf
                    },
                    success:function(response){
                        for(var i=0; i < id.length; i++){
                            $('tr#'+id[i]+'').css('background-color', '#ccc');
                            $('tr#'+id[i]+'').fadeOut('slow');
                        }
                    }
                })
            }
            }
            })
            })
        </script>


 <script src="https://code.jquery.com/jquery-2.2.4.min.js"></script>
  <script>
    $(document).ready(function(){
      $('#delete-product-btn').click(function(){
          {
          var id = [];
          var csrf=$('input[name=csrfmiddlewaretoken').val();
          $(':checkbox:checked').each(function(i){
              id[i]=$(this).val()
          })

          $.post({
                  url:"delete/",
                  method:"POST",
                  data:{
                      id,
                      csrfmiddlewaretoken:csrf
                  },
            })
        }
    })
})

  </script>


$.ajax({
                  url:"delete/",
                  method:"POST",
                  data:{
                      id,
                      csrfmiddlewaretoken:csrf
                  },
            })



  <div>
    {{ form.sku.label_tag }}{{ form.sku }}
  </div>
  <div>
    {{ form.name.label_tag }}{{ form.name }}
  </div>
  <div>
    {{ form.price.label_tag }}{{ form.price }}
  </div>
  <div>
      {{ form.type.label_tag }}{{ form.type }}
  </div>
  <div>
    {{ form.size.label_tag }}{{ form.size }}
  </div>
  <div>
      {{ form.weight.label_tag }}{{ form.weight }}
  </div>
  <div>
    {{ form.height.label_tag }}{{ form.height }}
  </div> 
  <div>
    {{ form.width.label_tag }}{{ form.width }}
  </div> 
  <div>
    {{ form.length.label_tag }}{{ form.length }}
  </div> 



<script>

  function Hide() {
      if(document.getElementById('id_type').options[document.getElementById('id_type').selectedIndex].value == "4") {
           document.getElementById('id_size').style.display = 'none';
           document.getElementById('id_weight').style.display = 'none';
           document.getElementById('id_height').style.display = 'none';
           document.getElementById('id_width').style.display = 'none';
           document.getElementById('id_length').style.display = 'none';
      }else if(document.getElementById('id_type').options[document.getElementById('id_type').selectedIndex].value == "1") {
           document.getElementById('id_size').style.display = '';
           document.getElementById('id_weight').style.display = 'none';
           document.getElementById('id_height').style.display = 'none';
           document.getElementById('id_width').style.display = 'none';
           document.getElementById('id_length').style.display = 'none';
    }else if(document.getElementById('id_type').options[document.getElementById('id_type').selectedIndex].value == "2") {
           document.getElementById('id_size').style.display = 'none';
           document.getElementById('id_weight').style.display = '';
           document.getElementById('id_height').style.display = 'none';
           document.getElementById('id_width').style.display = 'none';
           document.getElementById('id_length').style.display = 'none';
      } else {
           document.getElementById('id_size').style.display = 'none';
           document.getElementById('id_weight').style.display = 'none';
           document.getElementById('id_height').style.display = '';
           document.getElementById('id_width').style.display = '';
           document.getElementById('id_length').style.display = '';
      }
  }
  window.onload = function() {
      document.getElementById('id_type').onchange = Hide;
  };



  </script>
 
 <form method="post" action="" class="form" >
  {% csrf_token %}
  {% bootstrap_form form %}
</form>

    '''
'''работающий темплейт

<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Gwin</title>
    <link
      href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0-beta1/dist/css/bootstrap.min.css"
      rel="stylesheet"
      integrity="sha384-0evHe/X+R7YkIZDRvuzKMRqM+OrBnVFBL6DOitfPri4tjfHxaWutUpFmBp4vmVor"
      crossorigin="anonymous"
    />
  </head>
  <body>
    
    <div class="container">
       <div class="d-flex my-3">
        <legend>Product add</legend>
        <button type="submit" form="add-product" class="btn btn-outline-success" id="submit">
          Save
        </button> 
        <button type="button" onclick="location.href='{% url 'index' %}'" class="btn btn-outline-warning" id="cancel">
          Cancel
        </button>
      </div>

      <form action="{% url 'add-product' %}" method="post" id="add-product" class="form">
        {%csrf_token%}
        <div class="row mb-3">
          <label for="sku" class="col-sm-2 col-form-label">SKU</label>
          <div class="col-sm-10">
            <input type="text" class="form-control" id="sku" name='sku' required="required"/>
          </div>
        </div>
        <div class="row mb-3">
          <label for="name" class="col-sm-2 col-form-label">Name</label>
          <div class="col-sm-10">
            <input type="text" class="form-control" id="name"  name ='name' required="required"/>
          </div>
        </div>
        <div class="row mb-3">
          <label for="price" class="col-sm-2 col-form-label">Price</label>
          <div class="col-sm-10">
            <input type="number" class="form-control" id="price" name ='price' required="required"/>
          </div>
        </div>
        <div class="row mb-3">
          <label class="col-sm-2 col-form-labe" for="productType">Type Switcher</label>
          <div class="col-sm-10">
            <select class="form-select" id="productType" >
              <option selected>Type Switcher</option>
              <option value="DVD" id="DVD">DVD</option>
              <option value="Book" id="Book">Book</option>
              <option value="Furniture" id="Furniture">Furniture</option>
            </select>
          </div>
        </div>
        <div id="DVD-ele" style="display: none">
          <div class="row mb-3">
            <label for="size" class="col-sm-2 col-form-label">Size (MB)</label>
            <div class="col-sm-10">
              <input type="number" class="form-control" id="size" name ='size' />
            </div>
          </div>
        </div>
        <div id="Furniture-ele" style="display: none">
          <div class="row mb-3">
            <label for="height" class="col-sm-2 col-form-label">height (CM)</label>
            <div class="col-sm-10">
              <input type="number" class="form-control" id="height" name ='height'/>
            </div>
          </div>
          <div class="row mb-3">
            <label for="width" class="col-sm-2 col-form-label">width (CM)</label>
            <div class="col-sm-10">
              <input type="number" class="form-control" id="width" name ='width'/>
            </div>
          </div>
          <div class="row mb-3">
            <label for="length" class="col-sm-2 col-form-label">length (CM)</label>
            <div class="col-sm-10">
              <input type="number" class="form-control" id="length" name ='length'/>
            </div>
          </div>
        </div>
        <div id="Book-ele" style="display: none">
          <div class="row mb-3">
            <label for="weight" class="col-sm-2 col-form-label">Weight (KG)</label>
            <div class="col-sm-10">
              <input type="number" class="form-control" id="weight" name ='weight'/>
            </div>
          </div>
        </div>
      </form>
      <hr/>
    </div>

<script>
let dvdEle = document.querySelector('#DVD-ele');
let furnitureEle = document.querySelector('#Furniture-ele');
let bookEle = document.querySelector('#Book-ele');

productType.addEventListener('change', function(e) {
    if (e.target.value === 'DVD') {
        dvdEle.style.display = 'block';
        bookEle.style.display = 'none';
        furnitureEle.style.display = 'none';

    } else if (e.target.value === 'Book') {
        bookEle.style.display = 'block';
        dvdEle.style.display = 'none';
        furnitureEle.style.display = 'none';

    } else if (e.target.value === 'Furniture') {
        furnitureEle.style.display = 'block';
        dvdEle.style.display = 'none';
        bookEle.style.display = 'none';
    }
  }
)
</script>
  </body>
</html>
'''

'''работающий add product
def add_product(request):
    if request.method != 'POST':
        pass #form = SearchForm()
    else:
        #form = SearchForm(request.POST)
        add_sku = request.POST.get('sku')
        add_name = request.POST.get('name')
        add_price = request.POST.get('price')
        if request.POST.get('size') != '':
            add_size = request.POST.get('size')
        else:
            add_size = None
        if request.POST.get('weight') != '':
            add_weight = request.POST.get('weight')
        else:
            add_weight = None
        if request.POST.get('height') != '':
            add_height = request.POST.get('height')
        else:
            add_height = None
        if request.POST.get('width') != '':
            add_width = request.POST.get('width')
        else:
            add_width = None
        if request.POST.get('length') != '':
            add_length = request.POST.get('length')
        else:
            add_length = None
        ex=Product.objects.create(sku = add_sku, name = add_name, price=add_price, size=add_size, 
        weight = add_weight, height = add_height, width = add_width, length = add_length)
        #ex.size = request.POST.get('size')
        #ex.weight = request.POST.get('weight')
        #ex.height = request.POST.get('weight')
        #ex.width = request.POST.get('width')
        #ex.length = request.POST.get('length')
        #ex.save
        #return HttpResponseRedirect(reverse('index'))
    print(request.POST.get('price'))
    #context = {'form': form}
    return render(request, 'DVscandiweb/add-product.html')#, context)

def mass_delete(request):
    if request.method=='POST':
        to_delete = request.POST.getlist('products')
        Product.objects.filter(id__in=to_delete).delete()
    return redirect('index')

'''