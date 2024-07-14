from django.shortcuts import render
from django.shortcuts import render, redirect,get_object_or_404
from django.conf import settings
from .forms import *
from .models import *
from django.contrib.auth.decorators import login_required,user_passes_test
from django.forms import formset_factory,modelformset_factory
from django.db.models import Sum
from django.http import JsonResponse,HttpResponse
from django.template.loader import get_template
from django.contrib.auth.models import User, auth
from num2words import num2words
from django.contrib import messages

def user_base(request):
    return render(request,'user_base.html')

def create_customer(request):
    form = CustomerForm(request.POST)
    if request.method == 'POST':
        customer_name = request.POST['customer_name']
        if customer_profile.objects.filter(customer_name__icontains= customer_name).exists():
                messages.error(request, 'Customer Name already exists')
                return redirect('create_customer')
        else:
              if form.is_valid:
                form.save()
                messages.success(request, 'Profile Created Successfully')
                return render(request, "create_customer.html")
         
    
    return render(request, 'create_customer.html', {'form': form})

def delete_customer(request, customer_name): 
    # request.customer_profile.customer_name.remove(customer_name)
    
    customer = customer_profile.objects.filter(customer_name = customer_name)
    customer.delete()
    
    return render(request, 'customer_list.html' ,{'customer': customer})

def create_supplier(request):
    form = SupplierForm(request.POST)
    if request.method == 'POST':
        supplier_name = request.POST['supplier_name']
        if supplier_profile.objects.filter(supplier_name__icontains= supplier_name).exists():
                messages.error(request, 'Supplier Name already exists')
                return redirect('create_supplier')
        else:
              if form.is_valid:
                form.save()
                messages.success(request, 'Profile Created Successfully')
                return render(request, "create_supplier.html")
         
    
    return render(request, 'create_supplier.html', {'form': form})

def display_customer(request):
    if request.method == 'GET':
        customers = customer_profile.objects.all()
        context = {
                    'my_customer': customers,
                }
          
    return render(request, 'display_customer.html', context)

def display_supplier(request):
    if request.method == 'GET':
        suppliers = supplier_profile.objects.all()
        context = {
                    'my_supplier': suppliers,
                }
          
    return render(request, 'display_supplier.html', context)

