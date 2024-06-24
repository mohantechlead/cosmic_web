from django.urls import path
from .views import *

urlpatterns = [
    path('create_sales', sales.create_sales, name="create_sales"),
    path('display_sales', sales.display_sales, name="display_sales"),
    path('display_single_sale/<str:order_no>', sales.display_single_sale, name="display_single_sale"),
    path('create_sale_items', sales.create_sale_items, name="create_sale_items"),
    path('display_items', items.display_items, name='display_items'),
    path('pr_invoice', sales.pr_invoice, name='pr_invoice'),
    path('get_item_data/<str:item_id>/', get_item_data, name='get_item_data'),
]