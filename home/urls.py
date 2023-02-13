from django.urls import path

from . import views

app_name = 'home'
urlpatterns = [
    path('', views.index, name='index')                         ,
    path('login', views.login_page, name='login')               ,
    path('signup', views.signup_page, name='signup')            ,
    path('shopcart', views.shopcart_page, name='shopcart')      ,
    path('login/admin', views.admin_login, name='admin-login')  ,
    path('newitem', views.newitem, name='newitem')              ,
    path('newitemadd', views.addNewItem, name='newitemadd')     ,
    path('item/<id>', views.item, name='item')                  ,
    path('uploadimage', views.home_view, name='image_upload')   ,
    path('success', views.success, name='success')              ,
]
