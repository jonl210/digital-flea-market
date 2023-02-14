from django.shortcuts import render
from .models import Items,ItemSupplier, Customer
import datetime

def index(request):
    item_list = Items.objects.all()
    return render(request, "home/index.html",{'item_list':item_list})

def login_page(request):
    return render(request, "home/login.html")
    
def signup_page(request):
    if request.method=="POST":
        # Verify there are inputs for all expected fields in the form
        if request.POST.get("firstName") and request.POST.get("lastName") and request.POST.get("phoneNum") \
            and request.POST.get("streetAddress") and request.POST.get("city") and request.POST.get("state") \
            and request.POST.get("zipCode") and request.POST.get("email") and request.POST.get("password") \
            and request.POST.get("confirmPassword"):

            # Creates new customer on home_customer table
            newCustomer = Customer(FirstName=request.POST.get("firstName"), LastName=request.POST.get("lastName"), City=request.POST.get("city"),
            State=request.POST.get("state"), Zip=request.POST.get("zipCode"), email=request.POST.get("email"), PhoneNum=request.POST.get("phoneNum"))
            newCustomer.save()

    return render(request, "home/signup.html")
    
def shopcart_page(request):
    return render(request, "home/shopcart.html")

def admin_login(request):
    return render(request, "home/admin-login.html")

def newitem(request):
    return render(request, "home/newitem.html")

def addNewItem(request):
    if request.method=="POST":
        # Verify there are inputs for all expected fields in the form
        if request.POST.get("itemID") and request.POST.get("supplierID") and request.POST.get("itemName") and request.POST.get("inStock") \
            and request.POST.get("itemPrice") and request.POST.get("itemMarkup") and request.POST.get("priceToOrder") and request.POST.get("itemDescription"):
            
            # Creates item on home_itemsupplier table
            supplier = ItemSupplier(SupplierName="Test Name Here", ValueSuppliedToDate=0.0, FirstItemDate=datetime.datetime.now(), LastItemDate=datetime.datetime.now()) 
            supplier.save()

            # Creates item on home_items table
            newItem = Items(ItemSupplierID=supplier, ItemDiscription=request.POST.get("itemDescription"), \
                ItemName=request.POST.get("itemName"), ItemMarkup=request.POST.get("itemMarkup"), SalePrice = request.POST.get("itemPrice"), \
                PriceToOrder=request.POST.get("priceToOrder"), InStock=request.POST.get("inStock"))
            newItem.save()

            # Render newitem page
            return render(request, "home/newitem.html")
    
    else:
        # Render newitem page
        return render(request, "home/newitem.html")

# single item view
def item(request, id):
    item = Items.objects.get(id=id)
    return render(request, "home/itempage.html", {'item': item})
