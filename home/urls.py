from django.urls import path, re_path
from django.contrib.auth import views as auth_views

from . import views

app_name = 'home'
urlpatterns = [

    path('main/<id>', views.addToCart, name='main'),
    path('', views.main, name='main')                         ,
    path('main', views.main, name='main')                         ,
    path('signup', views.register, name='signup')            ,
    path('shopcart', views.shopcart_page, name='shopcart')      ,
    path('login/admin', views.admin_login, name='admin-login')  ,
    path('newitem', views.newitem, name='newitem')              ,
    path('newitemadd', views.addNewItem, name='newitemadd')     ,
    path('item/<id>', views.item, name='item')                  ,
    path('success', views.success, name='success')              ,
    #path('login', auth_views.LoginView.as_view(template_name='home/login.html'), name='login'),
    #path('logout', auth_views.LogoutView.as_view(template_name='home/main.html'), name='logout'),
    path('checkout', views.checkout_page, name='checkout')      ,
    path('about',views.about, name='about')                     ,
    path('searchresults', views.search, name='searchresults')
]
