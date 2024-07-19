from typing import Any
from django.test import TestCase
from .models import cosmic_order
from django.urls import reverse

class TestFormSet(TestCase):
    def test_new_recipe(self):
        data={
            "customer_name":"Tibarek",
            "order_no": 1001,
            "notify_party":"Tibarek",
            "consignee":"Tibarek",
            "notify_party":"Tibarek",
            "notify_party2":"Tibarek",
            "date":"7-7-2024",
            "freight":"Pre-paid",
            "freight_price":40,
            "payment_type":"Confirmed LC",
            "measurement_type":"Ltr",
            "transportation":"Sea",
            "shipment_type":"FOB",
            "approved_by":"",
            "PR_before_vat":1024,
            # "status":,
            "ref_no":12547,
            "total_quantity":40,
            "remaining":5,
            "supplier_name":"Tsegi",
            "port_of_loading":"Ethiopia",
            "port_of_discharge":"Ethiopia",
            "final_destination":"Ethiopia",
            "country_of_origin":"Ethiopia",
        }

        r = self.client.post(reverse('create_sales'), data=data)
        self.assertEqual(cosmic_order.objects.first().customer_name.count(),3)
