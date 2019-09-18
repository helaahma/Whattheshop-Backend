from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.datetime_safe import datetime


class Brand(models.Model):
    name = models.CharField(max_length = 100)

    def __str__(self):
        return self.name

class Watch(models.Model):

#   brand = models.ForeignKey(Brand, on_delete=models.CASCADE,  related_name="brand")
    brand = models.CharField(max_length=100)
    model_name = models.CharField(max_length=100)
    case_size = models.IntegerField(validators=[MinValueValidator(20), MaxValueValidator(60)])
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
# AddToCart
class Cart(models.Model):
    watch=models.ManyToManyField(Watch)
    total= models.PositiveIntegerField(default=0)
    status=models.BooleanField(default=False)
    timestamp=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return str(self.watch)

@receiver(post_save, sender=Cart)
def update_cart_handler(sender, instance, **kwargs):
    instance.total += instance.watch.price
    instance.status =True
    instance.timestamp = datetime.now()



# To be expanded as need after meeting
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.user)