from django import forms
from django.conf import settings

from django_ace import AceWidget

from sodaseo.models import (
    Config, Template, Url, Var, Seo, get_default_template
)
from sodaseo.settings import SODA_SEO_LANGUAGES


class ConfigForm(forms.ModelForm):

    class Meta:
        model = Config
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
            'body': AceWidget(
                mode='django', width='640px', showprintmargin=False
            ),
        }
        exclude = ()


class UrlForm(forms.ModelForm):

    class Meta:
        model = Url
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
        exclude = ()


class SeoForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(SeoForm, self).__init__(*args, **kwargs)
        if 'language' in self.fields:
            self.fields['language'].required = True
            self.fields['language'].widget = forms.Select(
                choices=SODA_SEO_LANGUAGES
            )
            if not self.fields['language'].initial:
                self.fields['language'].initial = settings.LANGUAGE_CODE

    class Meta:
        model = Seo
        exclude = ()
