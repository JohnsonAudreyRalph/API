from rest_framework import serializers
from .models import Data_API_read, Data_API_read_write

class Data_Serializer_read(serializers.ModelSerializer):
    class Meta:
        model = Data_API_read
        fields = '__all__'

class Data_Serializer_read_write(serializers.ModelSerializer):
    class Meta:
        model = Data_API_read_write
        fields = '__all__'