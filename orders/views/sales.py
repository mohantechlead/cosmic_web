from django.shortcuts import render,redirect
from users.models import *
from django.http import JsonResponse
from django.forms import formset_factory
from orders.forms import *
from users.forms import *
from num2words import num2words

def create_sales(request):
    if request.method == 'POST':
        form = CosmicOrderForm(request.POST)
        print(form.data)
        if form.errors:
            print(form.errors) 

        if form.is_valid():
            print(form.data,"val")
            customers_name = request.POST.get('customer_name') 
            notify_party = request.POST.get('notify_party') 
            suppliers_name = request.POST.get('supplier_name') 

            customer = customer_profile.objects.get(customer_name=customers_name)
            if notify_party:
                notify_1 = customer_profile.objects.get(customer_name=notify_party)
                form.instance.notify_party = notify_1
            supplier = supplier_profile.objects.get(supplier_name=suppliers_name)
            form.instance.customer_name = customer
            form.instance.supplier_name = supplier
            form.save()
            return redirect('create_sales')  # Redirect to the list of purchases or any other desired view
        else:
            print(form.data,"nval")
            errors = dict(form.errors.items())
            print(errors,"errors")
            return JsonResponse({'form_errors': errors}, status=400)
        
    form = CosmicOrderForm()
    formset = formset_factory(OrderItemForm, extra=1)
    formset = formset(prefix="items")

    customers = customer_profile.objects.all()
    suppliers = supplier_profile.objects.all()
    
    context = {
        'form': form, 
        'formset': formset, 
        'customers': customers,
        'suppliers':suppliers
        
    }

    return render(request, 'sales/create_sales.html', context)

def create_sale_items(request):
    if request.method == 'POST':
        formset = formset_factory(OrderItemForm, extra=1, min_num=1)
        
        formset = formset(request.POST or None,prefix="items")
        #print(formset.data,"r")
      
        if formset.errors:
            print(formset.errors)   
        
        # Check if 'PR_no' field is empty in each form within the formset
        for form in formset:
            print(form,"form")
        non_empty_forms = [form for form in formset if form.cleaned_data.get('item_name')]
        pr_no = request.POST.get('order_no')
        if non_empty_forms:
            if formset.is_valid():
                final_quantity = 0.0
                final_price = 0.00
                pr = cosmic_order.objects.get(order_no=pr_no)
                for form in non_empty_forms:
                    form.instance.remaining = form.cleaned_data['quantity']
                    form.instance.order_no = pr
                    items = form.cleaned_data['item_name']
                    item = item_codes.objects.all()
                    item = item.filter(item_name = items).first()
                    code = item.hs_code
                    form.instance.hs_code = code
                    final_quantity += form.cleaned_data['quantity']
                    final_price += float(form.cleaned_data['before_vat'])
                    
                    form.save()
                
                pr.PR_before_vat = final_price
                pr.total_quantity = final_quantity
                pr.remaining = final_quantity
                pr.save()
                #message.success("successful!")
            else:
                print(formset.data,"nval")
                errors = dict(formset.errors.items())
                return JsonResponse({'form_errors': errors}, status=400)
        
            pr_form = CosmicOrderForm(prefix="orders")
            formset = formset_factory(OrderItemForm, extra=1)
            formset = formset(prefix="items")

            context = {
                'pr_form': pr_form,
                'formset': formset,
                # 'message':success_message,
                'code':code
            }
            return render(request, 'sales/create_sales.html', context)
    else:
       
        formset = formset_factory(OrderItemForm, extra=1)
        formset = formset(prefix="items")

    context = {
        'formset': formset,
    }
    return render(request, 'sales/create_sales.html', context)

