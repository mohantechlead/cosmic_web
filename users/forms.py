from django import forms
from django.forms import ModelForm
from .models import *
from django.forms import inlineformset_factory

class CustomerForm(forms.ModelForm):
        
    class Meta:
   
        model = customer_profile
        fields = ['customer_name','customer_address','email','phone_number','contact_person','comments']

class SupplierForm(forms.ModelForm):
 
    class Meta:
   
        model = supplier_profile
        fields = ['supplier_name','supplier_address','email','phone_number','contact_person','comments']