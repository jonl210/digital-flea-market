from django.db import models
from django.contrib.auth.models import User

class Employee(models.Model):
    EmployeeFirst = models.CharField(max_length=30)
    EmployeeLast = models.CharField(max_length=30)
    Password = models.CharField(max_length=200, null=True)

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=None)

class ItemSupplier(models.Model):
    ID = models.IntegerField(primary_key=True)
    SupplierName = models.CharField(max_length=100)
    ValueSuppliedToDate = models.FloatField()
    FirstItemDate = models.DateField()
    LastItemDate = models.DateField()

class Items(models.Model):
    ItemSupplierID = models.ForeignKey(ItemSupplier, on_delete=models.CASCADE)
    ItemName = models.CharField(max_length=50)
    ItemDiscription = models.TextField()
    ItemMarkup = models.FloatField()
    SalePrice = models.FloatField()
    PriceToOrder = models.FloatField()
    InStock = models.IntegerField()

#images for website
class Image(models.Model):
    title = models.CharField(max_length=200)
    img = models.ImageField(upload_to='images/')
    ItemsID = models.ForeignKey(Items, on_delete=models.CASCADE, null=True)

    class Meta:
        db_table = 'Image Upload'

class Transaction(models.Model):
    EmployeeID = models.ForeignKey(Employee, on_delete=models.CASCADE)
    ItemID = models.ForeignKey(Items, on_delete=models.CASCADE)
    CustomerID = models.ForeignKey(Customer, on_delete=models.CASCADE)
    TransDateTime = models.DateTimeField
    TransTotal = models.FloatField()
    BuyOnline = models.BooleanField()
    buyOffline = models.BooleanField()


    