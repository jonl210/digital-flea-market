from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import ImageFieldForm
from .models import Items,ItemSupplier,Customer
import datetime
from django.contrib.auth.forms import UserCreationForm
from django.db.models import Q

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            Customer.objects.create(user=new_user)
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'home/signup.html', {'form': form})

def login_page(request):
    return render(request, "login.html")

def success(request): 
    return HttpResponse('home/success.html') 

def addToCart(request, id):
    if request.method=="POST":
        item = Items.objects.get(id=id)
        if request.user.is_authenticated and not request.user.is_superuser:
            #request.user.cart.add(item)
            current_user = Customer.objects.get(user=request.user)
            #print(current_user.id)
            current_user.cart.add(item)
    item_list = Items.objects.all()
    context = {'item_list' : item_list}
    return render(request, "home/main.html", context)

def main(request):
    item_list = Items.objects.all()
    context = {'item_list' : item_list}
    return render(request, "home/main.html", context)

    
def shopcart_page(request):
    return render(request, "home/shopcart.html")

def admin_login(request):
    return render(request, "home/admin-login.html")

def newitem(request):
    return render(request, "home/newitem.html")

def addNewItem(request):
    if request.method=="POST":
        # Verify there are inputs for all expected fields in the form
        if request.POST.get("itemName") and request.POST.get("salePrice") and request.POST.get("itemMarkup") and request.POST.get("priceToOrder") \
        and request.POST.get("itemDescription") and request.POST.get("supplierID") and request.POST.get("inStock"):           

            # Creates item on home_itemsupplier table
            supplier = ItemSupplier(ID=request.POST.get("supplierID"),SupplierName="Test Name Here2", ValueSuppliedToDate=0.0, FirstItemDate=datetime.datetime.now(), LastItemDate=datetime.datetime.now()) 
            supplier.save()
            
            # Creates item on home_items table
            newItem = Items(ItemSupplierID=supplier,ItemDiscription=request.POST.get("itemDescription"), ItemName=request.POST.get("itemName"), \
                    ItemMarkup=request.POST.get("itemMarkup"), SalePrice = request.POST.get("salePrice"), PriceToOrder=request.POST.get("priceToOrder"), \
                    InStock=request.POST.get("inStock")) 

            newItem.save()

            # Render newitem page
            return render(request, "home/newitem.html")
    
    else:
        # Render newitem page
        return render(request, "home/newitem.html")

# single item view
def item(request, id):
    if request.method=="POST":
        item = Items.objects.get(id=id)
        if request.user.is_authenticated and not request.user.is_superuser:
            #request.user.cart.add(item)
            current_user = Customer.objects.get(user=request.user)
            #print(current_user.cart.all())
            current_user.cart.add(item)
        else:
            return redirect('login')
    item = Items.objects.get(id=id)
    return render(request, "home/itempage.html", {'item': item})

def checkout_page(request):
    return render(request, "home/checkout.html")

def about(request):
    return render(request, "home/about.html")


def search(request):
    query = request.GET.get("q")
    object_list = Items.objects.filter(
       Q(ItemName__icontains=query) | Q(ProductType__icontains=query)
    )
    context = {'search_item_list' : object_list}
    return render(request, "home/searchresults.html", context)
    
def category(request):
    distinct_cat = Items.objects.values('ProductType').distinct()
    return render(request, "home/category.html", {'distinct_cat': distinct_cat})

def product_list(request, product_type):
    products = Items.objects.filter(ProductType=product_type)
    distinct_cat = Items.objects.values('ProductType').distinct()
    return render(request, "home/product_list.html", {'products': products, 'distinct_cat': distinct_cat})


