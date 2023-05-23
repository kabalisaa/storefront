from django.db import models

# Create your models here.
class Promotion(models.Model):
    description = models.CharField(max_length=255)
    discount = models.FloatField()
    
    
class Collection(models.Model):
    title = models.CharField(max_length=255)
    #because we have relationship in both collectiona and product we have to put related name into + to ovoid cllcur relationship
    featured_product = models.ForeignKey('Product', on_delete=models.SET_NULL, null=True, related_name='+') #tell django not to create a reverse relationship
    
    
class Product(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    inventory = models.IntegerField()
    last_update = models.DateTimeField(auto_now=True)
    collection = models.ForeignKey(Collection, on_delete=models.PROTECT)
    
    promotions = models.ManyToManyField(Promotion)


class Customer(models.Model):
    MEMBERSHIP_BRONZE = 'B'
    MEMBERSHIP_SILVER = 'S'
    MEMBERSHIP_GOLDER = 'G'
    MEMBERSHIP_CHOICE = [
        (MEMBERSHIP_BRONZE, 'Bronze'), 
        (MEMBERSHIP_SILVER, 'Silver'),
        (MEMBERSHIP_GOLDER, 'Gold')
    ]
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=255)
    birth_date = models.DateField( null=True)
    membership = models.CharField(max_length=255, choices=MEMBERSHIP_CHOICE, default=MEMBERSHIP_BRONZE)
    
class Order(models.Model):
    PENDING_STATUS = 'P'
    COMPLETE_STATUS = 'C'
    FAILED_STATUS = 'F'
    PAYMENT_CHOICE = [
        (PENDING_STATUS, 'Pending'),
        (COMPLETE_STATUS, 'Completed'),
        (FAILED_STATUS, 'Failed')
    ]
    
    payment_status = models.CharField(max_length=255, choices=PAYMENT_CHOICE, default=PENDING_STATUS)
    placed_at = models.DateTimeField(auto_now_add=True)
    customer = models.ForeignKey(Customer , on_delete=models.PROTECT)

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.PROTECT)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    quantity = models.PositiveSmallIntegerField()
    unit_price = models.DecimalField(max_digits=6, decimal_places=2)
    
    
class Address (models.Model):
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    #customer = models.OneToOneField(Customer, on_delete=models.CASCADE, primary_key=True) #this is for one to one  relationship
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE) #for one to many relationship

class Cart(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE) 
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField()