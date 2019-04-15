from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('orders', views.OrderView)
router.register('products', views.ProductView)

urlpatterns = [
    path('', views.index, name='index'),
    path('orders/', views.orders, name='orders'),
    path('form/', views.form, name='form'),
    path('api/', include(router.urls), name='api'),
]
