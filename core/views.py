from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import serializers
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema_view,extend_schema,OpenApiParameter, OpenApiExample
from drf_spectacular.types import OpenApiTypes
from .serializer import LoginSerializer
from rest_framework.decorators import action

# Create your views here.
class Login(APIView):
   # @extend_schema(
   #       parameters=[
   #          OpenApiParameter(name='username', description='Username', required=True, type=str),
   #          OpenApiParameter(name='password', description='Password', required=True, type=str),
   #       ],
   #       methods=["POST"]
   # )
   @extend_schema(
        request=LoginSerializer,
        responses={204: None},
        methods=["POST"]
    )
   @action(detail=True, methods=['post'])
   def post(self, request):
      username = request.data.get('username')
      password = request.data.get('password')
      if username == None and password == None:
         raise serializers.ValidationError({
            "details":"Username and Password are both required."
         })
      user = authenticate(username = username, password = password)
      if user:
         token,_=Token.objects.get_or_create(user = user)
         return Response({
            "token":token.key,
            "user":username
         })