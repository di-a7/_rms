from django.shortcuts import render
from rest_framework.response import Response
from django.http import HttpResponse
from .models import *
from .serializers import CategorySerializer
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.serializers import ValidationError

# Create your views here.
@api_view(['GET','POST'])
def category_list(request):
   if request.method == 'GET':
      category = Category.objects.all()
      serializer = CategorySerializer(category,many = True)
      return Response(serializer.data)
   else:
      serializer = CategorySerializer(data = request.data)
      serializer.is_valid(raise_exception = True)
      serializer.save()
      
      return Response({"details":"Data has been created"},status=status.HTTP_201_CREATED)

@api_view(['GET','DELETE'])
def category_details(request,pk):
   category = Category.objects.get(pk = pk)
   if request.method == "GET":
      serializer = CategorySerializer(category)
      return Response(serializer.data)
   else:
      items = OrderItem.objects.filter(food__category = category).count()
      if items > 0:
         raise ValidationError({"details":"Orderitem related to this category exist."})
      else:
         category.delete()
         return Response({"details":"Category deleted"}, status= status.HTTP_404_NOT_FOUND)