from django.contrib.auth.forms import UserCreationForm

from account.models import User


class UserForm(UserCreationForm):
    class Meta:
        model=User
        fields=['email','password1','password2','type']