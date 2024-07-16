from django.urls import path
from . import views
urlpatterns = [

  path('', views.home, name=""),

  path('index', views.dashboard, name="index"),

  path('register', views.register, name="register"),

  path('login', views.my_login, name="login"),

   # CRUD

  path('create-customer', views.create_customer, name="create-customer"),

  path('update-customer/<int:pk>', views.update_customer, name='update-customer'),

  path('customer/<int:pk>', views.singular_customer, name="customer"),

  path('delete-customer/<int:pk>', views.delete_customer, name="delete-customer"),

]
