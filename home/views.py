from django.shortcuts import render

def index(request):
    return render(request, "home/index.html")

def login_page(request):
    return render(request, "home/login.html")