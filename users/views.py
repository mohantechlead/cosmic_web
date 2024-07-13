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

# def create_customer(request):
#     if request.method == 'POST':
#         email = request.POST['email']
#         form = CustomerForm(request.POST)
#         if form.errors:
#             print(form.errors)
#         if customer_profile.objects.filter(email = email). exists():
#             messages.error(request, 'Email Already exists')
#             return redirect('create_customer')
#         if form.is_valid():
#             try:
#                 form.save()
#                 messages.success(request, 'Successfully Submitted')
#             except Exception as e:
#                 print(f"Error: {e}")
#             return redirect('create_customer')
#     else:
        
#         form = CustomerForm()
#     return render(request, 'create_customer.html', {'form': form })

def create_customer(request):
    form = CustomerForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            try:
                form.save()
                success = 'Profile Created Successfully'
                # return JsonResponse({'msg': 'success'})
                return render(request, "create_customer.html")
            except Exception as e:
               print(f"Error: {e}")
               return HttpResponse(e)
        if form.errors == 'customer_name':
             print(form.errors)
        #      error = form.errors
        #      return HttpResponse(error)
    
    return render(request, 'create_customer.html', {'form': form})

def create_supplier(request):
    if request.method == 'POST':
        email = request.POST['email']
        form = SupplierForm(request.POST)
        if form.errors:
            print(form.errors)
        if customer_profile.objects.filter(email = email). exists():
            messages.error(request, 'Email Already exists')
            return redirect('create_customer')
        if form.is_valid():
            try:
                form.save()
                messages.success(request, 'Successfully Submitted')
            except Exception as e:
                print(f"Error: {e}")
            return redirect('create_customer')
    else:
        
        form = SupplierForm()
    return render(request, 'create_supplier.html', {'form': form })

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

