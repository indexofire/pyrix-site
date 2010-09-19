# -*- coding: utf-8 -*-
from django import forms
from django.conf import settings
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse
from userfeed.models import Feed, Subscription, Action

class SubscriptionForm(forms.ModelForm):
    """
    Subscription Form Class
    """
    actions = forms.ModelMultipleChoiceField(queryset=None, widget=forms.CheckboxSelectMultiple(), required=False)
    
    def __init__(self, *args, **kwargs):
        self.feed = kwargs.pop('feed', None)
        
        super(SubscriptionForm, self).__init__(*args, **kwargs)
        
        # hide the fields we don't need and get the right actions
        self.fields['feed'].widget = forms.HiddenInput()
        self.fields['user'].widget = forms.HiddenInput()
        self.fields['actions'].queryset = Action.objects.filter(content_type=self.feed.content_type)

    class Meta:
        model = Subscription
        fields = ('user', 'feed', 'actions')
