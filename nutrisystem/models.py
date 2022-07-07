from django.db import models

# Create your models here.
class Customer(models.Model):
	ALLERGENS = (
					('Milk', 'Milk'),
					('Egg', 'Egg'),
					('Fish', 'Fish'),
					('Shellfish', 'Shellfish'),
					('Tree nuts', 'Tree nuts'),
					('Peanuts', 'Peanuts'),
					('Wheat', 'Wheat'),
					('Soybeans', 'Soybeans'),
					('None', 'None'),
					)
	GENDERS = (
					('Male', 'Male'),
					('Female', 'Female'),
					)
	fullname = models.CharField(max_length=254)
	gender = models.CharField(max_length=24,choices=GENDERS)
	age = models.PositiveIntegerField()
	email = models.EmailField()
	address= models.CharField(max_length=256)
	contact= models.PositiveIntegerField()
	foodallergens= models.CharField(max_length=24, choices=ALLERGENS)
	def __str__(self):
         return self.fullname

class Product(models.Model):
	CATEGORY = (
					('Nutrigeek Juice', 'Nutrigeek Juice'),
					('Nutrigeek Coffee', 'Nutrigeek Coffee'),
					('Nutrigeek Vitamins', 'Nutrigeek Vitamins'),
					)
	Product_Category=models.CharField(max_length=24,choices=CATEGORY)
	Product_Name = models.CharField(max_length=24,blank = True)
	Product_Description = models.TextField(blank = True)
	Product_Price = models.PositiveIntegerField()
	Product_Quantity= models.PositiveIntegerField()
	def __str__(self):
         return '%s-%s' % (self.Product_Name, self.Product_Category)

class Order(models.Model):
	Customer_Reference = models.ForeignKey(Customer,on_delete = models.CASCADE)
	Product_Reference = models.ForeignKey(Product,on_delete=models.CASCADE)
	Order_Quantity = models.PositiveIntegerField()
	Order_Date = models.DateField()
	def __str__(self):
         return '%s-%s' % (self.Customer_Reference, self.Product_Reference)

class Payment(models.Model):
	CATEGORY = (
					('Nutrigeek Juice', 'Nutrigeek Juice'),
					('Nutrigeek Coffee', 'Nutrigeek Coffee'),
					('Nutrigeek Vitamins', 'Nutrigeek Vitamins'),
					)
	PAYMENTS = (
					('Cash on Delivery', 'Cash on Delivery'),
					('Gcash', 'Gcash'),
					('Paymaya', 'Paymaya'),
					('Paypal', 'Paypal'),
					('Credit Card', 'Credit Card'),
					)
	Customer_Payment= models.ForeignKey(Customer,on_delete = models.CASCADE)
	Order_Payment= models.ForeignKey(Order,on_delete = models.CASCADE)
	Payment_Category=models.CharField(max_length=24,choices=CATEGORY)
	Payment_Date = models.DateField()
	Payment_Type = models.CharField(max_length=24,blank = True,choices=PAYMENTS)
	Payment_Amount = models.PositiveIntegerField()
	def __str__(self):
         return '%s-%s' % (self.Customer_Payment, self.Payment_Type)

class Delivery(models.Model):
	COURIERS = (
				('J&T', 'J&T'),
				('Flash', 'Flash'),
				('Toktok', 'Toktok'),
				('JRS Express', 'JRS Express'),
				('Ninja Van', 'Ninja Van'),
				)
	Order_Delivery = models.ForeignKey(Order,on_delete = models.CASCADE)
	Customer_Delivery= models.ForeignKey(Customer,on_delete = models.CASCADE)	
	Delivery_Courier=models.CharField(max_length=24,choices=COURIERS)
	Arrival_Date = models.DateField()
	def __str__(self):
         return '%s-%s' % (self.Order_Delivery, self.Arrival_Date)
