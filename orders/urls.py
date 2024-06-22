from django.urls import path
from orders import views

urlpatterns = [
    path(r'^create_sales', views.create_sales, name="create_sales")
]