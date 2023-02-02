from django.db import models

from users.models import User


class Supplier(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=120, unique=True)
    address = models.CharField(max_length=220)
    created_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name


class Buyer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=120, unique=True)
    address = models.CharField(max_length=220)
    created_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name


class Season(models.Model):
    name = models.CharField(max_length=120, unique=True)
    description = models.CharField(max_length=220)
    created_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name


class Drop(models.Model):
    name = models.CharField(max_length=120, unique=True)
    created_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=120, blank=True, null= True)
    part_no = models.CharField(max_length=50, null=True, blank=True)
    manufacturer = models.CharField(max_length=100, null=True, blank=True)
    quantity = models.PositiveIntegerField()
    price = models.CharField(max_length=10, null=True, blank=True)
    user =  models.ForeignKey(User, on_delete=models.CASCADE)
    created_date = models.DateField(auto_now_add=True)
    published = models.BooleanField(null=True, default=False)
    supplier = models.CharField(max_length=120, blank=True, null= True)
    warranty = models.CharField(max_length=50, null=True, blank=True) 
    color = models.CharField(max_length=50, null=True, blank=True)
    
    
    

    def __str__(self):
        return self.name
    
class Order(models.Model):
    STATUS_CHOICE = (
        ('pending', 'Pending'),
        ('decline', 'Decline'),
        ('approved', 'Approved'),
        ('processing', 'Processing'),
        ('complete', 'Complete'),
        ('bulk', 'Bulk'),
    )
    # supplier = models.IntegerField(null=True, blank=True)
    product_id = models.IntegerField(max_length=20, blank=True, null=True)
    quantity = models.IntegerField(max_length=50,null=True,blank=True)
    amount = models.IntegerField(max_length=50,null=True,blank=True)
    garage = models.CharField(max_length=50,null=True,blank=True)
    garage_cont = models.IntegerField(max_length=20,null=True,blank=True)
    address = models.CharField(max_length=200, null=True, blank=True)
    state = models.CharField(max_length=100, null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    landmark = models.CharField(max_length=100, null=True, blank=True)
    zip = models.IntegerField(null=True,blank=True)
    created_by = models.IntegerField(max_length=20, blank=True, null=True)
    created_date = models.DateField(auto_now_add=True)


    def __str__(self):
        return self.garage


class Delivery(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    courier_name = models.CharField(max_length=120)
    created_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.courier_name