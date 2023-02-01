from django.contrib import admin
from .models import Customer
from .models import Items
from .models import ItemSupplier
from .models import Employee
from .models import Transaction
# Register your models here.

admin.site.register(Customer)
admin.site.register(Items)
admin.site.register(ItemSupplier)
admin.site.register(Employee)
admin.site.register(Transaction)

class Customer(admin.ModelAdmin):
    exclude = ('CardNum')