# coding: utf-8
from urllib.request import urlopen
import xml.etree.ElementTree as ET

def loadXML(url): 
    tree = ET.parse(urlopen(url))
    root = tree.getroot()

    orders = [] 
    for XMLorder in root.findall('./orders/order'):
        order = {}
        order['marketplace'] = XMLorder.find('marketplace').text
        order['lastname'] = XMLorder.find('billing_address/billing_lastname').text
        order['city'] = XMLorder.find('billing_address/billing_city').text
        
        products = []
        for XMLproduct in XMLorder.findall('./cart/products/product'): 
            product = {}
            product['title'] = XMLproduct.find('title').text
            product['price'] = XMLproduct.find('price').text
            products.append(product)

        order['products'] = products
        orders.append(order)

    print(orders)
    return orders