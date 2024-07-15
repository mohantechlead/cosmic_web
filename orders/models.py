from django.db import models
from users.forms import *
from users.models import *
import uuid

class cosmic_order(models.Model):
    customer_name = models.ForeignKey('users.customer_profile', related_name='orders_related_to_customer',on_delete=models.CASCADE, db_column='customer_name',blank=False, null=True)
    order_no = models.TextField(primary_key=True)
    notify_party = models.ForeignKey('users.customer_profile', related_name='notify_party_one',on_delete=models.CASCADE, blank=True, null=True,db_column='notify_party')
    consignee = models.ForeignKey('users.customer_profile', related_name='consignee',on_delete=models.CASCADE, blank=True, null=True,db_column='consignee')
    notify_party2 = models.ForeignKey('users.customer_profile', related_name='orders_related_to_bank', on_delete=models.CASCADE, db_column='notify_party2',blank=True, null=True)
    date = models.DateField(blank=False)
    freight = models.TextField(blank=True, null=True)
    freight_price = models.FloatField(blank=True, null=True)
    payment_type = models.TextField(blank=True, null=True)
    measurement_type = models.TextField(blank=True, null=True)
    transportation = models.TextField(blank=True, null=True)
    shipment_type = models.TextField(blank=True, null=True)
    approved_by = models.TextField(blank=True, null=True)
    PR_before_vat = models.FloatField(blank=True, null=True)
    status = models.TextField(blank=True, null=True, default="Pending")
    ref_no = models.TextField(blank=False, null=True)
    total_quantity = models.FloatField(blank=True, null=True)
    remaining =  models.FloatField(blank=True, null=True)
    supplier_name = models.ForeignKey('users.supplier_profile', related_name='orders_related_to_supplier',on_delete=models.CASCADE, blank=False, null=True, db_column='supplier_name')
    port_of_loading = models.TextField(blank=False, null=True)
    port_of_discharge = models.TextField(blank=True, null=True)
    final_destination = models.TextField(blank=True, null=True)
    country_of_origin = models.TextField(blank=False, null=True)
    
    
class order_item(models.Model):
    order_no = models.ForeignKey('cosmic_order', on_delete=models.CASCADE, db_column='order_no',blank=True, null=True)
    id_numeric = models.AutoField(primary_key=True)
    hs_code = models.TextField(blank=True, null=True)
    item_name = models.TextField(blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    before_vat = models.FloatField(blank=True, null=True)
    quantity =  models.FloatField(blank=True, null=True)
    measurement = models.TextField(blank=True, null=True)

class shipping_item(models.Model):
    order_no = models.ForeignKey('cosmic_order', on_delete=models.CASCADE, db_column='order_no',blank=True, null=True)
    id_numeric = models.AutoField(primary_key=True)
    price = models.FloatField(blank=True, null=True)
    item_name = models.TextField(blank=True, null=True)
    quantity =  models.FloatField(blank=True, null=True)
    total_price = models.FloatField(blank=True, null=True)
    measurement = models.TextField(blank=True, null=True)
    bags = models.FloatField(blank=True, null=True)
    net_weight = models.FloatField(blank=True, null=True)
    gross_weight = models.FloatField(blank=True, null=True)
    
class item_codes(models.Model):
    hs_code = models.TextField(blank=True, null=True)
    item_name = models.TextField(blank=True, null=True)
    new_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    
    def __str__(self):
        return self.item_name
    



