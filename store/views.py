from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template import loader
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required

from users.models import User
from .models import (
    Supplier,
    Buyer,
    Season,
    Drop,
    Product,
    Order,
    Delivery
)
from .forms import (
    SupplierForm,
    BuyerForm,
    SeasonForm,
    DropForm,
    ProductForm,
    OrderForm,
    DeliveryForm
)


@login_required(login_url='login')
def dashboard(request):
    total_product = Product.objects.filter(user_id = request.user.id).count()
    total_supplier = Supplier.objects.count()
    total_buyer = Buyer.objects.count()
    total_oder =     Order.objects.filter(created_by = request.user.id).count()
    orders = Order.objects.all().order_by('-id')
    context = {
        'product': total_product,
        'supplier': total_supplier,
        'buyer': total_buyer,
        'order': total_oder,
        'orders': orders,
        
    }
    return render(request, 'dashboard.html', context)




# Supplier views
@login_required(login_url='login')
def create_supplier(request):
    forms = SupplierForm()
    if request.method == 'POST':
        forms = SupplierForm(request.POST)
        if forms.is_valid():
            name = forms.cleaned_data['name']
            address = forms.cleaned_data['address']
            email = forms.cleaned_data['email']
            username = forms.cleaned_data['username']
            password = forms.cleaned_data['password']
            retype_password = forms.cleaned_data['retype_password']
            if password == retype_password:
                user = User.objects.create_user(username=username, password=password, email=email, is_supplier=True)
                Supplier.objects.create(user=user, name=name, address=address)
                return redirect('supplier-list')
    context = {
        'form': forms
    }
    return render(request, 'store/addSupplier.html', context)


class SupplierListView(ListView):
    model = Supplier
    template_name = 'store/supplier_list.html'
    context_object_name = 'supplier'


# Buyer views
@login_required(login_url='login')
def create_buyer(request):
    forms = BuyerForm()
    if request.method == 'POST':
        forms = BuyerForm(request.POST)
        if forms.is_valid():
            name = forms.cleaned_data['name']
            address = forms.cleaned_data['address']
            email = forms.cleaned_data['email']
            username = forms.cleaned_data['username']
            password = forms.cleaned_data['password']
            retype_password = forms.cleaned_data['retype_password']
            if password == retype_password:
                user = User.objects.create_user(username=username, password=password, email=email, is_buyer=True)
                Buyer.objects.create(user=user, name=name, address=address)
                return redirect('buyer-list')
    context = {
        'form': forms
    }
    return render(request, 'store/addbuyer.html', context)


class BuyerListView(ListView):
    model = Buyer
    template_name = 'store/buyer_list.html'
    context_object_name = 'buyer'


# Season views
@login_required(login_url='login')
def create_season(request):
    forms = SeasonForm()
    if request.method == 'POST':
        forms = SeasonForm(request.POST)
        if forms.is_valid():
            forms.save()
            return redirect('season-list')
    context = {
        'form': forms
    }
    return render(request, 'store/addSeason.html', context)


class SeasonListView(ListView):
    model = Season
    template_name = 'store/season_list.html'
    context_object_name = 'season'


# Drop views
@login_required(login_url='login')
def create_drop(request):
    forms = DropForm()
    if request.method == 'POST':
        forms = DropForm(request.POST)
        if forms.is_valid():
            forms.save()
            return redirect('drop-list')
    context = {
        'form': forms
    }
    return render(request, 'store/addCategory.html', context)


class DropListView(ListView):
    model = Drop
    template_name = 'store/category_list.html'
    context_object_name = 'drop'


# Product views
@login_required(login_url='login')
def create_product(request):
    forms = ProductForm()
    if request.method == 'POST':
        forms = ProductForm(request.POST)
        if forms.is_valid():
            instance = forms.save(commit=False)
            instance.user_id = request.user.id
            instance.save()
            return redirect('product-list')
    context = {
        'form': forms
    }
    return render(request, 'store/addProduct.html', context)

