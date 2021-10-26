from django.urls import path
from .views import *

app_name = 'newcom'

urlpatterns = [
    path('ids/', id_list),
    path('ids/<int:pk>/', id_detail),
    path('pro/', product_list),
]
