from cProfile import label
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.forms import UserCreationForm
from django import forms

# from django.contrib.auth.models import User
from .models import CustomUser
from django.utils.translation import gettext as _


class CreateUserForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ["first_name", "last_name", "email", "password1", "password2", "phone"]


# class CreateUserForm(forms.Form):
#     your_name = forms.CharField(label="Your name", max_length=100)


class CreatePost(forms.Form):
    post = forms.CharField(
        label=_("Ձեր կարծիքը։"),
        strip=False,
        required=False,
        widget=forms.TextInput(
            attrs={
                "size": 40,
                "title": _("Ձեր կարծիքը։"),
            }
        ),
    )
    gnahatakan = forms.IntegerField(label=_('Ձեր գնահատականը։'),
        validators=[
            MinValueValidator(
                1, message=_("Խնդհրում ենք ներմուծել մեկից մեծ գնահատական")
            ),
            MaxValueValidator(
                5, message=_("Խնդհրում ենք ներմուծել հինգից փոքր գնահատական")
            ),
        ]
    )
