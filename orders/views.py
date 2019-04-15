from django.shortcuts import render
from rest_framework import viewsets
from .models import Order, Product
from .serializers import OrderSerializer, ProductSerializer
from .xmlRead import loadXML
from django.http import HttpResponseRedirect
from .formMethod import formGet, formPost
from itertools import chain

class OrderView(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class ProductView(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

context = {
    'url': 'http://test.lengow.io/orders-test.xml',
}

def index(request):
    context['status'] = ''
    if request.GET.get('url'):
        context['url'] = request.GET['url']
    if request.GET.get('status'):
        context['status'] = request.GET['status']
    context['orders'] = loadXML(context['url'])
    context['type'] = 'xml'
    return render(request, 'orders/index.html', context)


def orders(request):
    if request.GET.get('action') == 'delete':
        print('delete')
        if request.GET.get('idOrder') and isinstance(int(request.GET['idOrder']), int) and request.GET.get('idProduct') and isinstance(int(request.GET['idProduct']), int):
            try:
                Product.objects.get(id=request.GET['idProduct']).delete()
                return HttpResponseRedirect('/orders/')
            except:
                pass
        else:
            print('qsdsdqsdq')
            if request.GET.get('idOrder') and isinstance(int(request.GET['idOrder']), int):
                try:
                    Order.objects.get(id=request.GET['idOrder']).delete()
                    return HttpResponseRedirect('/orders/')
                except:
                    pass

    if request.GET.get('search'):
        context['search'] = request.GET['search']
        print(request.GET['search'])
        
        try:
            orders_marketplace = Order.objects.filter(marketplace=request.GET['search'])
        except Order.DoesNotExist:
            print('data')


        try:
            orders_lastname = Order.objects.filter(lastname=request.GET['search'])
        except Order.DoesNotExist:
            print('data')


        try:
            orders_city = Order.objects.filter(city=request.GET['search'])
        except Order.DoesNotExist:
            print('data')

        orders = list(chain(orders_marketplace, orders_lastname, orders_city))
        print(orders)

    else:
        context['search'] = ''
        orders = Order.objects.all()
    context['orders'] = orders
    if request.GET.get('status'):
        context['status'] = request.GET['status']

    context['type'] = 'order'
    return render(request, 'orders/orders.html', context)


def form(request):
    if request.method == 'GET':
        fuck = formGet(request, context)
        return render(request, 'orders/form.html', context)

    if request.method == 'POST':
        text = formPost(request)
        return HttpResponseRedirect(text)
