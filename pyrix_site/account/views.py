# -*- coding: utf-8 -*-
from django import forms
from django.conf import settings
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

#from forms import SignatureForm

class SignatureForm(forms.Form):
    # name =  forms.CharField(label = 'Name', max_length=50)
    email = forms.EmailField(label = 'Email Address', help_text = 'Required')
    content = forms.CharField(widget = forms.widgets.Textarea(attrs = {
        'rows' : 4,
        'style' : 'width:100%;',
        'cols' : 20
        }),
        label = 'Comments', help_text = 'Optional', required = False
    )
  
    def clean_content(self):
      data = self.clean_data['content']
      if "http://" in data:
          raise forms.ValidationError("Cannot have HTML/Links in the comment")

      return data

@login_required
def profile(request, user_id=None, template_name="account/profile.html"):
    user = get_object_or_404(User, pk=user_id)
    view_only = user != request.user
    context = {
        'view_user': user, 
        'view_only': view_only,
    }
    return render_to_response(template_name, context, RequestContext(request))

@login_required
def signature(request, form_class=SignatureForm, template_name="account/signature.html"):
    profile = request.user.lbforum_profile
    if request.method == "POST":
        form = form_class(instance=profile, data=request.POST)
        form.save()
    else:
        form = form_class(instance=profile)
    ext_ctx = {'form': form}
    return render_to_response(template_name, ext_ctx, RequestContext(request))

"""
def create(request, template_name='accounts/create.html',
    redirect_field_name='redirect_to'):

    user_form = None
    captcha_error = ""
    redirect_to = request.REQUEST.get(redirect_field_name, '')

    if request.method == "POST":
        captcha_response = captcha.submit(
            request.POST.get("recaptcha_challenge_field", None),
            request.POST.get("recaptcha_response_field", None),
            settings.RECAPTCHA_PRIVATE_KEY,
            request.META.get("REMOTE_ADDR", None))

        if not captcha_response.is_valid:
            captcha_error = "&error=%s" % captcha_response.error_code
        else:
            # perform other registration checks as needed...
            # success!
            return HttpResponseRedirect(redirect_to)

    if not user_form:
        user_form = UserForm(prefix="user")

    return render_to_response(template_name, {
        'captcha_error': captcha_error,
        'user_form': user_form},
        context_instance=RequestContext(request))
"""
