from django.shortcuts import render
from rest_framework import viewsets
from .models import Order
from .serializers import OrderSerializer
from .xmlRead import loadXML

class OrderView(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

def index(request):
    url = 'http://test.lengow.io/orders-test.xml'
    orders = loadXML(url)
    context = {
        'url': url,
        'orders': orders
    }
    return render(request, 'orders/index.html', context)