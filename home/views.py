from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import ImageFieldForm
from .models import Items,ItemSupplier, Image, Customer
import datetime
from django.contrib.auth.forms import UserCreationForm 

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
    

def home_view(request): 
    context = {}
    if request.method == "POST": 
        form = ImageFieldForm(request.POST, request.FILES) 
        if form.is_valid(): 
            name = form.cleaned_data.get("name") 
            img = form.cleaned_data.get("image_field") 
            obj = Image.objects.create( 
                                 title = name,  
                                 img = img 
                                 ) 
            obj.save() 
            print(obj)
            #to be redirected to employee homepage
            return render(request, 'home/success.html') 
    else: 
        form = ImageFieldForm()
        context['form'] = form
        return render( request, "home/image_upload.html", context) 

def success(request): 
    return HttpResponse('home/success.html') 

def index(request):
    item_list = Items.objects.all()
    context = {'item_list' : item_list}
    return render(request, "home/index.html", context)
    
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
    item = Items.objects.get(id=id)
    return render(request, "home/itempage.html", {'item': item})

def checkout_page(request):
    return render(request, "home/checkout.html")
