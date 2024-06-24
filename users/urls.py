from .views import *
from users import views
from django.urls import path

urlpatterns=[
    path("",views.user_base, name="user_base"),
    path("create_customer",views.create_customer, name="create_customer"),
    path("create_supplier",views.create_supplier, name="create_supplier"),
    path("display_customer",views.display_customer, name="display_customer"),
    path("display_supplier",views.display_supplier, name="display_supplier"),
]

