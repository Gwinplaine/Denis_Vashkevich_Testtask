from django.shortcuts import render, redirect
#from django import forms
from .models import Product
#from django.http import HttpResponsePermanentRedirect
#from django.urls import reverse


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
        '''ex.size = request.POST.get('size')
        ex.weight = request.POST.get('weight')
        ex.height = request.POST.get('weight')
        ex.width = request.POST.get('width')
        ex.length = request.POST.get('length')
        ex.save'''
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
