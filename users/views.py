from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.core.exceptions import ValidationError
from .models import User,Profile
from users.models import Profile, User, Bus_profile
from users.forms import ProfileForm, Bus_profileForm
from .forms import LoginForm, SignupForm_garage,SignupForm_vendor,ProfileForm
from django.contrib.auth.decorators import login_required


def login_page(request):
    forms = LoginForm()
    if request.method == 'POST':
        forms = LoginForm(request.POST)
        if forms.is_valid():
            username = forms.cleaned_data['username']
            password = forms.cleaned_data['password']
            user = authenticate(username=username, password=password)
            is_prof = User.objects.get(username = username)
            if user and is_prof.is_profile == True:
                login(request, user)
                return redirect('dashboard')
    context = {'form': forms}
    return render(request, 'users/login.html', context)


def logout_page(request):
    logout(request)
    return redirect('login')


def signup_vendor(request):
    
    form = SignupForm_vendor()
    error = None
    if request.method == 'POST':
        form = SignupForm_vendor(request.POST)
        
        if form.is_valid():
                username = form.cleaned_data['username']
            # password1 =form.cleaned_data['password1']
            # password2 =form.cleaned_data['password2']
            
            # user_dt = None
            # user_dt = User.objects.filter(username = username).values()
            # print(user_dt)
            # if user_dt.exists():
            #     error = "user already exists"
                
            # if(password1 == password2):
                instance = form.save(commit=False)
                instance.is_vendor = True
                instance.save()
                return redirect('profile', username=username)
            # else:
            #     error = "passwords do not match"    
    context =  {'form': form, 'error':error}        
    return render(request, 'users/signup_vendor.html', context )


def signup_garage(request):
    
    form = SignupForm_garage()
    
    if request.method == 'POST':
        form = SignupForm_garage(request.POST)
        if form.is_valid:
            instance = form.save(commit=False)
            instance.is_garage = True
            instance.save()
            return redirect('login')
        
        
    
    context =  {'form': form}        
    return render(request, 'users/signup_garage.html', context )



def profile(request, username):
    user_data = User.objects.get(username = username)
    form = ProfileForm() 
    
    
    if request.method == 'POST':
        
        form = ProfileForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            instance = form.save(commit=False)
            instance.user_id = user_data.id
            instance.save()
            name = form.cleaned_data['name']
            User.objects.filter(id=user_data.id).update(first_name=name, email=email)
            
            return redirect('bus_profile', username=username)
    context = {
        
        'user' : user_data,
        
        'forms': form
         
    }
 
    return render(request, 'profile.html', context)

def bus_profile(request,username):
    
    user_data = User.objects.get(username = username)
    form = Bus_profileForm()
    
    if request.method == 'POST':
        
        form = Bus_profileForm(request.POST)
        if form.is_valid:
            instance = form.save(commit=False)
            instance.user_id = user_data.id
            instance.save()
            User.objects.filter(username = username).update(is_profile = True)            
            
            return redirect('login')
    context = {
        
        'user' : user_data,
        
        'forms': form
         
    }
 
    return render(request, 'bus_profile.html', context)

@login_required(login_url='login')
def edit_profile(request, username):
    
    mydt = User.objects.get(username=username)
    
    user_id = mydt.id 
    prof_dt = Profile.objects.get(user_id=user_id)
    bus_dt = Bus_profile.objects.get(user_id = user_id)
    print(prof_dt.name)
    context = {
        'profile':prof_dt,
        'bus_prof' : bus_dt
    }
    
    return render(request, 'edit_profile.html', context)
        
@login_required
def update_profile(request,id):
    mydata = Profile.objects.get(user_id = id)
    # print(mydata.price)
    forms = ProfileForm()
    if request.method == 'POST':
        forms = ProfileForm(request.POST, instance=mydata)
        if forms.is_valid():
            instance = forms.save(commit=False)
            instance.user_id = id
            instance.save()
        return redirect('dashboard')
    context = {
        'form': forms
    }
    return render(request, 'edit_profile.html', context)        

@login_required(login_url='login')
def edit_bus_profile(request, username):
    
    
    mydt = User.objects.get(username=username)
    user_id = mydt.id 
    bus_dt = Bus_profile.objects.get(user_id = user_id)
    user_id = mydt.id 
    prof_dt = Profile.objects.get(user_id=user_id)
    print(prof_dt.name)
    context = {
        'profile':prof_dt,
        'bus_prof': bus_dt
    }
    
    return render(request, 'edit_bus_profile.html', context)

def inventory(request):
    
    return render(request, 'inventory.html')

    

# @login_required(login_url='login')
# def edit_profile(request,id):
#     mydata = Profile.objects.filter(user_id=id).values()
#     template = loader.get_template('profile.html')
#     print(mydata[0]) 
#     context = {
#         'profile': mydata[0]
#     }
#     return HttpResponse(template.render(context, request))

# @login_required
# def update_profile(request,id):
#     mydata = Profile.objects.get(user_id=id)
#     # print(mydata.price)
#     forms = ProfileForm()
#     if request.method == 'POST':
#         forms = ProfileForm(request.POST, instance=mydata   )
#         if forms.is_valid():
#            forms.save()
#         return redirect('dashboard')
#     context = {
#         'form': forms
#     }
#     return render(request, 'store/editProduct.html', context) 
    
    
    