def display_sales(request):
    if request.method == 'GET':
        orders = cosmic_order.objects.all()
        orders = orders.order_by('order_no')

        orders_data = []
        for order in orders:
            # Fetch all order items related to each cosmic order
            order_items = order_item.objects.filter(order_no=order.order_no)

            # Create a dictionary containing order details and items
            order_data = {
                'order_no': order.order_no,
                'date': order.date,  # Assuming 'date' is a field in CosmicOrder
                'order_items': order_items,  # Assuming a related name 'order_items' on CosmicOrder pointing to OrderItem
                'PR_before_vat': order.PR_before_vat,  # Assuming 'PR_before_vat' is a field in CosmicOrder
                'total_quantity': order.total_quantity,  # Assuming 'total_quantity' is a field in CosmicOrder
                'customer_name': order.customer_name,  # Assuming 'customer_name' is a field in CosmicOrder
                'status': order.status,  # Assuming 'status' is a field in CosmicOrder
            }
            orders_data.append(order_data)

    context = {
        'my_order': orders_data,
    }
    return render(request, 'sales/display_sales.html', context)

def display_single_sale(request,order_no):
    if request.method == 'GET':
        # pr_no = request.GET['order_no']
          
        try:
            orders = cosmic_order.objects.get(order_no=order_no)
            pr_items = order_item.objects.all()
            pr_items = pr_items.filter(order_no=order_no)
            print(pr_items)
        except cosmic_order.DoesNotExist:
            order = None 
        # try:
            
        #     invoices = shipping_info.objects.all()
        #     invoices = invoices.filter(order_no = pr_no)
        # except shipping_info.DoesNotExist:
        #     try:
        #         print("trial")
        #         invoices = shipping_info.objects.all()
        #         invoices = invoices.filter(order_no = pr_no)
        #     except shipping_info.DoesNotExist:
        #         invoices = None
        #     invoices = None
        if pr_items.exists():
            print(pr_items,"yes")
            context = {
                        'pr_items': pr_items,
                        'my_order': orders,
                        # 'the_invoices':invoices,
                    }
            return render(request, 'sales/display_single_sale.html', context)
        context = {
                        
                        'my_order': orders,
                        # 'the_invoices':invoices
                    }
    return render(request, 'sales/display_single_sale.html', context)

def pr_invoice(request):
    if request.method == 'GET':
        if 'order_no' in request.GET:
            pr_no = request.GET['order_no']
        
        try:
            orders = cosmic_order.objects.get(order_no=pr_no)
            pr_items = order_item.objects.all()
            pr_items = pr_items.filter(order_no=pr_no)
            proforma_type = "order"
            
        except cosmic_order.DoesNotExist:
                orders = None
        
        if hasattr(orders, 'PR_before_vat'):
            number = float(orders.PR_before_vat)
            print("yes")
        else:
            number = float(orders.before_vat)
            print(orders.before_vat)

        if orders.freight_price:
            number += float(orders.freight_price)
        #print(shipping.freight_amount,"fr")
        dicts = {1:"TEN",2:"TWENTY",3:"THIRTY",4:"FORTY",5:"FIFTY",6:"SIXTY",7:"SEVENTY",8:"EIGHTY",9:"NINTY"}
        
        print(number)
        whole_part, decimal_part = str(number).split('.')
        number_in_words = num2words(whole_part)
        number_in_words = number_in_words.replace(',', '')
        number_in_words = number_in_words.replace('-', ' ')
        num = number_in_words.upper()
        if int(decimal_part) in dicts:
            dec = " AND " + str(dicts[int(decimal_part)]) + " CENTS ONLY"
        elif decimal_part == "0":
            dec = " ONLY"
        else:
            dec = " AND " + num2words(decimal_part) + " CENTS ONLY"
        print(decimal_part,dec)
        num = num.replace(' AND', '')
        num += dec 
        print(orders, num)
        print("no")
        
        if pr_items.exists():
            print(pr_items,"yes")
            context = {
                        'pr_items': pr_items,
                        'my_order': orders,
                        'num': num,
                        'number':number,
                        'type': proforma_type,
                        
                    }
            return render(request, 'sales/pr_invoice.html', context)
       
        context = {
                        
                        'my_order': orders,
                        'num': num,
                        'number':number,
                        'type': proforma_type,
                       
                    }
       
    return render(request, 'sales/pr_invoice.html', context)

