from django.shortcuts import render
from rest_framework.response import Response
from django.http import HttpResponse
from .models import Category
from .serializers import CategorySerializer
from rest_framework.decorators import api_view
# Create your views here.
@api_view(['GET'])
def category_list(request):
   category = Category.objects.all()
   serializer = CategorySerializer(category,many = True)
   return Response(serializer.data)