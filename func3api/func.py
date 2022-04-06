from django.shortcuts import *
from email import message
from tokenize import Name
from unicodedata import name
from func3api.filters import *
from django.conf import settings
from func3api.models import *
from linebot import LineBotApi
from linebot.models import DatetimePickerTemplateAction, LocationSendMessage, MessageAction, QuickReplyButton, QuickReply, StickerSendMessage, TextSendMessage, TemplateSendMessage, ConfirmTemplate, MessageTemplateAction, ButtonsTemplate, PostbackTemplateAction, URITemplateAction, CarouselTemplate, CarouselColumn, ImageCarouselTemplate, ImageCarouselColumn, ImageSendMessage, FlexSendMessage
import datetime
import requests
from bs4 import BeautifulSoup
from urllib.request import urlretrieve
line_bot_api = LineBotApi(settings.LINE_CHANNEL_ACCESS_TOKEN)



def ALL_data_inquire(event,data_text):
    datalist = data_text[3:]
    if All.objects.filter(name_all=datalist).exists():
        a1 = All.objects.get(name_all = datalist)
        print("結果"+str(a1.price))
        flex_message = FlexSendMessage(
            alt_text='搜尋結果',
            contents={
                "type": "bubble",
                        "hero": {
                            "type": "image",
                            "url": str(display_name.pc_images),
                            "size": "full",
                            "aspectRatio": "3:2",
                            "aspectMode": "cover",
                            "action": {
                                "type": "uri",
                                        "uri": str(display_name.url_list)
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
                                    "text": "價格:"+str(display_name.price),
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
                                    "text": str(display_name.commodity),
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
                                                "uri": str(display_name.url_list)
                                        }
                                    }
                            ]
                        }
            }
        )

        line_bot_api.reply_message(  # 回覆訊息
            event.reply_token, flex_message
        )

 
