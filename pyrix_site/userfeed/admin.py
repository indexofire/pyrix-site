# -*- coding: utf-8 -*-
from django.contrib import admin
from userfeed.models import Feed, Subscription, Update, Action


admin.site.register(Feed)
admin.site.register(Subscription)
admin.site.register(Update)admin.site.register(Action)
