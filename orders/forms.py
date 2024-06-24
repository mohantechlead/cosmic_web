from django import forms
from .models import *
from users.models import *
from users.forms import *

class CosmicOrderForm(forms.ModelForm):
    
    order_no = forms.CharField(widget=forms.TextInput(attrs={'class': 'order_no form-control'}))

    class Meta:
   
        model = cosmic_order
        fields = ['freight_price','customer_name','supplier_name','order_no','date','payment_type','measurement_type','approved_by','PR_before_vat','total_quantity','transportation','shipment_type','freight','ref_no','notify_party','country_of_origin','final_destination','port_of_discharge','port_of_loading','notify_party2','consignee']
        
class OrderItemForm(forms.ModelForm):
   
    before_vat = forms.DecimalField(
        label='Total Price',
        required=False,
        widget=forms.TextInput(attrs={'class': 'before_vat form-control', 'readonly': 'readonly'})
    )
    measurement = forms.CharField(widget=forms.TextInput(attrs={'class': 'measurement form-control'}), required=False)
    quantity = forms.FloatField(widget=forms.TextInput(attrs={'class': 'quantity form-control' }))
    price = forms.DecimalField(widget=forms.TextInput(attrs={'class': 'price form-control'}))

    item_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter name'}),
    )
    
    
    class Meta:
   
        model = order_item
        fields = [ 'item_name','price','quantity','before_vat','measurement']
