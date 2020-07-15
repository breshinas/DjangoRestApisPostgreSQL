from django.conf.urls import url 
from catering import views #, UserViewSet, RecipeViewSet, OrderViewSet, DishViewSet
 
# urlpatterns = [ 
#     url(r'^api/orders$', views.order_list),
#     url(r'^api/orders/(?P<pk>[0-9]+)$', views.order_detail),
#     url(r'^api/orders/published$', views.order_list_published)
# ]

from django.contrib.auth.models import User
from django.urls import path, include

# #from django.urls import path, url, include

from rest_framework.routers import DefaultRouter
from rest_framework import routers


# Routers provide an easy way of automatically determining the URL conf.

router = DefaultRouter()
router.register(r'api/users', views.UserViewSet, basename='user')
router.register(r'api/recipes', views.RecipeViewSet, basename='recipe')
router.register(r'api/orders', views.OrderViewSet, basename='order')
router.register(r'api/dishes',views. DishViewSet, basename='dish')


# Wire up our API using automatic URL routing.
urlpatterns = [
    path(r'', include(router.urls)),
]