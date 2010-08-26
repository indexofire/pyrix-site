# -*- coding: utf-8 -*-
from django.contrib import admin

from userprofile.models import *


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'city')
admin.site.register(UserProfile, UserProfileAdmin)


class ServiceAdmin(admin.ModelAdmin):
    list_display = ('profile', 'service')
    list_filter = ('profile', 'service')
admin.site.register(Service, ServiceAdmin)


admin.site.register(MobileProvider)
admin.site.register(ServiceType)
admin.site.register(Link)
