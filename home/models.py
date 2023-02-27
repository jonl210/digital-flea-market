from django.db import models
from django.contrib.auth.models import User



class ItemSupplier(models.Model):
    SupplierName = models.CharField(max_length=100)
    ValueSuppliedToDate = models.FloatField()
    FirstItemDate = models.DateField()
    LastItemDate = models.DateField()

ProdChoices = (
    ('Fresh Produce', 'PRODUCE'),
    ('Canned Goods', 'CANNED'),
    ('Frozen', 'FROZEN'),
    ('Dairy', 'DAIRY'),
    ('Deli', 'DELI'),
    ('Bakery', 'BAKERY'),
    ('Stationary', 'STATIONARY'),
    ('Jewelry', 'JEWELERY'),
    ('Crafts', 'CRAFTS'),
    ('Electronics', 'ELECTRONICS'),
    ("Men's Clothing", 'MENS'),
    ("Women's Clothing", 'WOMENS'),
    ('Toys', 'TOYS'),
    ('Cleaning Supplies', 'CLEANING'),
    ('Housewares', 'HOUSEWARES'),
    ('Hardware', 'HARDWARE'),
    ('Gardening', 'GARDEN'),
    ('Cosmetics', 'COSMETICS'),
    ('Pharmacy', 'PHARMACY'),
    ('Sporting Goods', 'SPORTING'),
    ('Automotive', 'AUTOMOTIVE'),
    ('Impulse', 'IMPULSE')
)

class Items(models.Model):
    ItemSupplierID = models.ForeignKey(ItemSupplier, on_delete=models.CASCADE)
    ItemName = models.CharField(max_length=50)
    ItemDiscription = models.TextField()
    ItemMarkup = models.FloatField()
    SalePrice = models.FloatField()
    PriceToOrder = models.FloatField()
    InStock = models.IntegerField()
    ProductType = models.CharField(max_length=50, choices=ProdChoices, null=True)

# Needs to be below Items declaration for many to many field to work.
class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=None)
    cart = models.ManyToManyField(Items, default=None)

#images for website
class Image(models.Model):
    title = models.CharField(max_length=200)
    img = models.ImageField(upload_to='images/')
    ItemsID = models.ForeignKey(Items, on_delete=models.CASCADE, null=True)

    class Meta:
        db_table = 'Image Upload'

class Transaction(models.Model):
    ItemID = models.ForeignKey(Items, on_delete=models.CASCADE)
    CustomerID = models.ForeignKey(Customer, on_delete=models.CASCADE)
    Quantity = models.IntegerField(default=1)
    Address = models.CharField(max_length=100, default='', blank=True)
    Phone = models.CharField(max_length=50, default='', blank=True)
    TransDateTime = models.DateTimeField
    TransTotal = models.FloatField()
    Status = models.BooleanField(default=True)

    def placeOrder(self):
        self.save

    @staticmethod
    def getCustOrders(CustomerID):
        return Transaction.objects.filter(Customer=CustomerID).order_by('-date')