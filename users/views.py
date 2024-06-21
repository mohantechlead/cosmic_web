from django.shortcuts import render

def user_base(request):
    return render(request,'user_base.html')

def create_customer(request):
    return render(request,'create_customer.html')

