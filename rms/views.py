from django.shortcuts import render
from rest_framework.response import Response
from django.http import HttpResponse
from .models import *
from .serializers import *
from rest_framework.decorators import api_view
from rest_framework import status, viewsets
from rest_framework.serializers import ValidationError
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView, ListAPIView,CreateAPIView,RetrieveAPIView, DestroyAPIView,UpdateAPIView,RetrieveUpdateDestroyAPIView
from rest_framework.pagination import PageNumberPagination
# Create your views here.

class CategoryViewset(viewsets.ModelViewSet):
   queryset = Category.objects.all()
   serializer_class = CategorySerializers

class FoodViewset(viewsets.ModelViewSet):
   queryset = Food.objects.select_related('category').all()
   serializer_class = FoodSerializer
   pagination_class = PageNumberPagination

class TableList(ListCreateAPIView):
   queryset = Table.objects.all()
   serializer_class = TableSerializer