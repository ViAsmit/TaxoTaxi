from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from . import models
from customer import models as customermodels

class ContactForm(forms.ModelForm):
    class Meta:
        model = models.contact
        fields = '__all__'

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = models.User
        fields = ['first_name', 'last_name', 'email', 'mobile', 'profile_pic']

class AssignVendorsForm(forms.ModelForm):
    class Meta:
        model = models.assign_vendor
        exclude = ['booking', 'datetime']

class VendorBidsForm(forms.ModelForm):
    class Meta:
        model = models.vendorbids
        exclude = ['booking', 'vendor', 'datetime']

class FinalVendorForm(forms.ModelForm):
    class Meta:
        model = models.final_ride_detail
        fields = ['bid']

class AssignDriverCar(forms.ModelForm):
    class Meta:
        model = models.final_ride_detail
        fields = ['car', 'driver']