from django.shortcuts import render
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework import status

from .models import Data_API_read, Data_API_read_write
from .serializers import Data_Serializer_read, Data_Serializer_read_write
    

from rest_framework.response import Response
from rest_framework.decorators import api_view
import requests
import json

@api_view(['GET'])
def Show_all_read(request):
    data = Data_API_read.objects.all()
    serializer = Data_Serializer_read(data, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def Show_all_read_write(request):
    data = Data_API_read_write.objects.all()
    serializer = Data_Serializer_read_write(data, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def Create_API_read(request):
    serializer = Data_Serializer_read(data=request.query_params)
    if serializer.is_valid():

        if serializer.is_valid():
            serializer.save()

            return JsonResponse({
                'message': 'Data Success!'
            }, status=status.HTTP_200_OK)

        return JsonResponse({
            'message': 'Lỗi, tạo API thành công!'
        }, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response(serializer.errors, status=400)
    
@api_view(['GET'])
def Create_API_read_write(request):
    serializer = Data_Serializer_read_write(data=request.query_params)
    if serializer.is_valid():

        if serializer.is_valid():
            serializer.save()

            return JsonResponse({
                'message': 'Data Success!'
            }, status=status.HTTP_200_OK)

        return JsonResponse({
            'message': 'Lỗi, tạo API thành công!'
        }, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response(serializer.errors, status=400)


def update_data_read(request):
    data = get_object_or_404(Data_API_read, pk=1)
    serializer = Data_Serializer_read(data, data=request.GET.dict())


    if serializer.is_valid():
        serializer.save()

        url = 'http://127.0.0.1:8000/Show_all_read/?format=json'
        response = requests.get(url)

        if response.status_code == 200:
            return JsonResponse({
                'message': json.dumps(response.json()) 
            }, status=status.HTTP_200_OK)

        return JsonResponse({'message': 'Cập nhật thành công!'}, status=status.HTTP_200_OK)

    return JsonResponse({'message': 'Lỗi, cập nhật không thành công!'}, status=status.HTTP_400_BAD_REQUEST)

def update_data_read_write(request):
    data = get_object_or_404(Data_API_read_write, pk=1)
    serializer = Data_Serializer_read_write(data, data=request.GET.dict())


    if serializer.is_valid():
        serializer.save()

        url = 'http://127.0.0.1:8000/Show_all_read_write/?format=json'
        response = requests.get(url)

        if response.status_code == 200:
            return JsonResponse(response.json(), safe=False)

        return JsonResponse({'message': 'Cập nhật thành công!'}, status=status.HTTP_200_OK)

    return JsonResponse({'message': 'Lỗi, cập nhật không thành công!'}, status=status.HTTP_400_BAD_REQUEST)


def delete_data_view(request, pk):
    car = get_object_or_404(Data_API_read, pk=pk)
    car.delete()
    return JsonResponse({'message': 'Xóa thành công!'}, status=status.HTTP_200_OK)

