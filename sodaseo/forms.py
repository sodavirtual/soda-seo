# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django import forms
from django.conf import settings

from suit.widgets import (
    SuitSplitDateTimeWidget, LinkedSelect, AutosizedTextarea
)
from django_ace import AceWidget

from sodaseo.models import (
    Config, Template, Url, Var, Seo, get_default_template
)
from sodaseo.settings import SODA_SEO_URLS, SODA_SEO_I18N


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

        if self.instance:
            search = Config.objects.exclude(pk=self.instance.pk).filter(
                site=site
            ).exists()
        else:
            search = Config.objects.filter(site=site).exists()
        if search:
            raise forms.ValidationError(
                'Já existe uma configuração para esse site.'
            )

        return site


class TemplateForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(TemplateForm, self).__init__(*args, **kwargs)
        if not self.instance.pk:
            self.initial['body'] = get_default_template()

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
            'path': forms.Select(choices=sorted(SODA_SEO_URLS)),
            'description': AutosizedTextarea(
                attrs={'rows': 3, 'class': 'input-xxlarge'}
            ),
        }

        exclude = ()

    def clean_path(self):
        site = self.cleaned_data.get('site')
        path = self.cleaned_data.get('path')

        if self.instance:
            search = Url.objects.exclude(pk=self.instance.pk).filter(
                site=site, path=path
            ).exists()
        else:
            search = Url.objects.filter(site=site, path=path).exists()

        if search:
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

    def __init__(self, *args, **kwargs):
        super(SeoForm, self).__init__(*args, **kwargs)
        if 'language' in self.fields:
            self.fields['language'].required = True
            self.fields['language'].widget = forms.Select(
                choices=settings.LANGUAGES
            )
            if not self.fields['language'].initial:
                self.fields['language'].initial = settings.LANGUAGE_CODE

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
            # 'og_type': forms.TextInput(attrs={'class': 'input-xxlarge'}),
            'og_url': forms.TextInput(attrs={'class': 'input-xxlarge'}),
            'og_description': forms.TextInput(
                attrs={'class': 'input-xxlarge'}
            ),
            'og_see_also': AutosizedTextarea(
                attrs={'rows': 3, 'class': 'input-xxlarge'}
            ),
            'og_video': forms.TextInput(attrs={'class': 'input-xxlarge'}),
            'og_audio': forms.TextInput(attrs={'class': 'input-xxlarge'}),
            'article_published_time': SuitSplitDateTimeWidget,
            'article_modified_time': SuitSplitDateTimeWidget,
            'article_section': forms.TextInput(
                attrs={'class': 'input-xxlarge'}
            ),
            'article_author': forms.TextInput(
                attrs={'class': 'input-xxlarge'}
            ),
            'article_publisher': forms.TextInput(
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
