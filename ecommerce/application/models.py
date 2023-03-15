from django.db import models

# Create your models here.
from django.contrib.auth.models import User


class Category(models.Model):
    name=models.TextField(max_length=100)


    def __str__(self) :
        return self.name



class Product(models.Model):
    p_name=models.TextField(max_length=100)
    description=models.CharField(max_length=500)
    price=models.IntegerField()
    
    image = models.ImageField(upload_to='product_images')
    cat=models.ForeignKey(Category,on_delete=models.CASCADE,related_name="cat1")


    def __str__(self):
        return self.p_name
   

class Offer(models.Model):
    code=models.CharField(max_length=150)
    description=models.CharField(max_length=200)
    discount_percent=models.CharField(max_length=100)
    p=models.ForeignKey(Product,on_delete=models.CASCADE,related_name="product")



class  CartItem(models.Model):
    Prod_name=models.ForeignKey(Product,on_delete=models.CASCADE,related_name="product_name")  
    
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    quantity=models.IntegerField()



class Checkout(models.Model):
    
    pname= models.ForeignKey(Product,on_delete=models.CASCADE,related_name="productname")
  

    def __str__(self):
        return self.pname
    
   












class AdminContact(models.Model):
    Title = models.CharField(max_length=255)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.Title

# class Cart(models.Model):
#     # items=models.IntegerField()
#     # total=models.IntegerField()
#     cart_items=models.ForeignKey(CartItem,on_delete=models.CASCADE,related_name="cartitem")
   
