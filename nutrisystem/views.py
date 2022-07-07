from django.shortcuts import render, redirect
from .models import * 
from .forms import *

def HomePage(request):
    return render(request,'home.html')

def CustomerPage(request):
    customer = Customer.objects.all()
    context = {'customer':customer}
    return render(request,'customer.html',context)

def OrderPage(request):
    order = Order.objects.all()
    context = {'order':order}
    return render(request,'order.html',context)

def PaymentPage(request):
    payment = Payment.objects.all()
    context = {'payment':payment}
    return render(request,'payment.html',context)

def DeliveryPage(request):
    delivery = Payment.objects.all()
    context = {'delivery':delivery}
    return render(request,'delivery.html',context)

def AddCustomer(request):
    form = CreateCustomer()
    if request.method == 'POST':
        item = CreateCustomer(request.POST)
        if item.is_valid():
            item.save()
            return redirect('customer')
    value = {'form':form}
    return render(request, 'create.html',value)

def UpdateCustomer(request,pk):
    updateditem = Customer.objects.get(id=pk)
    form = CreateCustomer(instance=updateditem)
    if request.method == "POST":
        item = CreateCustomer(request.POST,instance=updateditem)
        if item.is_valid:
            item.save()
            return redirect('customer')

    value = {'form':form}
    return render(request, 'create.html',value)

def DeleteCustomer(request,pk):
    deleteitem = Customer.objects.get(id=pk)
    if request.method == "POST":
        deleteitem.delete()
        return redirect('customer')
    value = {'item':deleteitem}
    return render(request, 'create.html',value)

def AddOrder(request):
    form = CreateOrder()
    if request.method == 'POST':
        item = CreateOrder(request.POST)
        if item.is_valid():
            item.save()
            return redirect('view-order')
    value = {'form':form}
    return render(request, 'create.html',value)

def UpdateOrder(request,pk):
    updateditem = Order.objects.get(id=pk)
    form = CreateOrder(instance=updateditem)
    if request.method == "POST":
        item = CreateOrder(request.POST,instance=updateditem)
        if item.is_valid:
            item.save()
            return redirect('view-order')

    value = {'form':form}
    return render(request, 'create.html',value)

def DeleteOrder(request,pk):
    deleteitem = Order.objects.get(id=pk)
    if request.method == "POST":
        deleteitem.delete()
        return redirect('view-order')
    value = {'item':deleteitem}
    return render(request, 'create.html',value)

def AddPayment(request):
    form = CreatePayment()
    if request.method == 'POST':
        item = CreatePayment(request.POST)
        if item.is_valid():
            item.save()
            return redirect('view-payment')
    value = {'form':form}
    return render(request, 'create.html',value)

def UpdatePayment(request,pk):
    updateditem = Payment.objects.get(id=pk)
    form = CreateOrder(instance=updateditem)
    if request.method == "POST":
        item = CreatePayment(request.POST,instance=updateditem)
        if item.is_valid:
            item.save()
            return redirect('view-payment')

    value = {'form':form}
    return render(request, 'create.html',value)

def DeletePayment(request,pk):
    deleteitem = Payment.objects.get(id=pk)
    if request.method == "POST":
        deleteitem.delete()
        return redirect('view-payment')
    value = {'item':deleteitem}
    return render(request, 'create.html',value)

def AddDelivery(request):
    form = CreateDelivery()
    if request.method == 'POST':
        item = CreateDelivery(request.POST)
        if item.is_valid():
            item.save()
            return redirect('view-delivery')
    value = {'form':form}
    return render(request, 'create.html',value)

def UpdateDelivery(request,pk):
    updateditem = Delivery.objects.get(id=pk)
    form = CreateDelivery(instance=updateditem)
    if request.method == "POST":
        item = CreateDelivery(request.POST,instance=updateditem)
        if item.is_valid:
            item.save()
            return redirect('view-delivery')

    value = {'form':form}
    return render(request, 'create.html',value)

def DeleteDelivery(request,pk):
    deleteitem = Delivery.objects.get(id=pk)
    if request.method == "POST":
        deleteitem.delete()
        return redirect('view-delivery')
    value = {'item':deleteitem}
    return render(request, 'create.html',value)
