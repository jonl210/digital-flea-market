from django.shortcuts import render

def index(request):
    return render(request, "home/index.html")

def login_page(request):
    return render(request, "home/login.html")
    
def signup_page(request):
    return render(request, "home/signup.html")
    
def shopcart_page(request):
    return render(request, "home/shopcart.html")
