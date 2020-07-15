from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import routers, serializers, viewsets, status
 
from .models import Recipe, Order, Dish
from .serializers import UserSerializer, RecipeSerializer, OrderSerializer, DishSerializer
from rest_framework.decorators import api_view

from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework import filters

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class RecipeViewSet(viewsets.ModelViewSet):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    # @action(detail=True, methods=['post'])
    # def update(self, request, pk=None):
    #     order = self.get_object()
    #     print("XXX", request)
    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        # self.perform_update(serializer)
        # change data to currently logged in user
        serializer.validated_data['user'] = request.user
        serializer.save()

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)

    # def partial_update(self, request, *args, **kwargs):
    #     print("YYY", request)
    #     instance = self.queryset.get(pk=kwargs.get('pk'))
    #     serializer = self.serializer_class(instance, data=request.data, partial=True)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()
    #     return Response(serializer.data)


class DishViewSet(viewsets.ModelViewSet):
    queryset = Dish.objects.all()
    serializer_class = DishSerializer

# class BookViewSet(viewsets.ModelViewSet):
#     """
#     List all workkers, or create a new worker.
#     """
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer
#     filter_backends = [filters.OrderingFilter]
#     ordering_fields = ['release_date']


@api_view(['GET', 'POST', 'DELETE'])
def order_list(request):
    if request.method == 'GET':
        orders = Order.objects.all()
        
        title = request.GET.get('title', None)
        if title is not None:
            orders = orders.filter(title__icontains=title)
        
        order_serializer = OrderSerializer(orders, many=True)
        return JsonResponse(order_serializer.data, safe=False)
        # 'safe=False' for objects serialization
 
    elif request.method == 'POST':
        order_data = JSONParser().parse(request)
        order_serializer = OrderSerializer(data=order_data)
        if order_serializer.is_valid():
            order_serializer.save()
            return JsonResponse(order_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(order_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        count = Order.objects.all().delete()
        return JsonResponse({'message': '{} Orders were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)
 
 
@api_view(['GET', 'PUT', 'DELETE'])
def order_detail(request, pk):
    try: 
        order = Order.objects.get(pk=pk) 
    except Order.DoesNotExist: 
        return JsonResponse({'message': 'The order does not exist'}, status=status.HTTP_404_NOT_FOUND) 
 
    if request.method == 'GET': 
        order_serializer = OrderSerializer(order) 
        return JsonResponse(order_serializer.data) 
 
    elif request.method == 'PUT': 
        order_data = JSONParser().parse(request) 
        order_serializer = OrderSerializer(order, data=order_data) 
        if order_serializer.is_valid(): 
            order_serializer.save() 
            return JsonResponse(order_serializer.data) 
        return JsonResponse(order_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
 
    elif request.method == 'DELETE': 
        order.delete() 
        return JsonResponse({'message': 'Order was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
    
        
@api_view(['GET'])
def order_list_published(request):
    orders = Order.objects.filter(published=True)
        
    if request.method == 'GET': 
        order_serializer = OrderSerializer(orders, many=True)
        return JsonResponse(order_serializer.data, safe=False)