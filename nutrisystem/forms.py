from django.forms import ModelForm
from .models import *
from django import forms

class DateInput(forms.DateInput):
    input_type = 'date'

class CreateCustomer(ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'

class CreateOrder(ModelForm):
    class Meta:
        widgets = {'Order_Date':DateInput()}
        model = Order
        fields = '__all__'

class CreatePayment(ModelForm):
    class Meta:
        widgets = {'Payment_Date':DateInput()}
        model = Payment
        fields = '__all__'
        
class CreateDelivery(ModelForm):
    class Meta:
        widgets = {'Arrival_Date':DateInput()}
        model = Delivery
        fields = '__all__'
