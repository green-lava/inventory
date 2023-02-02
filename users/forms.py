from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import User, Profile, Bus_profile


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Username',
    }))
    password = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Password',
        'type': 'password'
    }))


class SignupForm_vendor(UserCreationForm):
    
    # is_garage = forms.BooleanField()
    # is_vendor = True
    # username = forms.CharField(max_length=100)
    # password1 = forms.CharField(max_length=100)
    # password2 = forms.CharField(max_length=100)
    
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'is_vendor']
        
class SignupForm_garage(UserCreationForm):
    
    # is_garage = forms.BooleanField()
    # is_garage = True
    
    class Meta:
        model = User
        fields = ['username', 'email',  'password1', 'password2', 'is_garage']        
        
        
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        # fields = '__all__'
        exclude = ['user']
        
class Bus_profileForm(forms.ModelForm):
    class Meta:
        model = Bus_profile
        exclude = ['user']        
        