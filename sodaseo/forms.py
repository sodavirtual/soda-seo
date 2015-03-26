# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django import forms

from suit.widgets import (
    SuitSplitDateTimeWidget, LinkedSelect, AutosizedTextarea
)
from django_ace import AceWidget

from sodaseo.models import Config, Template, Url, Var, Seo


class ConfigForm(forms.ModelForm):

    class Meta:
        model = Config
        widgets = {
            'site_name': forms.TextInput(attrs={'class': 'input-xxlarge'}),
            'google_site_verification': forms.TextInput(
                attrs={'class': 'input-xxlarge'}
            ),
        }
        exclude = ()

    def clean_site(self):
        site = self.cleaned_data.get('site')

        if Config.objects.filter(site=site).exists():
            raise forms.ValidationError(
                'Já existe uma configuração para esse site.'
            )

        return site


class TemplateForm(forms.ModelForm):

    class Meta:
        model = Template
        widgets = {
            'name': forms.TextInput(attrs={'class': 'input-xxlarge'}),
            'slug': forms.TextInput(attrs={'class': 'input-xxlarge'}),
            'body': AceWidget(
                mode='django', width='640px', showprintmargin=False
            ),
        }
        exclude = ()


class UrlForm(forms.ModelForm):

    class Meta:
        model = Url
        widgets = {
            'path': forms.TextInput(attrs={'class': 'input-xxlarge'})
        }

        exclude = ()

    def clean_path(self):
        site = self.cleaned_data.get('site')
        path = self.cleaned_data.get('path')

        if Url.objects.filter(site=site, path=path).exists():
            raise forms.ValidationError('Url já cadastrada.')

        return path


class VarForm(forms.ModelForm):

    class Meta:
        model = Var
        widgets = {
            'description': AutosizedTextarea(
                attrs={'rows': 3, 'class': 'input-xxlarge'}
            ),
        }
        exclude = ()


class SeoForm(forms.ModelForm):

    class Meta:
        model = Seo
        widgets = {
            'template': LinkedSelect,
            'title': forms.TextInput(attrs={'class': 'input-xxlarge'}),
            'keywords': forms.TextInput(attrs={'class': 'input-xxlarge'}),
            'description': forms.TextInput(attrs={'class': 'input-xxlarge'}),
            'author': forms.TextInput(attrs={'class': 'input-xxlarge'}),
            'og_site_name': forms.TextInput(attrs={'class': 'input-xxlarge'}),
            'og_title': forms.TextInput(attrs={'class': 'input-xxlarge'}),
            'og_type': forms.TextInput(attrs={'class': 'input-xxlarge'}),
            'og_url': forms.TextInput(attrs={'class': 'input-xxlarge'}),
            'og_description': forms.TextInput(
                attrs={'class': 'input-xxlarge'}
            ),
            'article_published_time': SuitSplitDateTimeWidget,
            'article_modified_time': SuitSplitDateTimeWidget,
            'article_section': forms.TextInput(
                attrs={'class': 'input-xxlarge'}
            ),
            'article_tag': forms.TextInput(attrs={'class': 'input-xxlarge'}),
            'itemprop_name': forms.TextInput(attrs={'class': 'input-xxlarge'}),
            'itemprop_description': forms.TextInput(
                attrs={'class': 'input-xxlarge'}
            ),
            'itemprop_image': forms.TextInput(
                attrs={'class': 'input-xxlarge'}
            ),
            'twitter_card': forms.TextInput(attrs={'class': 'input-xxlarge'}),
            'twitter_site': forms.TextInput(attrs={'class': 'input-xxlarge'}),
            'twitter_title': forms.TextInput(attrs={'class': 'input-xxlarge'}),
            'twitter_description': forms.TextInput(
                attrs={'class': 'input-xxlarge'}
            ),
            'twitter_url': forms.TextInput(attrs={'class': 'input-xxlarge'}),
        }
        exclude = ()