@login_required(login_url='login')
def product_view(request):
    mydata = Product.objects.filter(user_id=request.user.id).values()
    # template_name = 'store/product_list.html'
   
    template = loader.get_template('store/product_list.html')
    context = {
        'product': mydata,
    }
    return HttpResponse(template.render(context, request))


@login_required(login_url='login')
def edit_product(request,id):
    mydata = Product.objects.filter(id=id).values()
    template = loader.get_template('store/editProduct.html')
    # print(mydata[0])
    context = {
        'product': mydata[0]
    }
    return HttpResponse(template.render(context, request))

@login_required
def update_product(request,id):
    mydata = Product.objects.get(id=id)
    # print(mydata.price)
    forms = ProductForm()
    if request.method == 'POST':
        forms = ProductForm(request.POST, instance=mydata   )
        if forms.is_valid():
           forms.save()
        return redirect('product-list')
    context = {
        'form': forms
    }
    return render(request, 'store/editProduct', context)
    
@login_required
def delete_product(request, id):
    mydata = Product.objects.get(id=id)  
    mydata.delete() 
    return redirect('product-list') 


#shop
@login_required(login_url='login')
def shop_view(request):
    mydata = Product.objects.filter(user_id=request.user.id).values()
    # template_name = 'store/product_list.html'
    
    template = loader.get_template('store/shop_list.html')
    context = {
        'product': mydata,
    }
    return HttpResponse(template.render(context, request))    

@login_required(login_url='login')
def publish_prod(request,id):
    
    prod_dt = Product.objects.get(id=id)
    
    if(prod_dt.published == False):
     prod_dt.published = True
    else:
        prod_dt.published = False
        
    prod_dt.save()
     
    return redirect('shop-list')
    
    
    

# Order views
@login_required(login_url='login')
def create_order(request):
    forms = OrderForm()
    
    product_dt = Product.objects.filter(user_id=request.user.id).values()
    # print(product_dt)
    if request.method == 'POST':
        forms = OrderForm(request.POST)
        if forms.is_valid():
           instance = forms.save(commit=False)
           instance.created_by = request.user.id
           product_id = forms.cleaned_data['product_id']
           print(product_id)
           instance.product_id = product_id
           instance.save()
           return redirect('order-list')
    context = {
        'form': forms,
        'product' : product_dt
    }
    return render(request, 'store/addOrder.html', context)
    
@login_required(login_url='login')
def order_view(request):
    mydata = Order.objects.filter(created_by=request.user.id).values()
    
    if mydata:
        prod_dt = Product.objects.filter(id = mydata[0]['product_id']).values()
        prod = prod_dt[0]
    else:
        prod = None
    template = loader.get_template('store/order_list.html')
    context = {
        'order': mydata,
        'prod' : prod
    }
    return HttpResponse(template.render(context, request))

@login_required(login_url='login')
def edit_order(request,id):
    mydata = Order.objects.filter(id=id).values()
    prod = Product.objects.filter(created_by=request.user.id).values()
    print(prod)
    template = loader.get_template('store/editOrder.html')
    # print(mydata[0])
    context = {
        'order': mydata[0],
        'product' : prod
    }
    return HttpResponse(template.render(context, request))

@login_required
def update_order(request,id):
    mydata = Order.objects.get(id=id)
    # print(mydata.price)
    forms = OrderForm()
    if request.method == 'POST':
        forms = OrderForm(request.POST, instance=mydata)
        if forms.is_valid():
            instance = forms.save(commit=False)
            instance.created_by = id
            instance.save()
        return redirect('/store/order-list')
    context = {
        'form': forms
    }
    return render(request, 'profile.html', context)

# Delivery views
@login_required(login_url='login')
def create_delivery(request):
    forms = DeliveryForm()
    if request.method == 'POST':
        forms = DeliveryForm(request.POST)
        if forms.is_valid():
            forms.save()
            return redirect('delivery-list')
    context = {
        'form': forms
    }
    return render(request, 'store/addelivery.html', context)


class DeliveryListView(ListView):
    model = Delivery
    template_name = 'store/delivery_list.html'
    context_object_name = 'delivery'
