from django.shortcuts import render
from django.http import HttpResponse
from .forms import ImageFieldForm
from .models import Items,ItemSupplier, Image
import datetime

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
    return render(request, "home/index.html",{'item_list':item_list})

def login_page(request):
    return render(request, "home/login.html")
    
def signup_page(request):
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
        if request.POST.get("itemID") and request.POST.get("itemCatID") and request.POST.get("brandID") and request.POST.get("supplierID") \
            and request.POST.get("itemName") and request.POST.get("totalOnHand") and request.POST.get("itemPrice") and request.POST.get("reorderMin") \
            and request.POST.get("max") and request.POST.get("itemDescription"):

            # Creates item on home_itemsupplier table
            # Hard coded values because there are no inputs for these fields in the form yet
            supplier = ItemSupplier(SupplierName="Test Name Here", ValueSuppliedToDate=0.0, FirstItemDate=datetime.datetime.now(), LastItemDate=datetime.datetime.now()) 
            supplier.save()

            # Creates item on home_items table
            newItem = Items(ItemSupplierID=supplier, ItemDiscription=request.POST.get("itemDescription"), \
                ItemName=request.POST.get("itemName"), ItemMarkup=0, SalePrice = request.POST.get("itemPrice"), PriceToOrder=0, InStock=True)
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
