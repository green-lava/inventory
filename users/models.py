from django.db import models
from django.contrib.auth.models import AbstractUser
from phone_field import PhoneField


class User(AbstractUser):
    is_garage = models.BooleanField(default=False)
    is_vendor = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_supplier = models.BooleanField(default=False)
    is_buyer = models.BooleanField(default=False)
    is_profile = models.BooleanField(default=False)
    
class Profile(models.Model):
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, null=True, blank=True)
    email = models.CharField(max_length=50, null=True, blank=True)
    state = models.CharField(max_length=50, null=True, blank=True)
    city = models.CharField(max_length=50, null=True, blank=True)
    landmark = models.CharField(max_length=50, null=True, blank=True)
    zip = models.CharField(max_length=50, null=True, blank=True)
    address = models.CharField(max_length=200, null=True, blank=True)
    contact = models.CharField(max_length=12,null=True, blank=True)
    alt_cont = models.CharField(max_length=12, null=True, blank=True)
    cont_per_name = models.CharField(max_length=50, null=True, blank=True)
    cont_per_phone = models.CharField(max_length=12,null=True, blank=True)
    
    
    def __str__(self):
        return self.user.username or ''
    
class Bus_profile(models.Model):
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    shop_name = models.CharField(max_length=50, null=True, blank=True)
    business_name= models.CharField(max_length=50, null=True, blank=True)
    business_type = models.CharField(max_length=50, null=True, blank=True)
    reg_number = models.CharField(max_length=50, null=True, blank=True)
    gst_no = models.CharField(max_length=50, null=True, blank=True)
    address = models.CharField(max_length=50, null=True, blank=True)
    state = models.CharField(max_length=50, null=True, blank=True)
    city = models.CharField(max_length=50, null=True, blank=True)
    zip = models.CharField(max_length=50, null=True, blank=True)
    # specialization = models.CharField(max_length=50, null=True, blank=True)
    # shop_image = models.ImageField(upload_to='uploads/', null=True, blank=True)
    # inc_cert = models.FileField(upload_to='uploads/', null=True, blank=True) 
    # gst_cert = models.FileField(upload_to='uploads/', null=True, blank=True)
    # other_doc = models.FileField(upload_to='uploads/', null=True, blank=True)
    # shop_add_proof = models.FileField(upload_to='uploads/', null=True, blank=True)
    # vendor_of = models.CharField(max_length=50,null=True, blank=True)
    # bus_card = models.FileField(upload_to='uploads/', null=True, blank=True)
    
    def __str__(self):
        return self.shop_name or ''