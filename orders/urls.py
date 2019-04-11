from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('orders', views.OrderView)

urlpatterns = [
    path('', views.index, name='index'),
    path('api/', include(router.urls)),
]
