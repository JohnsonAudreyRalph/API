from rest_framework import serializers
from .models import Data_API

class Data_Serializer(serializers.ModelSerializer):

    class Meta:
        model = Data_API
        fields = '__all__'