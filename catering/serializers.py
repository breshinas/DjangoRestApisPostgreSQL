from django.contrib.auth.models import User
from rest_framework import serializers
from catering.models import Recipe, Order, Dish

# Serializers define the API representation.
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password')

class RecipeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Recipe
        fields = ('id',
                  'name',
                  'url',
                  'amount')

class OrderSerializer(serializers.ModelSerializer):
    # dishes = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Order
        fields = ('id',
                  'created',
                  'user',
                  'customer',
                  'totalDishes',
                  'totalCount',
                  'totalAmount')

class DishSerializer(serializers.ModelSerializer):

    class Meta:
        model = Dish
        fields = ('id',
                  'order',
                  'recipe',
                  'user',
                  'count',
                  'amount',
                  'created')