from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class Type(models.TextChoices):
    RESPONSABLE = "RESPONSABLE", "RESPONSABLE"
    ETUDIANT = "ETUDIANT", 'ETUDIANT'



class MyUserManager(BaseUserManager):
    def create_user(self, email,password=None,**kwargs):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """

        if not email:
            raise ValueError('Un Utilisateur doit forcément avoir un email')

        user = self.model(
            email=self.normalize_email(email),


        )
        user.is_administrator=False
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None,**kwargs):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """


        user = self.create_user(
            email,
            password=password,


        )
        user.is_administrator=True
        user.type=Type.RESPONSABLE
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):

    email = models.EmailField(unique=True, blank=True)
    #phone=models.CharField(max_length=15,blank=True,null=True)
    type=models.CharField(choices=Type.choices,max_length=255,default=Type.ETUDIANT)

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_administrator = models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELD = 'email'


    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin

    @property
    def get_pseudo(self):
        return self.email.split('@')[0]



    @property
    def date_joined_(self):
        return self.date_joined