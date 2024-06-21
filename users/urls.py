from .views import *
from users import views
from django.urls import path

urlpatterns=[
    path("user_base",views.user_base, name="user_base"),
    path("create_customer",views.create_customer, name="create_customer"),
]

