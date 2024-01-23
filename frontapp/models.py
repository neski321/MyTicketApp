from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from datetime import datetime
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
# Create your models here.

#--------------------------------------------------------------------------
# Account Type
#--------------------------------------------------------------------------
ACC_TYPES = [
    ('Customer', 'Customer'),
    ('Promoter', 'Promoter'),
    ('Venue', 'Venue')
]

class AccountType(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    accType = models.CharField (max_length=10, choices=ACC_TYPES, default="Customer", verbose_name="Account Type")

    def _accType(self):
        return self.accType


#when new user is created, this also creates Account Type DB entry
@receiver(post_save, sender=User)
def create_userNew(sender, instance, created, **kwargs):
    if created:
        AccountType.objects.create(user=instance)
        #instance.accounttype.save()

#--------------------------------------------------------------------------
# Balance
#--------------------------------------------------------------------------

class Balance(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    balance = models.DecimalField(decimal_places=2, default = 0, verbose_name="Account Balance", max_digits=10)

    def __str__(self):
        return str(self.balance)

@receiver(post_save, sender=User)
def create_userNew(sender, instance, created, **kwargs):
    if created:
        Balance.objects.create(user=instance)

#--------------------------------------------------------------------------
# Venue
#--------------------------------------------------------------------------
class VenueOwner(models.Model):
    user = models.OneToOneField(AccountType, on_delete=models.CASCADE,  primary_key=True)
    venueName = models.CharField(max_length=150, default="", verbose_name="Venue Name", null=True)
    
    seats1 = models.CharField(max_length=150, default="", verbose_name="Seat Tier Name", null=True, blank=True)
    seats2 = models.CharField(max_length=150, default="", verbose_name="Seat Tier 2 Name", null=True, blank=True)
    seats3 = models.CharField(max_length=150, default="", verbose_name="Seat Tier 3 Name", null=True, blank=True)
    seats4 = models.CharField(max_length=150, default="", verbose_name="Seat Tier 4 Name", null=True, blank=True)

    seats_capacity1 = models.IntegerField( default=0, verbose_name="Total Seats")
    seats_capacity2 = models.IntegerField( default=0, verbose_name="Total Seats")
    seats_capacity3 = models.IntegerField( default=0, verbose_name="Total Seats")
    seats_capacity4 = models.IntegerField( default=0, verbose_name="Total Seats")
    
    price1 = models.DecimalField(decimal_places=2, default = 0, verbose_name="Seat Price ", max_digits=8)
    price2 = models.DecimalField(decimal_places=2, default = 0, verbose_name="Seat Price ", max_digits=8)
    price3 = models.DecimalField(decimal_places=2, default = 0, verbose_name="Seat Price ", max_digits=8)
    price4 = models.DecimalField(decimal_places=2, default = 0, verbose_name="Seat Price ", max_digits=8)

    def __str__(self):
        #return self.user.user.get_full_name()
        return self.venueName
    
#Deletes DB entries for VenueOwner model automatically when account type changes # https://docs.djangoproject.com/en/4.1/ref/signals/
@receiver(post_save, sender=AccountType)
def remove_Venue(sender, instance, created, **kwargs):
    if instance.accType != 'Venue': #instance is acctype 
        ven = VenueOwner.objects.filter(user= instance)
        if ven.exists():
            ven.delete() 

#--------------------------------------------------------------------------
#  Concerts - venue owners create concerts
#--------------------------------------------------------------------------
class Concert(models.Model):
    concertName = models.CharField(max_length=100)
    date = models.DateField(verbose_name="Concert Date", null=True)
    time = models.TimeField(verbose_name="Concert Time",null=True)
    venueName = models.ForeignKey(VenueOwner, verbose_name="Venue", null=True, on_delete=models.CASCADE)
    seats_avail1 = models.IntegerField(default=0, ) #used to decrement the amount of seats left per ticket purchase for the concert
    seats_avail2 = models.IntegerField(default=0, ) 
    seats_avail3 = models.IntegerField(default=0, )
    seats_avail4 = models.IntegerField(default=0, )

    
    def __str__(self):
        return self.concertName

#--------------------------------------------------------------------------
# Promoter / reseller module - need to re do 
#--------------------------------------------------------------------------

class Promoter(models.Model):
    user = models.ForeignKey(AccountType, on_delete=models.CASCADE)
    managed_concerts = models.ForeignKey(Concert, on_delete=models.CASCADE, verbose_name="Concerts/Events Managed", null=True, default="")
    def __str__(self):
        return self.user.user.get_short_name()

#auto delete promoter from DB on account type change
@receiver(post_save, sender=AccountType)
def remove_Venue(sender, instance, created, **kwargs):
    if instance.accType != 'Promoter': #instance is acctype 
        prom = Promoter.objects.filter(user= instance)
        if prom.exists():
            prom.delete() 
#--------------------------------------------------------------------------

#--------------------------------------------------------------------------
# Ticket Order Module
#--------------------------------------------------------------------------
class TicketOrder(models.Model):
    ticket_id = models.AutoField(primary_key=True)
    seat_type = models.CharField(max_length=150, default="", verbose_name="Seat Tier", null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    concertName = models.ForeignKey(Concert, verbose_name="Concert", null=True, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    price = models.DecimalField(decimal_places=2, default = 0, verbose_name="Seat Price ", max_digits=8)
    

