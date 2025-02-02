from rest_framework import serializers
from .models import *

class CategorySerializers(serializers.ModelSerializer):
   class Meta:
      model = Category
      fields = ['id','name']
   
   def save(self,**kwargs):
      validated_data = self.validated_data
      total_number = self.Meta.model.objects.filter(name = validated_data.get('name')).count()
      if total_number > 0:
         raise serializers.ValidationError("Category already exists.")
      
      # category = Category(**validated_data)
      # Category(name = validated_data.get('name'))
      
      category = self.Meta.model(**validated_data)
      category.save()
      return category


class FoodSerializer(serializers.ModelSerializer):
   price_with_tax = serializers.SerializerMethodField()
   category = serializers.StringRelatedField()
   category_id = serializers.PrimaryKeyRelatedField(
      queryset = Food.objects.all(),
      source = 'category'
   )
   class Meta:
      fields = (
         "name",
         "price_with_tax",
         "price",
         "category_id",
         "category",
      )
      model = Food
   
   def get_price_with_tax(self, food:Food):
      return food.price * 0.13 + food.price
class TableSerializer(serializers.ModelSerializer):
   class Meta:
      model = Table
      fields = '__all__'