from operator import length_hint
from typing import Text
from django.core.paginator import *
from urllib.request import Request
from django.template.loader import *
from django.contrib import messages
from django.shortcuts import *
from django.conf import settings
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseForbidden
from django.views.decorators.csrf import csrf_exempt
from numpy import product
from func3api.models import *
import subprocess
from linebot import LineBotApi, WebhookParser
from linebot.exceptions import InvalidSignatureError, LineBotApiError
from linebot.models import *
from urllib.parse import parse_qsl
import web_crawler
from .filters import *
from func3api import func

line_bot_api = LineBotApi(settings.LINE_CHANNEL_ACCESS_TOKEN)
parser = WebhookParser(settings.LINE_CHANNEL_SECRET)
HEROKU_APP_URL = ' https://topiclinebot.herokuapp.com/'
"""


    
def listone(request):
    unit = display.objects.get(id=8)
    return render(request,'listone.html',locals())




def ssd1(request):
    ssd_all = ssd.objects.all()
    return render(request, 'ssd.html', locals())

"""


@csrf_exempt



def listall(request):
    test1 = db.objects.all()
    
    if total_db.objects.filter(name="total1").exists():
        total = total_db.objects.filter(name="total1").first()
    else:
        total = total_db.objects.get(name="total")
    
    if request.method=="POST":
    
        result = request.POST['button']
        print(result)
        if result == 'Yes' and total_db.objects.filter(name="total1").exists():
            Delete_all = db.objects.all()
            Delete_all.delete()
            Delete_total = total_db.objects.filter(name="total1")
            Delete_total.delete()
        else:
            pass

    return render(request, 'test.html', locals())

def liff(request):
    cpus = cpu.objects.get(id=8)
    return render(request, 'index_form.html', locals())

def cpu1(request):
    cpus = cpu.objects.all().order_by('-price')
    all_data = All.objects.all()
    
    aFilter = cpuFilter(queryset=cpus)
    Filter_all = allFilter(queryset=all_data)
    if request.method == "POST":
            aFilter = cpuFilter(request.POST, queryset=cpus) #queryset查詢集
            Filter_all = allFilter(request.POST, queryset=all_data)
    context = {
        'aFilter': aFilter,
        'Filter_all': Filter_all
    }

    return render(request, 'cpu.html', context)




@csrf_exempt
def callback(request):
    if request.method == 'POST':
        #先設定一個要回傳的message空集合

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

                if msg[:3] == '###' and len(msg) > 3:
                    func.manageForm(event,msg)
              
                    
                
                if msg== '123':
                    Delete_all = db.objects.all()
                    Delete_all.delete()
                    
                
                if 'pc+' in msg:
                        keyword = msg.split('+')[1]
                        message = web_crawler.web_crawler(keyword)
                        line_bot_api.reply_message(event.reply_token, message)

                if event.message.text == "@傳送位置":
                    flex_message = FlexSendMessage(
                            alt_text='搜尋結果',
                            contents={
                                    "type": "bubble",
                                    "hero": {
                                        "type": "image",
                                        "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/01_1_cafe.png",
                                        "size": "full",
                                        "aspectRatio": "20:13",
                                        "aspectMode": "cover",
                                        "action": {
                                            "type": "uri",
                                            "uri": "http://linecorp.com/"
                                        }
                                    }
                            }
                        )
                    line_bot_api.reply_message(event.reply_token,flex_message)
                elif isinstance(event, MessageEvent):  # 如果有訊息事件
                    display_name = display.objects.filter(name=event.message.text)
                    
                    for displays in display_name:
                        flex_message = FlexSendMessage(
                            alt_text='搜尋結果',
                            contents={
                                "type": "bubble",
                                "hero": {
                                    "type": "image",
                                    "url": displays.pc_images,
                                    "size": "full",
                                    "aspectRatio": "3:2",
                                    "aspectMode": "cover",
                                    "action": {
                                        "type": "uri",
                                        "uri": displays.url_list
                                    }
                                },
                                "body": {
                                    "type": "box",
                                    "layout": "vertical",
                                    "spacing": "md",
                                    "action": {
                                        "type": "uri",
                                        "uri": "https://linecorp.com"
                                    },
                                    "contents": [
                                        {
                                            "type": "text",
                                            "text": "價格:"+str(displays.price),
                                            "size": "xxl",
                                            "weight": "bold"
                                        },
                                        {
                                            "type": "box",
                                            "layout": "vertical",
                                            "spacing": "sm",
                                            "contents": [
                                                {
                                                    "type": "box",
                                                    "layout": "baseline",
                                                    "contents": [
                                                        {
                                                            "type": "icon",
                                                            "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/restaurant_regular_32.png"
                                                        },
                                                        {
                                                            "type": "text",
                                                            "text": "詳細資訊",
                                                            "weight": "bold",
                                                            "margin": "sm",
                                                            "flex": 0,
                                                            "size": "lg"
                                                        }
                                                    ]
                                                }
                                            ]
                                        },
                                        {
                                            "type": "text",
                                            "text": displays.commodity,
                                            "wrap": True,
                                            "color": "#000000",
                                            "size": "xxs"
                                        }
                                    ]
                                },
                                "footer": {
                                    "type": "box",
                                    "layout": "vertical",
                                    "contents": [
                                        
                                        {
                                            "type": "button",
                                            "style": "primary",
                                            "color": "#905c44",
                                            "action": {
                                                "type": "uri",
                                                "label": "購買連結",
                                                "uri": displays.url_list
                                            }
                                        }
                                    ]
                                }
                            }
                        )
                    
                        line_bot_api.reply_message(  # 回覆訊息
                            event.reply_token,flex_message
                        )
    
        
        return HttpResponse()

    else:
        return HttpResponseBadRequest()

