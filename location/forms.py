from django import forms
from .models import Building
from django.utils.translation import gettext as _


class LocationSearchForm(forms.Form):
    q = forms.CharField()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['q'].label = 'Search For'
        self.fields['q'].widget.attrs.update({
            'class':"form-control"
        })
