from .xmlRead import loadXML
from .models import Order, Product


def formGet(request, context):
    context['marketplace'] = ''
    context['lastname'] = ''
    context['city'] = ''
    context['title'] = ''
    context['price'] = ''

    # Form for XML
    if request.GET.get('type') == 'xml':
        context['orders'] = loadXML(context['url'])
        if request.GET.get('idOrder') and isinstance(int(request.GET['idOrder']), int):
            idOrder = int(request.GET['idOrder'])
            context['marketplace'] = context['orders'][idOrder-1]['marketplace']
            context['lastname'] = context['orders'][idOrder-1]['lastname']
            context['city'] = context['orders'][idOrder-1]['city']

        if request.GET.get('idProduct') and isinstance(int(request.GET['idProduct']), int):
            idProduct = int(request.GET['idProduct'])
            context['title'] = context['orders'][idOrder-1]['products'][idProduct-1]['title']
            context['price'] = context['orders'][idOrder-1]['products'][idProduct-1]['price']

    # Form for Order     
    if request.GET.get('type') == 'order':
        if request.GET.get('idOrder') and isinstance(int(request.GET['idOrder']), int):
            idOrder = int(request.GET['idOrder'])
            order = Order.objects.get(id=idOrder)
            context['idOrder'] = order.id            
            context['marketplace'] = order.marketplace
            context['lastname'] = order.lastname
            context['city'] = order.city

        if request.GET.get('idProduct') and isinstance(int(request.GET['idProduct']), int):
            idProduct = int(request.GET['idProduct'])
            product = Product.objects.get(id=idProduct)
            context['idProduct'] = product.id
            context['title'] = product.title
            context['price'] = product.price

    if request.GET.get('type'):
        context['type'] = request.GET['type']
    if request.GET.get('action'):
        context['action'] = request.GET['action']
    return context


def formPost(request):
    if request.POST.get("marketplace", "") and request.POST.get("lastname", "") and request.POST.get("city", "") and request.POST.get("title", "") and request.POST.get("price", ""):
        
        if request.POST.get("action", "") == 'add':
        
            product = Product.objects.create(title=request.POST['title'], price=request.POST['price'])
            product.save()

            try:
                order = Order.objects.get(lastname=request.POST['lastname'])
                print('order exist')
                print(order.id)
                order.products.add(product)
                order.save()

            except Order.DoesNotExist:
                print('order not exist')
                order = Order.objects.create(marketplace=request.POST['marketplace'], lastname=request.POST['lastname'], city=request.POST['city'])
                order.products.add(product)
                order.save()

        if request.POST.get("action", "") == 'edit':
            if isinstance(int(request.POST['idProduct']), int):
                idProduct = int(request.POST['idProduct'])
                product = Product.objects.get(id=idProduct)
                product.title = request.POST['title']
                product.price = request.POST['price']
                product.save()

            if isinstance(int(request.POST['idOrder']), int):
                idOrder = int(request.POST['idOrder'])
                order = Order.objects.get(id=idOrder)
                order.marketplace = request.POST['marketplace']
                order.lastname = request.POST['lastname']
                order.city = request.POST['city']
                order.save()

        if request.POST['type'] == 'order':
            return "/orders/?status=success"
        else:
            return "/?status=success"

    else:
        if request.POST['type'] == 'order':
            return "/orders/?status=error"
        else:
            return "/?status=error"
