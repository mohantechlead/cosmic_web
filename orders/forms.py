from django import forms
from .models import *
from users.models import *
from users.forms import *

# ORDER FORM

class CosmicOrderForm(forms.ModelForm):
    
    order_no = forms.CharField(widget=forms.TextInput(attrs={'class': 'order_no form-control'}))

    class Meta:
   
        model = cosmic_order
        fields = ['freight_price','customer_name','supplier_name','order_no','date','payment_type','measurement_type','approved_by','PR_before_vat','total_quantity','transportation','shipment_type','freight','ref_no','notify_party','country_of_origin','final_destination','port_of_discharge','port_of_loading','notify_party2','consignee']
        
class OrderItemForm(forms.ModelForm):
   
    before_vat = forms.DecimalField(
        label='Total Price',
        required=False,
        widget=forms.TextInput(attrs={'class': 'before_vat form-control'})
    )
    measurement = forms.CharField(widget=forms.TextInput(attrs={'class': 'measurement form-control'}), required=False)
    quantity = forms.FloatField(widget=forms.TextInput(attrs={'class': 'quantity form-control' }))
    price = forms.DecimalField(widget=forms.TextInput(attrs={'class': 'price form-control'}))

    item_name = forms.ModelChoiceField(
        queryset=item_codes.objects.all(),
        empty_label="Item Name", 
        widget=forms.Select(attrs={'class': 'item_name form-control'}),
        to_field_name='item_name'
    )
    hs_code = forms.CharField(label='HS CODE', required=False, widget=forms.TextInput(attrs={'class': 'hs_codes form-control'}, ),  )
    
    
    class Meta:
   
        model = order_item
        fields = [ 'item_name','hs_code','price','quantity','before_vat','measurement']

class CosmicItemForm(forms.ModelForm):
    
    item_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'item_name form-control'}))
    hs_code = forms.DecimalField(widget=forms.TextInput(attrs={'class': 'hs_code form-control'}))
    
    class Meta:
   
        model = item_codes
        fields = ['item_name','hs_code']

# SHIPPING FORM

class ShippingItemForm(forms.ModelForm):
   
    measurement = forms.CharField(widget=forms.TextInput(attrs={'class': 'measurement form-control'}), required=False)
    quantity = forms.FloatField(widget=forms.TextInput(attrs={'class': 'quantity form-control' }))
    price = forms.DecimalField(widget=forms.TextInput(attrs={'class': 'price form-control'}))

    item_name = forms.ModelChoiceField(
        queryset=item_codes.objects.all(),
        empty_label="Item Name", 
        widget=forms.Select(attrs={'class': 'item_name form-control'}),
        to_field_name='item_name'
    )
    hs_code = forms.CharField(label='HS CODE', required=False, widget=forms.TextInput(attrs={'class': 'hs_codes form-control'}, ),  )
    
    
    class Meta:
   
        model = shipping_item
        fields = [ 'item_name','hs_code','price','quantity','measurement']