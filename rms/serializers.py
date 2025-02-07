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
         "id",
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

class OrderItemSerializer(serializers.ModelSerializer):
   food_id = serializers.PrimaryKeyRelatedField(
      queryset = Food.objects.all(),
      source = 'food',
   )
   food_name = serializers.StringRelatedField(
      source = 'food'
   )
   class Meta:
      model = OrderItem
      fields = ['food_id','food_name']
      
class OrderSerializer(serializers.ModelSerializer):
   user = serializers.HiddenField(default = serializers.CurrentUserDefault())
   items = OrderItemSerializer(many = True)
   status = serializers.CharField(read_only = True)
   payment = serializers.BooleanField(read_only = True)
   class Meta:
      model = Order
      fields = [
         "user",
         "table",
         "total_price",
         "status",
         "payment",
         "items",
      ]

   def create(self, validated_data):
      items_data = validated_data.pop('items')
      order = Order.objects.create(**validated_data)
      
      for item in items_data:
         OrderItem.objects.create(order = order, food = item['food'])
      return order