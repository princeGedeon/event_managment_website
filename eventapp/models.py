
from django.db import models

# Create your models here.
from account.models import User

from phonenumber_field.modelfields import PhoneNumberField


class Event(models.Model):
    title=models.CharField(max_length=150)
    image=models.ImageField(default="default/index.jpeg")
    description=models.TextField()
    end_register_date=models.DateTimeField(verbose_name="Date de fin d'inscription")
    gerants=models.ManyToManyField(User,related_name="gerants")
    proprietaire=models.ForeignKey(User,on_delete=models.CASCADE)
    is_free=models.BooleanField(default=True)

    phone_number = PhoneNumberField(blank=True)
    disable=models.BooleanField(default=False)



class EventParticipation(models.Model):
    event=models.ForeignKey(Event,on_delete=models.CASCADE)

