from django.db import models

# Create your models here.

#Employee Table
class Employee(models.Model):
    EmployeeFirst = models.CharField(max_length=30)
    EmployeeLast = models.CharField(max_length=30)
    Password = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.EmployeeLast


#customer table
class Customer(models.Model):
    FirstName = models.CharField(max_length=30)
    LastName = models.CharField(max_length=30)
    City = models.CharField(max_length=50)
    State = models.CharField(max_length=2)
    Zip = models.IntegerField()
    email = models.CharField(max_length=100)
    PhoneNum = models.IntegerField()
    Password = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.LastName

#supplier table
class ItemSupplier(models.Model):
    SupplierName = models.CharField(max_length=100)
    ValueSuppliedToDate = models.FloatField()
    FirstItemDate = models.DateField()
    LastItemDate = models.DateField()

    def __str__(self):
        return self.SupplierName

#product table
class Items(models.Model):
    ItemSupplierID = models.ForeignKey(ItemSupplier, on_delete=models.CASCADE)
    ItemName = models.CharField(max_length=50)
    ItemDiscription = models.TextField()
    ItemMarkup = models.FloatField()
    SalePrice = models.FloatField()
    PriceToOrder = models.FloatField()
    InStock = models.IntegerField()

    def __str__(self):
        return self.ItemName

#images for website
class Image(models.Model):
    title = models.CharField(max_length=200)
    img = models.ImageField(upload_to='images/')
    ItemsID = models.ForeignKey(Items, on_delete=models.CASCADE, null=True)

    class Meta:
        db_table = 'Image Upload'

#transactions
class Transaction(models.Model):
    EmployeeID = models.ForeignKey(Employee, on_delete=models.CASCADE)
    ItemID = models.ForeignKey(Items, on_delete=models.CASCADE)
    CustomerID = models.ForeignKey(Customer, on_delete=models.CASCADE)
    TransDateTime = models.DateTimeField
    TransTotal = models.FloatField()
    BuyOnline = models.BooleanField()
    buyOffline = models.BooleanField()

    def __str__(self):
        return self.CustomerID


    