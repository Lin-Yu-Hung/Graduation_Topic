from django.contrib import admin
from func3api import models
from func3api.models import *
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User


class total_dbAdmin(admin.ModelAdmin):
    list_display = ('id','total')

class dbAdmin(admin.ModelAdmin):
    list_display = ('id','vendor', 'name', 'price', 'url_list',)


class displayAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'commodity',
                    'vendor','display_chip')
    list_filter = ('name', 'price')
    search_fields = ('name',)
    ordering = ('id',)


class cpuAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'commodity',
                    'vendor','speed')
    list_filter = ('name', 'price')
    search_fields = ('name',)
    ordering = ('id',)


class ssdAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'commodity',
                    'vendor','size')
    list_filter = ('name', 'price')
    search_fields = ('name',)
    ordering = ('id',)


class chassisAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'commodity',
                    'vendor')
    list_filter = ('name', 'price')
    search_fields = ('name',)
    ordering = ('id',)


class hddAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'commodity',
                    'vendor', 'Rotating_speed')
    list_filter = ('name', 'price')
    search_fields = ('name',)
    ordering = ('id',)


class MBAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'commodity',
                    'vendor')
    list_filter = ('name', 'price')
    search_fields = ('name',)
    ordering = ('id',)


class MemoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'commodity',
                    'vendor')
    list_filter = ('name', 'price')
    search_fields = ('name',)
    ordering = ('id',)


class PowerAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'commodity',
                    'vendor')
    list_filter = ('name', 'price')
    search_fields = ('name',)
    ordering = ('id',)


class AllAdmin(admin.ModelAdmin):
    list_display = ('id', 'name_all', 'price', 'commodity',
                    'vendor')
    list_filter = ('name_all', 'price')
    search_fields = ('name_all',)
    ordering = ('id',)





admin.site.register(display, displayAdmin)
admin.site.register(cpu, cpuAdmin)
admin.site.register(ssd, ssdAdmin)
admin.site.register(chassis, chassisAdmin)
admin.site.register(hdd, hddAdmin)
admin.site.register(MB, MBAdmin)
admin.site.register(Memory, MemoryAdmin)
admin.site.register(Power, PowerAdmin)
admin.site.register(All, AllAdmin)
admin.site.register(db, dbAdmin)
admin.site.register(total_db, total_dbAdmin)
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
