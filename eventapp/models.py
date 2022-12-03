
from django.db import models

# Create your models here.
from account.models import User
from django.utils.text import slugify

from phonenumber_field.modelfields import PhoneNumberField


class Event(models.Model):
    title=models.CharField(max_length=150)
    image=models.ImageField(default="default/index.jpeg")
    description=models.TextField()
    prix=models.CharField(max_length=10,default="0")
    end_register_date=models.DateTimeField(verbose_name="Date de fin d'inscription")
    date_debut=models.DateField(auto_now=True)
    date_fin=models.DateField(auto_now=True)
    gerants=models.ManyToManyField(User,related_name="gerants")
    proprietaire=models.ForeignKey(User,on_delete=models.CASCADE)
    is_free=models.BooleanField(default=True)
    slug=models.SlugField(default="",null=True,blank=True)


    phone_number = PhoneNumberField(blank=True)
    disable=models.BooleanField(default=False)


    def __str__(self):
        return f"Event  <{self.title}>"

    def save(self, *args, **kwargs):

        if not self.slug:
            self.slug = slugify( self.title+'_'+ str(self.pk))
        super().save(*args, **kwargs)

class EventParticipation(models.Model):
    event=models.ForeignKey(Event,on_delete=models.CASCADE)
    participers=models.ManyToManyField(User)

