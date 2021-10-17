from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.db import transaction
from accounts.models import User,HSEB
from phonenumber_field.modelfields import PhoneNumberField
from django.core.validators import RegexValidator



class HSEBSignUpForm(UserCreationForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    address = forms.CharField(required=True)
    phone_number = forms.CharField(required=True,validators=[
      RegexValidator(
        regex=r'[9][0-9]{9}',
        message="Phone number must be entered in the format '9861165523'. ." 
      ),
    ])
    citizenship_no = forms.CharField(required=True)
 
    class Meta(UserCreationForm.Meta):
        model = User
    
    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_hseb = True
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.save()
        HSEB1 = HSEB.objects.create(user=user)
        HSEB1.address=self.cleaned_data.get('address')
        HSEB1.phone_number=self.cleaned_data.get('phone_number')
        HSEB1.citizenship_no=self.cleaned_data.get('citizenship_no')
        HSEB1.save()
        return user

