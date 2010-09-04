# -*- coding: utf-8 -*-
from django import forms
from django.forms import ModelForm
from django.forms.models import inlineformset_factory
from django.contrib.auth.models import User
from userprofile.models import *


class UserProfileForm(ModelForm):
    class Meta:
        model = UserProfile


ServiceFormSet  = inlineformset_factory(UserProfile, Service)
LinkFormSet     = inlineformset_factory(UserProfile, Link)


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name')
