from django.shortcuts import render

def create_sales(request):
    return render(request, 'create_sales.html')
