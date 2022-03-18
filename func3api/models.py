from turtle import mode
from unicodedata import category, name
from django.db import models


class display(models.Model):  # 設計LINE Bot所需要使用的資料表(Table)欄位
    vendor = models.CharField(max_length=100, default="")  # 名稱
    name = models.CharField(max_length=100, default="")  # 名稱
    price = models.IntegerField(default="")  # 價格
    commodity = models.CharField(max_length=3000, default="")  # 詳細資訊
    url_list = models.CharField(max_length=3000, default="")  # 商品連結
    pc_images = models.CharField(max_length=3000, default="")  # 圖片網址
    display_chip = models.CharField(max_length=100, default="")  # 顯示晶片
    Memory = models.CharField(max_length=100, default="")  # 記憶體


class cpu (models.Model):  # 設計LINE Bot所需要使用的資料表(Table)欄位
    vendor = models.CharField(max_length=100, default="")  # 名稱
    name = models.CharField(max_length=100, default="")  # 名稱
    price = models.IntegerField(default="")  # 價格
    commodity = models.CharField(max_length=3000, default="")
    url_list = models.CharField(max_length=3000, default="")  # 商品連結
    pc_images = models.CharField(max_length=3000, default="")  # 圖片網址
    chip = models.CharField(max_length=100, default="")  # 核心
    thread = models.CharField(max_length=100, default="")  # 執行緒
    speed = models.CharField(max_length=100, default="")  # 時脈速度
    foot_position_cpu = models.CharField(max_length=100, default="")  # 腳位

class ssd(models.Model):  # 設計LINE Bot所需要使用的資料表(Table)欄位
    vendor = models.CharField(max_length=100, default="")  # 名稱
    name = models.CharField(max_length=100, default="")  # 名稱
    price = models.IntegerField(default="")  # 價格
    commodity = models.CharField(max_length=3000, default="")
    url_list = models.CharField(max_length=3000, default="")  # 商品連結
    pc_images = models.CharField(max_length=3000, default="")  # 圖片網址
    capacity_TB = models.FloatField(max_length=100, default="0.0")  # 容量
    size = models.CharField(max_length=100, default="")  # 尺寸
    read_speed_mbs = models.IntegerField(default="")  # 讀取
    write_speed_mbs = models.IntegerField(default="")  # 寫入


class All(models.Model):  # 設計LINE Bot所需要使用的資料表(Table)欄位
    
    vendor = models.CharField(max_length=100, default="")  # 名稱
    name_all = models.CharField(max_length=100, default="")  # 名稱
    price = models.IntegerField(default="")  # 價格
    commodity = models.CharField(max_length=3000, default="")
    url_list = models.CharField(max_length=3000, default="")  # 商品連結
    pc_images = models.CharField(max_length=3000, default="")  # 圖片網址


class chassis(models.Model):  # 設計LINE Bot所需要使用的資料表(Table)欄位
    vendor = models.CharField(max_length=100, default="")  # 名稱
    name = models.CharField(max_length=100, default="")  # 名稱
    price = models.IntegerField(default="")  # 價格
    commodity = models.CharField(max_length=3000, default="")
    url_list = models.CharField(max_length=3000, default="")  # 商品連結
    pc_images = models.CharField(max_length=3000, default="")  # 圖片網址


class hdd(models.Model):  # 設計LINE Bot所需要使用的資料表(Table)欄位
    vendor = models.CharField(max_length=100, default="")  # 名稱
    name = models.CharField(max_length=100, default="")  # 名稱
    price = models.IntegerField(default="")  # 價格
    commodity = models.CharField(max_length=3000, default="")
    url_list = models.CharField(max_length=3000, default="")  # 商品連結
    pc_images = models.CharField(max_length=3000, default="")  # 圖片網址
    capacity_TB = models.FloatField(max_length=100, default="0.0")  # 容量
    size = models.CharField(max_length=100, default="")  # 尺寸
    Rotating_speed = models.CharField(max_length=100, default="")  # 轉速


class MB(models.Model):  # 設計LINE Bot所需要使用的資料表(Table)欄位
    vendor = models.CharField(max_length=100, default="")  # 名稱
    name = models.CharField(max_length=100, default="")  # 名稱
    price = models.IntegerField(default="")  # 價格
    commodity = models.CharField(max_length=3000, default="")
    url_list = models.CharField(max_length=3000, default="")  # 商品連結
    pc_images = models.CharField(max_length=3000, default="")  # 圖片網址
    foot_position_MB = models.CharField(max_length=100, default="")  # 名稱


class Memory(models.Model):  # 設計LINE Bot所需要使用的資料表(Table)欄位
    vendor = models.CharField(max_length=100, default="")  # 名稱
    name = models.CharField(max_length=100, default="")  # 名稱
    price = models.IntegerField(default="")  # 價格
    commodity = models.CharField(max_length=3000, default="")
    url_list = models.CharField(max_length=3000, default="")  # 商品連結
    pc_images = models.CharField(max_length=3000, default="")  # 圖片網址
    Memory_Specifications = models.CharField(max_length=100, default="")  # 記憶體類別
    capacity_GB = models.IntegerField(default="")  # 容量
    type = models.CharField(max_length=100, default="")  # 類型
    clock_rate = models.IntegerField(default="")  # 頻率


class Power(models.Model):  # 設計LINE Bot所需要使用的資料表(Table)欄位
    vendor = models.CharField(max_length=100, default="")  # 名稱
    name = models.CharField(max_length=100, default="")  # 名稱
    price = models.IntegerField(default="")  # 價格
    commodity = models.CharField(max_length=3000, default="")
    url_list = models.CharField(max_length=3000, default="")  # 商品連結
    pc_images = models.CharField(max_length=3000, default="")  # 圖片網址
    Watts = models.CharField(max_length=100, default="")  # 名稱


# Create your models here.
class Category (models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Product (models.Model):

    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    sku = models.CharField(max_length=20)
    name = models.CharField(max_length=200)
    description = models.TextField()
    image = models.URLField(null=True)
    website = models.URLField(null=True)
    stock = models.PositiveIntegerField(default=0)
    price = models.DecimalField(max_digits=10,decimal_places=2,default=0)
