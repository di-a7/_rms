from django.urls import path,include
from .views import category_list
urlpatterns = [
   path('category-list',category_list),
]