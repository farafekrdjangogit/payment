# -*- coding: utf-8 -*- Github.com/Rasooll
from django.http import HttpResponse
from django.shortcuts import redirect
from zeep import Client
from wallet.models import Order
from django.contrib.auth.models import User

client = Client('http://payment.farafekr.co/index.php/payment/wsdl')
MERCHANT = '28d773c437ac'
amount = 101  # Toman / Required
description = "توضیحات مربوط به تراکنش را در این قسمت وارد کنید"  # Required
CallbackURL = 'http://185.211.58.140:5000/verify/'

def send_request(request):
    order = Order.objects.create(user=request.user, basket_id = 1, ip='192.168.1.1', amount=amount)
    order_id = order.id
    au = client.service.request(MERCHANT, amount, CallbackURL, order_id, description)
    if len(au) >= 8:
        order.bankau = au
        print(order.save())
        return redirect('http://payment.farafekr.co/index.php/paymentgateway/?au=' + str(au))
    else:
        return HttpResponse('Error code: ' + str(au))

def verify(request):
    if 'order_id' in request.GET and 'au' in request.GET:
        result = client.service.verify(MERCHANT, request.GET['au'], amount)
        print(result)
        if int(result) == 1:
            return HttpResponse('Transaction success.\nRefID: ' + str(result))
        else:
            return HttpResponse('Transaction failed.\nStatus: ' + str(result))
    else:
        return HttpResponse('Input Error!')

