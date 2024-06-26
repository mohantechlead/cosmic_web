from django.db import models

class customer_profile(models.Model):
    customer_name = models.TextField(blank=False,primary_key=True)
    customer_address = models.TextField(blank=False)
    contact_person = models.TextField(blank=True)
    phone_number = models.TextField(blank=False, null=True)  
    email = models.TextField(blank=True, null=True)
    comments = models.TextField(blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True, blank=True)
    
    def __str__(self):
        return self.customer_name
    

class supplier_profile(models.Model):
    supplier_name = models.TextField(primary_key=True, blank=False)
    supplier_address = models.TextField(blank=False)
    contact_person = models.TextField(blank=True)
    phone_number = models.CharField(blank=False, null=True) 
    email = models.TextField(blank=True, null=True)
    comments = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    
    def __str__(self):
        return self.supplier_name