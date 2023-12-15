from django.urls import path
from .views import *

urlpatterns = [
    path('api', ListCreateCarView.as_view()),
    path('api/<int:pk>', UpdateDeleteCarView.as_view()),
    path('New_api/', my_api_view),
]