from django.shortcuts import render
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from .models import Data_API
from .serializers import Data_Serializer

# Create your views here.
# class ListCreateCarView(ListCreateAPIView):
#     model = Data_API
#     serializer_class = Data_Serializer

#     def get_queryset(self):
#         return Data_API.objects.all()

#     def create(self, request, *args, **kwargs):
#         serializer = Data_Serializer(data=request.data)

#         if serializer.is_valid():
#             serializer.save()

#             return JsonResponse({
#                 'message': 'Thực hiện tạo mới thành công!'
#             }, status=status.HTTP_201_CREATED)

#         return JsonResponse({
#             'message': 'Lỗi, chưa tạo mới thành công!'
#         }, status=status.HTTP_400_BAD_REQUEST)


# class UpdateDeleteCarView(RetrieveUpdateDestroyAPIView):
#     model = Data_API
#     serializer_class = Data_Serializer

#     def put(self, request, *args, **kwargs):
#         data = get_object_or_404(Data_API, id=kwargs.get('pk'))
#         serializer = Data_Serializer(data, data=request.data)

#         if serializer.is_valid():
#             serializer.save()

#             return JsonResponse({
#                 'message': 'Cập nhật thành công!'
#             }, status=status.HTTP_200_OK)

#         return JsonResponse({
#             'message': 'Lỗi, cập nhật không thành công!'
#         }, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, *args, **kwargs):
#         car = get_object_or_404(Data_API, id=kwargs.get('pk'))
#         car.delete()

#         return JsonResponse({
#             'message': 'Xóa thành công!'
#         }, status=status.HTTP_200_OK)
    

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
        # Xử lý dữ liệu nếu hợp lệ
        # validated_data = serializer.validated_data

        # url = 'http://127.0.0.1:8000/Show_All/?format=json'
        # response = requests.get(url)

        if serializer.is_valid():
            serializer.save()

            # if response.status_code == 200:
            #     return JsonResponse({
            #         'message': json.dumps(response.json()) 
            #     }, status=status.HTTP_200_OK)
            

            return JsonResponse({
                'message': 'Data Success!'
            }, status=status.HTTP_200_OK)

        return JsonResponse({
            'message': 'Lỗi, cập nhật không thành công!'
        }, status=status.HTTP_400_BAD_REQUEST)
    else:
        # Nếu dữ liệu không hợp lệ, trả về lỗi hoặc thông báo lỗi
        return Response(serializer.errors, status=400)


def update_data(request, pk):
    data = get_object_or_404(Data_API, pk=pk)
    serializer = Data_Serializer(data, data=request.GET.dict())

    url = 'http://127.0.0.1:8000/Show_All/?format=json'
    response = requests.get(url)

    if serializer.is_valid():
        serializer.save()


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

