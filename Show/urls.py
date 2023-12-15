from django.urls import path
from .views import *

urlpatterns = [
    path('Show_All/', Show_all),
    path('New_api/', Create_API),
    path('update_data/', update_data),
    path('delete_data_view/<int:pk>/', delete_data_view)
]