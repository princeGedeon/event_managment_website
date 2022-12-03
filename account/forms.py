from django.contrib.auth.forms import UserCreationForm

from account.models import User


class UserForm(UserCreationForm):
    class Meta:
        model=User
        fields=['nom','prenom','email','password1','password2',]