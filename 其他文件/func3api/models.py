import email
from turtle import mode
from unicodedata import category, name
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.timezone import now
from hitcount.models import HitCountMixin, HitCount
from django.contrib.contenttypes.fields import GenericRelation


class Post(models.Model, HitCountMixin):
    title = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=255, unique=True)
    published_on = models.DateTimeField(blank=True, default=None, null=True)
    content = models.TextField(blank=True)

    hit_count_generic = GenericRelation(
        HitCount, object_id_field='object_pk',
        related_query_name='hit_count_generic_relation'
    )

    def current_hit_count(self):
        return self.hit_count.hits

class UserProfile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, verbose_name='帳號名稱')
 
class total_db(models.Model):  # 設計LINE Bot所需要使用的資料表(Table)欄位
    name = models.CharField(max_length=100, default="")  # 名稱
    total = models.IntegerField(default="0")  # 價格

class db(models.Model):  # 設計LINE Bot所需要使用的資料表(Table)欄位
    vendor = models.CharField(max_length=100, default="")  # 名稱
    name = models.CharField(max_length=100, default="")  # 名稱
    price = models.IntegerField(default="")  # 價格
    pc_images = models.CharField(max_length=3000, default="")  # 圖片網址
    url_list = models.CharField(max_length=3000, default="")  # 商品連結



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

class cartdb(models.Model): 
    vendor = models.CharField(max_length=100, default="")  # 名稱
    name = models.CharField(max_length=100, default="")  # 名稱
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




