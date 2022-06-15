
from cmath import isnan
from itertools import count
from operator import length_hint
from threading import local
from typing import Text
from urllib import request
from django.core.paginator import *
from urllib.request import Request
from django.template.loader import *
from django.contrib import messages as ms
from django.shortcuts import *
from django.conf import settings
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseForbidden
from django.views.decorators.csrf import csrf_exempt
from numpy import product
from prometheus_client import Counter
from requests import session
from func3api.models import *
from django.db.models import Sum
import subprocess
from linebot import LineBotApi, WebhookParser
from linebot.exceptions import InvalidSignatureError, LineBotApiError
from linebot.models import *
from urllib.parse import parse_qsl
import web_crawler
from .filters import *
from func3api import func
import datetime
from django.db import connection
import time


line_bot_api = LineBotApi(settings.LINE_CHANNEL_ACCESS_TOKEN)
parser = WebhookParser(settings.LINE_CHANNEL_SECRET)
# HEROKU_APP_URL = ' https://topiclinebot.herokuapp.com/'


@csrf_exempt
def gettime():
    import time
    return time.ctime()


def getCount():
    countfile = open('count.dat', 'a+')
    counttext = countfile.read()
    try:
        count = int(counttext)+1
    except:
        count = 1
    countfile.seek(0)
    countfile.truncate()
    countfile.write(str(count))
    countfile.flush()
    countfile.close()
    return count


def listone(request):
    cpu1 = cpu.objects.get(id=2)
    for item in cpu1.__dict__.items():
        print(item)
    print('\n'.join(['%s'for item in cpu1.__dict__.items()]))

    return render(request, 'test1.html', locals())


def CART(request):

    cart_all = cartdb.objects.all()
    total = cartdb.objects.aggregate(Sum('price'))

    if request.method == "POST":
        cart_result = request.POST.get('cart_del')
        defbutton = request.POST.get('button')

        if cart_result == 'NO' or "None":
            pass
        else:
            delcart = cartdb.objects.filter(name=cart_result).first()
            delcart.delete()

        print(defbutton)
        print(cart_result)
        if defbutton == 'Yes':
            delcart_all = cartdb.objects.all()
            delcart_all.delete()
        else:
            pass

    return render(request, "cart.html", locals())


def listall(request):
    test1 = db.objects.all()
    total = db.objects.aggregate(Sum('price'))

    if request.method == "POST":
        cart_result = request.POST.get('cart_del')
        result = request.POST.get('button')
        print(result)
        print(cart_result)
        if cart_result == 'NO' and result == 'None':
            pass
        elif db.objects.filter(name=cart_result).exists():
            dellinebot = db.objects.filter(name=cart_result).first()
            dellinebot.delete()

        if result == 'Yes':
            Delete_all = db.objects.all()
            Delete_all.delete()
        else:
            pass

    return render(request, 'test.html', locals())


def liff(request):
    cpus = cpu.objects.get(id=8)
    return render(request, 'index_form.html', locals())


def cpu1(request):
    cart_all = cartdb.objects.all()

    cpus = cpu.objects.all().order_by('-price')
    all_data = All.objects.all()
    if request.method == "POST":
        cart = request.POST.get('cart_name')
        print(cart)
        if cart == 'NO' or None:
            ms.success(request, "取消成功")

        elif All.objects.filter(name_all=cart).exists():

            cartname = All.objects.get(name_all=cart)
            CARTname = cartname.name_all
            CARTvendor = cartname.vendor
            CARTprice = cartname.price
            CARTcommodity = cartname.commodity
            CARTurl_list = cartname.url_list
            CARTpc_images = cartname.pc_images


            #localtime = time.localtime()
            #資料庫名稱.objects.create(account=account,type="Button_cpu",time = localtime )
            save_cartdb = cartdb.objects.create(
                vendor=CARTvendor, name=CARTname, price=CARTprice,
                commodity=CARTcommodity, url_list=CARTurl_list, pc_images=CARTpc_images,)  # 新增資料

            save_cartdb.save()  # 儲存資料

















            ms.success(request, "成功將"+cart+"加入購物車\n\n\n目前共有" +
                       str(len(cart_all))+"筆資料")

    aFilter = cpuFilter(queryset=cpus)
    Filter_all = allFilter(queryset=all_data)
    if request.method == "POST":
        aFilter = cpuFilter(request.POST, queryset=cpus)  # queryset查詢集
        Filter_all = allFilter(request.POST, queryset=all_data)

    if "counter" in request.COOKIES:
        counter = int(request.COOKIES["counter"])
        counter += 1
    else:
        counter = 1

    context = {
        'aFilter': aFilter,
        'Filter_all': Filter_all,
    }

    return render(request, 'cpu.html', context)


@csrf_exempt
def callback(request):
    if request.method == 'POST':
        # 先設定一個要回傳的message空集合

        signature = request.META['HTTP_X_LINE_SIGNATURE']
        body = request.body.decode('utf-8')

        try:
            events = parser.parse(body, signature)
            print(events)
        except InvalidSignatureError:
            return HttpResponseForbidden()
        except LineBotApiError:
            return HttpResponseBadRequest()

        for event in events:
            if isinstance(event, MessageEvent):  # 如果有訊息事件
                msg = event.message.text
            if msg[:3] == '###' and len(msg) > 3:  # 購物清單功能
                try:
                    func.manageForm(event, msg)
                except:
                    line_bot_api.reply_message(
                        event.reply_token, TextSendMessage(text='發生錯誤！'))
            if msg[:3] == '$$$' and len(msg) > 3:  # 商品查詢功能
                try:
                    func.select(event, msg)
                except:
                    line_bot_api.reply_message(
                        event.reply_token, TextSendMessage(text='發生錯誤！'))
# ==========================推薦功能============================================
            if event.message.text == "@推薦商品":  # 推薦商品功能
                func.sendQuickreply(event)
            if event.message.text == "推薦CPU":
                print("#")
            if event.message.text == "推薦GPU":
                print("#")
            if event.message.text == "推薦主機板":
                print("#")
            if event.message.text == "推薦電源供應器":
                print("#")
            if event.message.text == "推薦SSD":
                print("#")

        return HttpResponse()

    else:
        return HttpResponseBadRequest()
