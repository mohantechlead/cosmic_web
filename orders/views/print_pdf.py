# from django.http import HttpResponse
# import datetime
# from django.template.loader import render_to_string
# from weasyprint import HTML
# import tempfile
# from django.db.models import *

def export_pdf(request):
    pass

    # response = HttpResponse(content_type='application/pdf')
    # response['Content-Disposition'] = 'attachement; filename=proforma_invoice' + \
    #     str(datetime.datetime.now())+'.pdf'
    # response['Content-Transfer-Encoding'] = 'binary'

    # html_string = render_to_string(
    #     'pdf_template/proforma_invoice.html', {'proforma_invoice': []})
    # html = HTML(string=html_string)

    # result = html.write_pdf()

    # with tempfile.NamedTemporaryFile(delete=True) as output:
    #     output.write(result)
    #     output.flush()
    #     output = open(output.name, 'rb')
    #     response.write(output.read())

    # return response
    
