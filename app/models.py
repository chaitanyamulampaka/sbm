from django.db import models
from django.contrib.auth.models import User
class pcards(models.Model):
    product_id=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    pcardimg=models.FileField(upload_to="app/",null=True,default=None)
    pcardname=models.CharField(max_length=50)
    pcardcost=models.CharField(max_length=50)
    pcarddiscount=models.CharField(max_length=50)
    pcardoldprice=models.CharField(max_length=50)
    pcardrating=models.IntegerField()
class productViewer(models.Model):
    product_id=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    smallimg1=models.FileField(upload_to="app/",null=True,default=None)
    smallimg2=models.FileField(upload_to="app/",null=True,default=None)
    smallimg3=models.FileField(upload_to="app/",null=True,default=None)
    smallimg4=models.FileField(upload_to="app/",null=True,default=None)
    mainimg=models.FileField(upload_to="app/",null=True,default=None)
    productdescription = models.TextField()


class Profile(models.Model):
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    fname= models.CharField(max_length=50,null=True)
    mobile = models.BigIntegerField(null=True)
    username=models.CharField(max_length=50,null=True)
    def __str__(self):
        return self.user.username

class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.user}'s Cart"

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(pcards, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} of {self.product.pcardname}"

class Address(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    a_mobile=models.CharField(max_length=100)
    pincode = models.BigIntegerField()
    state = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    house_no=models.CharField(max_length=100)
    area=models.CharField(max_length=100)
    landmark=models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name}"

    
