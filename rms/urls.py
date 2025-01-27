from django.urls import path,include
from .views import *
urlpatterns = [
   path('category-list',category_list),
   path('category-detail/<pk>/',category_details),
]