def manageForm(event, mtext ):

    flist = mtext[3:].split('#')
    
    if flist[0] == "請選擇CPU":
        CPU_name = "未選擇CPU"
        CPU_price = 0
        CPU_url = "https://24h.pchome.com.tw/"

    elif cpu.objects.filter(name=flist[0]).exists():  # CPU
        cpu_name = cpu.objects.get(name=flist[0])

        cpu_vendor = cpu_name.vendor
        CPU_name = cpu_name.name
        CPU_price = cpu_name.price
        CPU_images = cpu_name.pc_images
        CPU_url = cpu_name.url_list

        save_cpu = db.objects.create(
            vendor=cpu_vendor, name=CPU_name, price=CPU_price,
            pc_images=CPU_images, url_list=CPU_url,)  # 新增資料
        save_cpu.save() #儲存資料

    else:
        CPU_name = "資料錯誤"
        CPU_price = 0
        CPU_url = "https://24h.pchome.com.tw/"
        

    if flist[1] == "請選擇主機板":
        MB_NAME = "未選擇主機板"
        MB_price = 0
        MB_url = "https://24h.pchome.com.tw/"
    elif MB.objects.filter(name=flist[1]).exists():  # 主機板
        MB_name = MB.objects.get(name=flist[1])
        MB_vendor = MB_name.vendor
        MB_NAME = MB_name.name
        MB_price = MB_name.price
        MB_images = MB_name.pc_images
        MB_url = MB_name.url_list

        save_mb = db.objects.create(
            vendor=MB_vendor, name=MB_NAME, price=MB_price,
            pc_images=MB_images, url_list=MB_url, )  # 新增資料

        save_mb.save()  # 儲存資料
    else:
        MB_NAME = "資料錯誤"
        MB_price = 0
        MB_url = "https://24h.pchome.com.tw/"



    if flist[2] == "請選擇固態硬碟":
        SSD_name = "未選擇固態硬碟"
        SSD_price = 0
        SSD_url = "https://24h.pchome.com.tw/"
    elif ssd.objects.filter(name=flist[2]).exists():  # SSD
        ssd_name = ssd.objects.get(name=flist[2])
        SSD_vendor = ssd_name.vendor
        SSD_name = ssd_name.name
        SSD_images = ssd_name.pc_images
        SSD_price = ssd_name.price
        SSD_url = ssd_name.url_list

        save_SSD = db.objects.create(
            vendor=SSD_vendor, name=SSD_name, price=SSD_price,
            pc_images=SSD_images, url_list=SSD_url, )  # 新增資料

        save_SSD.save()  # 儲存資料
    else:
        SSD_name = "資料錯誤"
        SSD_price = 0
        SSD_url = "https://24h.pchome.com.tw/"

    if flist[3] == "請選擇傳統硬碟":
        HDD_name = "未選擇傳統硬碟"
        HDD_price = 0
        HDD_url = "https://24h.pchome.com.tw/"

    elif hdd.objects.filter(name=flist[3]).exists():  # HDD
        hdd_name = hdd.objects.get(name=flist[3])
        HDD_vendor = hdd_name.vendor
        HDD_name = hdd_name.name
        HDD_price = hdd_name.price
        HDD_images = hdd_name.pc_images
        HDD_url = hdd_name.url_list

        save_HDD = db.objects.create(
            vendor=HDD_vendor, name=HDD_name, price=HDD_price,
            pc_images=HDD_images, url_list=HDD_url, )  # 新增資料

        save_HDD.save()  # 儲存資料

    else:
        HDD_name = "資料錯誤"
        HDD_price = 0
        HDD_url = "https://24h.pchome.com.tw/"

    if flist[4] == "請選擇顯示卡":
        Display_name = "未選擇顯示卡"
        Display_price = 0
        Display_url = "https://24h.pchome.com.tw/"

    elif display.objects.filter(name=flist[4]).exists():  # 顯示卡
        display_name = display.objects.get(name=flist[4])
        Display_vendor = display_name.vendor
        Display_name = display_name.name
        Display_price = display_name.price
        Display_images = display_name.pc_images
        Display_url = display_name.url_list

        save_Display = db.objects.create(
            vendor=Display_vendor, name=Display_name, price=Display_price,
            pc_images=Display_images, url_list=Display_url, )  # 新增資料

        save_Display.save()  # 儲存資料
    else:
        Display_name = "資料錯誤"
        Display_price = 0
        Display_url = "https://24h.pchome.com.tw/"

    if flist[5] == "請選擇記憶體":
        MEMORY_name = "未選擇記憶體"
        MEMORY_price = 0
        MEMORY_url = "https://24h.pchome.com.tw/"

    elif Memory.objects.filter(name=flist[5]).exists():  # 記憶體
        Memory_name = Memory.objects.get(name=flist[5])
        MEMORY_name = Memory_name.name
        MEMORY_price = Memory_name.price
        MEMORY_url = Memory_name.url_list
        MEMORY_vendor = Memory_name.vendor
        MEMORY_images = Memory_name.pc_images


        save_Memory = db.objects.create(
            vendor=MEMORY_vendor, name=MEMORY_name, price=MEMORY_price,
            pc_images=MEMORY_images, url_list=MEMORY_url, )  # 新增資料

        save_Memory.save()  # 儲存資料
    else:
        MEMORY_name = "資料錯誤"
        MEMORY_price = 0
        MEMORY_url = "https://24h.pchome.com.tw/"

    if flist[6] == "請選擇電源供應器":
        POWER_name = "未選擇電源供應器"
        POWER_price = 0
        POWER_url = "https://24h.pchome.com.tw/"
    elif Power.objects.filter(name=flist[6]).exists():  # 電源供應器
        Power_name = Power.objects.get(name=flist[6])
        POWER_name = Power_name.name
        POWER_price = Power_name.price
        POWER_url = Power_name.url_list
        POWER_vendor = Power_name.vendor
        POWER_images = Power_name.pc_images

        save_POWER = db.objects.create(
            vendor=POWER_vendor, name=POWER_name, price=POWER_price,
            pc_images=POWER_images, url_list=POWER_url, )  # 新增資料

        save_POWER.save()  # 儲存資料
    else:
        POWER_name = "資料錯誤"
        POWER_price = 0
        POWER_url = "https://24h.pchome.com.tw/"

    if flist[7] == "請選擇機殼":
        CASE_name = "未選擇機殼"
        CASE_price = 0
        CASE_url = "https://24h.pchome.com.tw/"
    elif chassis.objects.filter(name=flist[7]).exists():  # 機殼
        chassis_name = chassis.objects.get(name=flist[7])
        CASE_name = chassis_name.name
        CASE_price = chassis_name.price
        CASE_url = chassis_name.url_list
        CASE_vendor = chassis_name.vendor
        CASE_images = chassis_name.pc_images

        save_CASE = db.objects.create(
            vendor=CASE_vendor, name=CASE_name, price=CASE_price,
            pc_images=CASE_images, url_list=CASE_url, )  # 新增資料

        save_CASE.save()  # 儲存資料
    else:
        CASE_name = "資料錯誤"
        CASE_price = 0
        CASE_url = "https://24h.pchome.com.tw/"

    for i in range(8):
        print(flist[i])
        
    total_price = int(CPU_price)+int(MB_price)+int(SSD_price)+int(HDD_price)+int(Display_price)+int(MEMORY_price)+int(POWER_price)+int(CASE_price)
    print(total_price)
    save_total = total_db.objects.create(name = "total1",total=total_price)  # 新增資料

    save_total.save()  # 儲存資料

    flex_message = FlexSendMessage(
        alt_text='搜尋結果',
        contents={
            "type": "bubble",
            "body": {
                "type": "box",
                "layout": "vertical",
                "contents": [
                    {
                        "type": "text",
                        "text": "配置清單",
                        "weight": "bold",
                        "size": "xxl",
                        "margin": "none",
                        "color": "#1DB446"
                    },
                    {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                            {
                                "type": "text",
                                "text": "CPU",
                                "size": "xl",
                                "weight": "bold"
                            },
                            {
                                "type": "separator",
                                "color": "#000000"
                            },
                            {
                                "type": "text",
                                "text": str(CPU_name),
                                "margin": "sm",
                                "wrap": True
                            },
                            {
                                "type": "box",
                                "layout": "vertical",
                                "contents": [
                                    {
                                        "type": "text",
                                        "text": "價格$"+str(CPU_price),
                                        "align": "end"
                                    }
                                ]
                            }
                        ],
                        "margin": "sm",
                        

                    },
                    {
                                        "type": "box",
                                        "layout": "vertical",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": "主機板",
                                                "size": "xl",
                                                "weight": "bold"
                                            },
                                            {
                                                "type": "separator",
                                                "color": "#000000"
                                            },
                                            {
                                                "type": "text",
                                                "text": str(MB_NAME),
                                                "margin": "sm",
                                                "wrap": True
                                            },
                                            {
                                                "type": "box",
                                                "layout": "vertical",
                                                "contents": [
                                                    {
                                                        "type": "text",
                                                        "text": "價格$"+str(MB_price),
                                                        "align": "end"
                                                    }
                                                ]
                                            }
                                        ],
                                        "margin": "sm",
                                        "backgroundColor": "#EEE9E9",
                                        
                                    },
                                    {
                                        "type": "box",
                                        "layout": "vertical",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": "固態硬碟SSD",
                                                "size": "xl",
                                                "weight": "bold"
                                            },
                                            {
                                                "type": "separator",
                                                "color": "#000000"
                                            },
                                            {
                                                "type": "text",
                                                "text": str(SSD_name),
                                                "margin": "sm",
                                                "wrap": True
                                            },
                                            {
                                                "type": "box",
                                                "layout": "vertical",
                                                "contents": [
                                                    {
                                                        "type": "text",
                                                        "text": "價格$"+str(SSD_price),
                                                        "align": "end"
                                                    }
                                                ]
                                            }
                                        ],
                                        "margin": "sm",
                                        
                                    },
                                    {
                                        "type": "box",
                                        "layout": "vertical",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": "傳統硬碟HDD",
                                                "size": "xl",
                                                "weight": "bold"
                                            },
                                            {
                                                "type": "separator",
                                                "color": "#000000"
                                            },
                                            {
                                                "type": "text",
                                                "text": str(HDD_name),
                                                "margin": "sm",
                                                "wrap": True
                                            },
                                            {
                                                "type": "box",
                                                "layout": "vertical",
                                                "contents": [
                                                    {
                                                        "type": "text",
                                                        "text": "價格$"+str(HDD_price),
                                                        "align": "end"
                                                    }
                                                ]
                                            }
                                        ],
                                        "margin": "sm",
                                        "backgroundColor": "#EEE9E9",
                                        
                                    },
                                    {
                                        "type": "box",
                                        "layout": "vertical",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": "顯示卡",
                                                "size": "xl",
                                                "weight": "bold"
                                            },
                                            {
                                                "type": "separator",
                                                "color": "#000000"
                                            },
                                            {
                                                "type": "text",
                                                "text": str(Display_name),
                                                "margin": "sm",
                                                "wrap": True
                                            },
                                            {
                                                "type": "box",
                                                "layout": "vertical",
                                                "contents": [
                                                    {
                                                        "type": "text",
                                                        "text": "價格$"+str(Display_price),
                                                        "align": "end"
                                                    }
                                                ]
                                            }
                                        ],
                                        "margin": "sm",
                                        
                                    },
                                    {
                                        "type": "box",
                                        "layout": "vertical",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": "記憶體",
                                                "size": "xl",
                                                "weight": "bold"
                                            },
                                            {
                                                "type": "separator",
                                                "color": "#000000"
                                            },
                                            {
                                                "type": "text",
                                                "text": str(MEMORY_name),
                                                "margin": "sm",
                                                "wrap": True
                                            },
                                            {
                                                "type": "box",
                                                "layout": "vertical",
                                                "contents": [
                                                    {
                                                        "type": "text",
                                                        "text": "價格$"+str(MEMORY_price),
                                                        "align": "end"
                                                    }
                                                ]
                                            }
                                        ],
                                        "margin": "sm",
                                        "backgroundColor": "#EEE9E9",
                                        
                                    },
                                    {
                                        "type": "box",
                                        "layout": "vertical",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": "電源供應器",
                                                "size": "xl",
                                                "weight": "bold"
                                            },
                                            {
                                                "type": "separator",
                                                "color": "#000000"
                                            },
                                            {
                                                "type": "text",
                                                "text": str(POWER_name),
                                                "margin": "sm",
                                                "wrap": True
                                            },
                                            {
                                                "type": "box",
                                                "layout": "vertical",
                                                "contents": [
                                                    {
                                                        "type": "text",
                                                        "text": "價格$"+str(POWER_price),
                                                        "align": "end"
                                                    }
                                                ]
                                            }
                                        ],
                                        "margin": "sm",
                                        
                                    },
                                    {
                                        "type": "box",
                                        "layout": "vertical",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": "機殼",
                                                "size": "xl",
                                                "weight": "bold"
                                            },
                                            {
                                                "type": "separator",
                                                "color": "#000000"
                                            },
                                            {
                                                "type": "text",
                                                "text": str(CASE_name),
                                                "margin": "sm",
                                                "wrap": True
                                            },
                                            {
                                                "type": "box",
                                                "layout": "vertical",
                                                "contents": [
                                                    {
                                                        "type": "text",
                                                        "text": "價格$"+str(CASE_price),
                                                        "align": "end"
                                                    }
                                                ]
                                            }
                                        ],
                                        "margin": "sm",
                                        "backgroundColor": "#EEE9E9",
                                        
                                    },
                    {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                            {
                                "type": "separator",
                                "color": "#000000"
                            },
                            {
                                "type": "text",
                                "text": "總計$"+str(total_price),
                                "margin": "md",
                                "align": "end",
                                "weight": "bold",
                                "size": "lg"
                            },
                            {
                                "type": "button",
                                "action": {
                                    "type": "uri",
                                    "label": "購買連結",
                                    "uri": "http://127.0.0.1:8000/test/"
                                },
                                "style": "primary",
                                "height": "sm",
                                "margin": "md"
                            }
                        ]
                    }

                ]
            },
            "styles": {
                "footer": {
                    "separator": True
                }
            }
        }
    )

    line_bot_api.reply_message(  # 回覆訊息
        event.reply_token, flex_message
    )
    

    
    
    #line_bot_api.reply_message(
    #    event.reply_token, TextSendMessage(text=CPU_name+'\n'+str(CPU_price)+'\n'+str(MB_price)+'\n'+ "總價為:"+str(total)))
        

   

def sendPosition(event):  # 傳送位置
    try:
        message = LocationSendMessage(
            title='崑山科技大學 Kun Shan University',
            address='710台南市永康區崑大路195號',
            latitude=22.99792647872198,  # 緯度
            longitude=120.25310442615711  # 經度
        )
        line_bot_api.reply_message(event.reply_token, message)
    except:
        line_bot_api.reply_message(
            event.reply_token, TextSendMessage(text='發生錯誤！'))


