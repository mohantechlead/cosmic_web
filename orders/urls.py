from django.urls import path
from orders import views

urlpatterns = [
    path('create_sales', views.create_sales, name="create_sales")
]