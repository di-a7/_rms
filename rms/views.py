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
from rest_framework import filters
from .permission import IsAuthenticatedOrReadOnly
from rest_framework.permissions import IsAuthenticated
from django_filters import rest_framework as filter
from .filters import FoodFilter
# Create your views here.

class CategoryViewset(viewsets.ModelViewSet):
   queryset = Category.objects.all()
   serializer_class = CategorySerializers
   permission_classes = [IsAuthenticatedOrReadOnly]

class FoodViewset(viewsets.ModelViewSet):
   queryset = Food.objects.select_related('category').all()
   serializer_class = FoodSerializer
   pagination_class = PageNumberPagination
   filter_backends = [filters.SearchFilter,filter.DjangoFilterBackend]
   filterset_class = FoodFilter
   # filterset_fields = ('category',)
   search_fields = ('name',)
   permission_classes = [IsAuthenticatedOrReadOnly]

class TableList(ListCreateAPIView):
   queryset = Table.objects.all()
   serializer_class = TableSerializer

class OrderViewset(viewsets.ModelViewSet):
   queryset = Order.objects.prefetch_related('items').all()
   serializer_class = OrderSerializer
   pagination_class = PageNumberPagination
   permission_classes = [IsAuthenticated]

from django.core.mail import send_mail
def sendmail(request):
   send_mail(
      subject = "Order",
      message ="Your order has been created.",
      from_email='shtdia0@gmail.com',
      recipient_list=['abc@gmail.com'],
   )
   return HttpResponse({
      "detail":"Mail Sent"
   })