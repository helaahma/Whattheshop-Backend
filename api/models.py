from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator


class Brand(models.Model):
	name = models.CharField(max_length = 100)

	def __str__(self):
		return self.name

class Watch(models.Model):
	brand = models.ForeignKey(Brand, on_delete=models.CASCADE,  related_name="brand")
	model_name = models.CharField(max_length=100)
	case_size = models.IntegerField(validators=[MinValueValidator(20),
									   MaxValueValidator(60)])
	thickness = models.IntegerField(validators=[MinValueValidator(5),
									   MaxValueValidator(30)],blank=True,null=True)
	lug_width = models.IntegerField(validators=[MinValueValidator(10),
									   MaxValueValidator(30)],blank=True,null=True)
	lug_to_lug = models.IntegerField(validators=[MinValueValidator(30),
									   MaxValueValidator(70)],blank=True,null=True)
	water_resistance = models.IntegerField(validators=[MinValueValidator(0),
									   MaxValueValidator(20000)],blank=True,null=True)
	manufacture_year = models.IntegerField(validators=[MinValueValidator(1700)],blank=True,null=True)
	price = models.DecimalField(max_digits=10, decimal_places=3)
	user = models.ForeignKey(User, on_delete=models.CASCADE,  related_name="watches")
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	availability = models.BooleanField(default=True)
	box_papers = models.CharField(max_length=100)
	strap = models.CharField(max_length=100,blank=True,null=True)
	functions = models.CharField(max_length=100,blank=True,null=True)

	MOVEMENT_CHOICES = [
		('automatic', 'automatic'),
		('manual', 'manual'),
		('quartz', 'quartz'),
	]
	movement = models.CharField(
		max_length=12,
		choices=MOVEMENT_CHOICES,
		default=False,
	)
	PAYMENT_CHOICES = [
		('paypal', 'paypal'),
		('credit_card', 'credit card'),
		('cash', 'cash'),
		('knet','knet'),
	]
	payment = models.CharField(
		max_length=10,
		choices=PAYMENT_CHOICES,
		default='cash',
	)
	DELIVERY_CHOICES = [
		('in_person', 'in person'),
		('DHL', 'DHL'),
		('FEDEX', 'FEDEX'),
		('EMS','EMS'),
		('driver_delivery','driver delivery'),
	]
	delivery = models.CharField(
		max_length=20,
		choices=DELIVERY_CHOICES,
		default='in_person',
	)
	description = models.TextField(max_length=2000,blank=True,null=True)
	image = models.ImageField(blank=True,null=True)

	
	def __str__(self):
		return str(self.model_name)

# To be expanded as need after meeting
class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	phone_number = models.PositiveIntegerField(blank=True, null = True)
	def __str__(self):
		return str(self.user)

class Address (models.Model):
	COUNTRIES = (
		('Kuwait', 'Kuwait'),
		('Oman','Oman'),
		('UAE','UAE'),
		('KSA','KSA'),
		('Bahrain','Bahrain'),
		('Qatar','Qatar'),
		('other','other'),
	)
	user = models.OneToOneField(User , on_delete = models.CASCADE)
	country = models.CharField( choices = COUNTRIES , max_length = 20, default='Kuwait')
	city = models.CharField( max_length = 100, blank = True)
	governate = models.CharField( max_length = 100, blank = True)
	zipcode = models.CharField(max_length = 5, blank = True)
	street_line1 = models.CharField( max_length = 100, blank = True)
	street_line2 = models.CharField( max_length = 100, blank = True)