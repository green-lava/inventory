from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.template import loader
from store.models import Product, Supplier, Buyer, Order
from users.models import Profile, User
from users.forms import ProfileForm, Bus_profileForm
from django.http import HttpResponse



def home(request):
    
    return render(request,'index.html')

def aboutus(request):
    return render(request, 'aboutus.html')

# @login_required(login_url='login')
