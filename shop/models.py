from django.conf import settings
from django.db import models
from django.utils import timezone


class User(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    email_address = models.CharField(max_length=100)
    phone_number = models.IntegerField()
    birthday_date = models.DateField(auto_now=True)
    wallet = models.ForeignKey("Wallet", on_delete=models.CASCADE)
    address = models.ForeignKey("Address", on_delete=models.CASCADE)
    modified_date = models.DateTimeField(auto_now=True)
    created_date = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.last_name


class Address(models.Model):
    country = models.CharField(max_length=100)
    province = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    address = models.TextField()
    tel_number = models.IntegerField()
    zip_code = models.IntegerField()
    modified_date = models.DateTimeField(auto_now=True)
    created_date = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.city


class Wallet(models.Model):
    amount = models.IntegerField()
    account_number = models.IntegerField()
    bank_name = models.CharField(max_length=100)
    purchase_amount = models.IntegerField()
    modified_date = models.DateTimeField(auto_now=True)
    purchase_date = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.amount        
     
        
class Transaction(models.Model):
    totall_payment = models.IntegerField()
    payment_method = models.CharField(max_length=100)
    tracking_number = models.IntegerField()
    modified_date = models.DateTimeField(auto_now=True)
    transaction_date = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.totall_payment
        
 
class Order(models.Model):
    user = models.ForeignKey("User", on_delete=models.CASCADE)
    transaction = models.ForeignKey("Transaction", on_delete=models.CASCADE)
    product = models.ForeignKey("Product", on_delete=models.CASCADE)
    price = models.ForeignKey("Price", on_delete=models.CASCADE)
    address = models.ForeignKey("Address", on_delete=models.CASCADE)
    amount = models.IntegerField()
    modified_date = models.DateTimeField(auto_now=True)
    created_date = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.amount
        

class Price(models.Model):
    price_quantity = models.IntegerField()
    modified_date = models.DateTimeField(auto_now=True)
    created_date = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.price_quantity
        
        
class Cart(models.Model):
    order = models.ForeignKey("Order", on_delete=models.CASCADE)
    address = models.ForeignKey("Address", on_delete=models.CASCADE)
    product = models.ForeignKey("Product", on_delete=models.CASCADE)
    totall_payment = models.IntegerField()
    quantity = models.IntegerField()
    modified_date = models.DateTimeField(auto_now=True)
    created_date = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.totall_payment
        
        
class Product(models.Model):
    product_category = models.ForeignKey("Product_Category", on_delete=models.CASCADE)
    product_stock = models.ForeignKey("Product_Stock", on_delete=models.CASCADE)
    price = models.ForeignKey("Price", on_delete=models.CASCADE)
    discount = models.ForeignKey("Discount", on_delete=models.CASCADE)
    p_name = models.CharField(max_length=100)
    explanation = models.TextField()
    modified_date = models.DateTimeField(auto_now=True)
    created_date = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.p_name
        
        
class Product_Category(models.Model):
    pc_name = models.CharField(max_length=100)
    pc_explanation = models.CharField(max_length=100)
    modified_date = models.DateTimeField(auto_now=True)
    created_date = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.pc_name
        
        
class Product_Stock(models.Model):
    product_amount = models.IntegerField()
    expiration_date = models.DateField(auto_now=True)
    modified_date = models.DateTimeField(auto_now=True)
    created_date = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.product_amount
        
        
class Discount(models.Model):
    name = models.CharField(max_length=100)
    explanation = models.CharField(max_length=100)
    discount_percent = models.IntegerField()
    modified_date = models.DateTimeField(auto_now=True)
    created_date = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.discount_percent
        
        
class Product_Comment(models.Model):
    product = models.ForeignKey("Product", on_delete=models.CASCADE)
    user = models.ForeignKey("User", on_delete=models.CASCADE)
    comment = models.TextField()
    modified_date = models.DateTimeField(auto_now=True)
    created_date = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.user


class Product_Like(models.Model):
    product = models.ForeignKey("Product", on_delete=models.CASCADE)
    user = models.ForeignKey("User", on_delete=models.CASCADE)
    modified_date = models.DateTimeField(auto_now=True)
    created_date = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.user
