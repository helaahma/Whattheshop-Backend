from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator



class Watch(models.Model):
	brand = models.CharField(max_length=100)
	model_name = models.CharField(max_length=100)
	case_size = models.IntegerField(validators=[MinValueValidator(20),
                                       MaxValueValidator(60)])
	thickness = models.IntegerField(validators=[MinValueValidator(5),
                                       MaxValueValidator(30)])
	lug_width = models.IntegerField(validators=[MinValueValidator(10),
                                       MaxValueValidator(30)])
	lug_to_lug = models.IntegerField(validators=[MinValueValidator(30),
                                       MaxValueValidator(70)])
	water_resistance = models.IntegerField(validators=[MinValueValidator(0),
                                       MaxValueValidator(20000)])
	manufacture_year = models.IntegerField(validators=[MinValueValidator(1700)])
	price = models.DecimalField(max_digits=10, decimal_places=3)
	user = models.ForeignKey(User, on_delete=models.CASCADE,  related_name="watches")
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	availability = models.BooleanField(default=True)
	box_papers = models.CharField(max_length=100)
	strap = models.CharField(max_length=100)
	functions = models.CharField(max_length=100)

	MOVEMENT_CHOICES = [
		('automatic', 'automatic'),
		('manual', 'manual'),
		('quartz', 'quartz'),
	]
	movement = models.CharField(
		max_length=10,
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
	description = models.TextField(max_length=2000)
	image = models.ImageField()

	
	def __str__(self):
		return str(self.model_name)

# To be expanded as need after meeting
class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)

	def __str__(self):
		return str(self.user)