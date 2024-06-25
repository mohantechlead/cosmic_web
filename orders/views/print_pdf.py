from django.shortcuts import render,redirect
from users.models import *
from django.http import JsonResponse,HttpResponse
from django.forms import formset_factory
from orders.forms import *
from users.forms import *
from num2words import num2words

from io import BytesIO
from django.template.loader import get_template
from xhtml2pdf import pisa
import os
from django.conf import settings


def fetch_resources(uri,rel):
    path = os.path.join(uri.replace(settings.STATIC_URL, ""))
    return path

def render_to_pdf(template_src, context_dict={}):
    template = get_template(template_src)
    html = template.render(context_dict)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode('ISO-8859-1')), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return None

class GenrateInvoice(View):
    def get(self, request, pk, *args, **kwargs):
        try:
            order_db = cosmic_order.get(id = pk )
    