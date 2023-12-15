from django.shortcuts import render
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework import status

from .models import Data_API
from .serializers import Data_Serializer
    

from rest_framework.response import Response
from rest_framework.decorators import api_view
import requests
import json

@api_view(['GET'])
def Show_all(request):
    data = Data_API.objects.all()
    serializer = Data_Serializer(data, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def Create_API(request):
    serializer = Data_Serializer(data=request.query_params)
    if serializer.is_valid():

        if serializer.is_valid():
            serializer.save()

            return JsonResponse({
                'message': 'Data Success!'
            }, status=status.HTTP_200_OK)

        return JsonResponse({
            'message': 'Lỗi, cập nhật không thành công!'
        }, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response(serializer.errors, status=400)


def update_data(request):
    data = get_object_or_404(Data_API, pk=1)
    serializer = Data_Serializer(data, data=request.GET.dict())


    if serializer.is_valid():
        serializer.save()

        url = 'http://127.0.0.1:8000/Show_All/?format=json'
        response = requests.get(url)

        if response.status_code == 200:
            return JsonResponse({
                'message': json.dumps(response.json()) 
            }, status=status.HTTP_200_OK)

        return JsonResponse({'message': 'Cập nhật thành công!'}, status=status.HTTP_200_OK)

    return JsonResponse({'message': 'Lỗi, cập nhật không thành công!'}, status=status.HTTP_400_BAD_REQUEST)


def delete_data_view(request, pk):
    car = get_object_or_404(Data_API, pk=pk)
    car.delete()
    return JsonResponse({'message': 'Xóa thành công!'}, status=status.HTTP_200_OK)

