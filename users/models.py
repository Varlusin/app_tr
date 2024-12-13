
#from parler.models import TranslatableModel, TranslatedFields ##esiminch


from django.contrib.auth.models import AbstractUser
from django.db import models
from phone_field import PhoneField 
from django.utils.translation import gettext_lazy as _


from .managers import CustomUserManager

class CustomUser(AbstractUser):
    username = None  ## => aranc logini 
    email = models.EmailField(_("email address"), unique=True) 
    phone =  PhoneField(blank=True, help_text = 'Phone number')


    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email
