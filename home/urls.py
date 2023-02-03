from django.urls import path

from . import views

app_name = 'home'
urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login_page, name='login'),
    path('signup', views.signup_page, name='signup'),
    path('shopcart', views.shopcart_page, name='shopcart'),
    path('login/admin', views.admin_login, name='admin-login'),
    path('newitem', views.newitem, name='newitem')
]
