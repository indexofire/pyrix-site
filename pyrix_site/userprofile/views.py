# -*- coding: utf-8 -*-
from django import forms
from django.conf import settings
from django.db.models import get_model

from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import Http404, HttpResponseRedirect
from django.views.generic import list_detail
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import permission_required
from django.core.urlresolvers import reverse
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import SiteProfileNotAvailable
from userprofile.models import *
from userprofile.forms import *


def get_profile_model():
    """
    Return the model class for the currently-active user profile
    model, as defined by the ``AUTH_PROFILE_MODULE`` setting. If that
    setting is missing, raise
    ``django.contrib.auth.models.SiteProfileNotAvailable``.
    
    """
    if (not hasattr(settings, 'AUTH_PROFILE_MODULE')) or \
           (not settings.AUTH_PROFILE_MODULE):
        raise SiteProfileNotAvailable
    profile_mod = get_model(*settings.AUTH_PROFILE_MODULE.split('.'))
    if profile_mod is None:
        raise SiteProfileNotAvailable
    return profile_mod


def get_profile_form():
    """
    Return a form class (a subclass of the default ``ModelForm``)
    suitable for creating/editing instances of the site-specific user
    profile model, as defined by the ``AUTH_PROFILE_MODULE``
    setting. If that setting is missing, raise
    ``django.contrib.auth.models.SiteProfileNotAvailable``.
    
    """
    profile_mod = get_profile_model()
    class _ProfileForm(forms.ModelForm):
        class Meta:
            model = profile_mod
            exclude = ('user',) # User will be filled in by the view.
    return _ProfileForm


@login_required
def profile_list(request):
    return list_detail.object_list(
        request,
        template_name='userprofile/profile_list.html',
        queryset=UserProfile.objects.all(),
        paginate_by=20,
    )
profile_list.__doc__ = list_detail.object_list.__doc__


@login_required
def profile_detail(request, username, profile=None):
    try:
        user = User.objects.get(username__iexact=username)
    except User.DoesNotExist:
        raise Http404
    try:
        profile = UserProfile.objects.get(user=user)
    except UserProfile.DoesNotExist:
        return HttpResponseRedirect(reverse('profile_create'))
    context = { 
        'object': profile
    }
    return render_to_response('userprofile/profile_detail.html', context, context_instance=RequestContext(request))


@login_required
def profile_edit(request, template_name='userprofile/profile_form.html'):
    """Edit profile."""

    if request.POST:
        profile = UserProfile.objects.get(user=request.user)
        profile_form = UserProfileForm(request.POST, request.FILES, instance=profile)
        user_form = UserForm(request.POST, instance=request.user)
        service_formset = ServiceFormSet(request.POST, instance=profile)
        link_formset = LinkFormSet(request.POST, instance=profile)

        if profile_form.is_valid() and user_form.is_valid() and service_formset.is_valid() and link_formset.is_valid():
            profile_form.save()
            user_form.save()
            service_formset.save()
            link_formset.save()
            return HttpResponseRedirect(reverse('profile_detail', kwargs={'username': request.user.username}))
        else:
            context = {
                'profile_form': profile_form,
                'user_form': user_form,
                'service_formset': service_formset,
                'link_formset': link_formset
            }
    else:
        profile = UserProfile.objects.get(user=request.user)
        service_formset = ServiceFormSet(instance=profile)
        link_formset = LinkFormSet(instance=profile)
        context = {
            'profile_form': UserProfileForm(instance=profile),
            'user_form': UserForm(instance=request.user),
            'service_formset': service_formset,
            'link_formset': link_formset
        }
    return render_to_response(template_name, context, context_instance=RequestContext(request))

#@permission_required('profile.can_create')
def profile_create(request, form_class=None, success_url=None, template_name='userprofile/profile_create.html'):
    """Create a profile for the current user, if one doesn't already
    exist.
    
    If the user already has a profile, as determined by
    ``request.user.get_profile()``, a redirect will be issued to the
    :view:`profiles.views.edit_profile` view. If no profile model has
    been specified in the ``AUTH_PROFILE_MODULE`` setting,
    ``django.contrib.auth.models.SiteProfileNotAvailable`` will be
    raised.
    
    To specify the form class used for profile creation, pass it as
    the keyword argument ``form_class``; if this is not supplied, it
    will fall back to a ``ModelForm`` for the model specified in the
    ``AUTH_PROFILE_MODULE`` setting.
    
    If you are supplying your own form class, it must define a method
    named ``save()`` which corresponds to the signature of ``save()``
    on ``ModelForm``, because this view will call it with
    ``commit=False`` and then fill in the relationship to the user
    (which must be via a field on the profile model named ``user``, a
    requirement already imposed by ``User.get_profile()``) before
    finally saving the profile object. If many-to-many relations are
    involved, the convention established by ``ModelForm`` of
    looking for a ``save_m2m()`` method on the form is used, and so
    your form class should define this method.
    
    To specify a URL to redirect to after successful profile creation,
    pass it as the keyword argument ``success_url``; this will default
    to the URL of the :view:`profiles.views.profile_detail` view for
    the new profile if unspecified.
    
    To specify the template to use, pass it as the keyword argument
    ``template_name``; this will default to
    :template:`profiles/create_profile.html` if unspecified.
    
    Context:
    
    form
        The profile-creation form.
    
    Template:
    
    ``template_name`` keyword argument, or
    :template:`profiles/create_profile.html`.
    
    """
    try:
        profile_obj = request.user.get_profile()
        return HttpResponseRedirect(reverse('profile_edit'))
    except ObjectDoesNotExist:
        pass
    
    #
    # We set up success_url here, rather than as the default value for
    # the argument. Trying to do it as the argument's default would
    # mean evaluating the call to reverse() at the time this module is
    # first imported, which introduces a circular dependency: to
    # perform the reverse lookup we need access to profiles/urls.py,
    # but profiles/urls.py in turn imports this module.
    #
    
    if success_url is None:
        success_url = reverse('profile_detail', kwargs={'username': request.user.username})
    if form_class is None:
        form_class = get_profile_form()
    if request.method == 'POST':
        form = form_class(data=request.POST, files=request.FILES)
        if form.is_valid():
            profile_obj = form.save(commit=False)
            profile_obj.user = request.user
            profile_obj.save()
            if hasattr(form, 'save_m2m'):
                form.save_m2m()
            return HttpResponseRedirect(success_url)
    else:
        form = form_class()
    return render_to_response(template_name,{'form': form}, context_instance=RequestContext(request))
