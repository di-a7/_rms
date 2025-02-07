from django.urls import path,include
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'category',CategoryViewset, basename='category')
router.register(r'foods',FoodViewset, basename='foods')
router.register(r'order',OrderViewset, basename='order')

urlpatterns = [
   path('sendmail',sendmail)
] + router.urls