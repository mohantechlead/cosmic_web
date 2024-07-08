from django.shortcuts import render,redirect
from users.models import *
from django.http import JsonResponse,HttpResponse
from django.forms import formset_factory
from orders.forms import *
from users.forms import *
from num2words import num2words
from django.views import View

from io import BytesIO
from django.template.loader import get_template
from xhtml2pdf import pisa
import os
from django.conf import settings

def render_to_pdf(template_src, context_dict={}):
    template = get_template(template_src)
    html = template.render(context_dict)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return None

data = {
    "company": "Tibarek",
    "address": "123 Street Name",
    "city": "Vancouver",
    "state": "WA",
    "zipcode": "98663",

    "phone": "555-2225-2466",
    "email": "tibarel@gmail.com",
    "website": "tibarek.com"
}

# class ViewPDF(View):
#     def get(self, request, *args, **kwargs):

#         pdf = render_to_pdf('pdf_template/proforma_invoice.html', data)
#         return HttpResponse(pdf, content_type='application/pdf')

def ViewPDF(request):
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
            # return render(request, 'sales/pr_invoice.html', context)
            pdf = render_to_pdf('pdf_template/proforma_invoice.html', context)
            return HttpResponse(pdf, content_type='application/pdf')
       
        context = {
                        
                        'my_order': orders,
                        'num': num,
                        'number':number,
                        'type': proforma_type,
                       
                    }
       
    # return render(request, 'sales/pr_invoice.html', context)
    pdf = render_to_pdf('pdf_template/proforma_invoice.html', context)
    return HttpResponse(pdf, content_type='application/pdf')

    

    
class DownloadPDF(View):
    def get(self, request, *args, **kwargs):
        
        pdf = render_to_pdf('pdf_template/proforma_invoice.html', data)

        response = HttpResponse(pdf, content_type='application/pdf')
        filename = "Invoice_%s.pdf" %("121341231")
        content = "attachement; filename='%s'" %(filename)
        response['Content-Disposition'] = content
        return response
    
# def index(request):
#     context = {}
#     return render(request, '/index.html', context)
    