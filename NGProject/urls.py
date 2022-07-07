"""NGProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from nutrisystem import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('',views.HomePage, name='home'),
    path('view-order/',views.OrderPage, name="view-order"),
    path('view-payment/',views.PaymentPage, name="view-payment"),
    path('view-delivery/',views.PaymentPage, name="view-delivery"),

    path('customer/',views.CustomerPage, name='customer'),
    path('add-customer/',views.AddCustomer, name='add-customer'),
    path('update-customer/<str:pk>/', views.UpdateCustomer, name="update-customer"),
    path('delete-customer/<str:pk>/', views.DeleteCustomer, name="delete-customer"),

    path('order/', views.AddOrder, name="order"),
    path('update-order/<str:pk>/', views.UpdateOrder, name="update-order"),
    path('delete-order/<str:pk>/', views.DeleteOrder, name="delete-order"),

    path('payment/', views.AddPayment, name="payment"),
    path('update-payment/<str:pk>/', views.UpdatePayment, name="update-payment"),
    path('delete-payment/<str:pk>/', views.DeletePayment, name="delete-payment"),

    path('delivery/', views.AddDelivery, name="delivery"),
    path('update-delivery/<str:pk>/', views.UpdateDelivery, name="update-delivery"),
    path('delete-delivery/<str:pk>/', views.DeleteDelivery, name="delete-delivery"),
    ]
