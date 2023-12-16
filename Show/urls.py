from django.urls import path
from .views import *

urlpatterns = [
    path('Show_all_read/', Show_all_read),
    path('Show_all_read_write/', Show_all_read_write),

    # path('New_api_read/', Create_API_read),
    # path('New_api_read_write/', Create_API_read_write),

    path('update_data_read/', update_data_read),
    path('update_data_read_write/', update_data_read_write),

    path('delete_data_view/<int:pk>/', delete_data_view)
]