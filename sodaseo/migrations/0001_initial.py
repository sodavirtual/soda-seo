# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import filer.fields.image
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0001_initial'),
        ('contenttypes', '0001_initial'),
        ('filer', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Config',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Atualizado em')),
                ('site_name', models.CharField(max_length=255, verbose_name='site_name')),
                ('google_site_verification', models.CharField(max_length=255, verbose_name='google-site-verification', blank=True)),
                ('fb_appid', models.CharField(max_length=255, verbose_name='fb:app_id', blank=True)),
                ('site', models.ForeignKey(related_name='sodaseo_config', default=1, verbose_name='site', to='sites.Site')),
            ],
            options={
                'verbose_name': 'configura\xe7\xe3o',
                'verbose_name_plural': 'configura\xe7\xf5es',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Seo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Atualizado em')),
                ('title', models.CharField(max_length=255, verbose_name='title')),
                ('keywords', models.CharField(max_length=255, verbose_name='keywords', blank=True)),
                ('description', models.CharField(max_length=255, verbose_name='description', blank=True)),
                ('author', models.CharField(max_length=255, verbose_name='author', blank=True)),
                ('og_site_name', models.CharField(max_length=255, verbose_name='og:site_name', blank=True)),
                ('og_title', models.CharField(max_length=255, verbose_name='og:title', blank=True)),
                ('og_type', models.CharField(max_length=255, verbose_name='og:type', blank=True)),
                ('og_url', models.CharField(max_length=255, verbose_name='og:url', blank=True)),
                ('og_description', models.CharField(max_length=255, verbose_name='og:description', blank=True)),
                ('article_published_time', models.DateTimeField(null=True, verbose_name='article:published_time', blank=True)),
                ('article_modified_time', models.DateTimeField(null=True, verbose_name='article:modified_time', blank=True)),
                ('article_section', models.CharField(max_length=255, verbose_name='article:section', blank=True)),
                ('article_tag', models.CharField(max_length=255, verbose_name='article:tag', blank=True)),
                ('itemprop_name', models.CharField(max_length=255, verbose_name='itemprop=name', blank=True)),
                ('itemprop_description', models.CharField(max_length=255, verbose_name='itemprop=description', blank=True)),
                ('twitter_card', models.CharField(max_length=255, verbose_name='twitter:card', blank=True)),
                ('twitter_site', models.CharField(max_length=255, verbose_name='twitter:site', blank=True)),
                ('twitter_title', models.CharField(max_length=255, verbose_name='twitter:title', blank=True)),
                ('twitter_description', models.CharField(max_length=255, verbose_name='twitter:description', blank=True)),
                ('twitter_creator', models.CharField(max_length=255, verbose_name='twitter:creator', blank=True)),
                ('object_id', models.PositiveIntegerField()),
                ('content_type', models.ForeignKey(to='contenttypes.ContentType')),
                ('itemprop_image', filer.fields.image.FilerImageField(related_name='seo_itemprop_image', on_delete=django.db.models.deletion.SET_NULL, verbose_name='itemprop=image', blank=True, to='filer.Image', null=True)),
                ('og_image', filer.fields.image.FilerImageField(related_name='seo_og_image', on_delete=django.db.models.deletion.SET_NULL, verbose_name='og:image', blank=True, to='filer.Image', null=True)),
            ],
            options={
                'verbose_name': 'entrada seo',
                'verbose_name_plural': 'entradas seo',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Template',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Atualizado em')),
                ('name', models.CharField(max_length=255, verbose_name='nome')),
                ('slug', models.SlugField(unique=True, max_length=255, verbose_name='identificador')),
                ('body', models.TextField(verbose_name='conte\xfado')),
            ],
            options={
                'ordering': ['name'],
                'verbose_name': 'template',
                'verbose_name_plural': 'templates',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Url',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Atualizado em')),
                ('path', models.CharField(max_length=255, verbose_name='caminho')),
                ('site', models.ForeignKey(related_name='sodaseo_urls', default=1, verbose_name='site', to='sites.Site')),
            ],
            options={
                'ordering': ['path'],
                'verbose_name': 'url',
                'verbose_name_plural': 'urls',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Var',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Atualizado em')),
                ('name', models.CharField(max_length=255, verbose_name='nome')),
                ('description', models.TextField(verbose_name='descri\xe7\xe3o')),
                ('url', models.ForeignKey(related_name='vars', verbose_name='url', to='sodaseo.Url')),
            ],
            options={
                'ordering': ['name'],
                'verbose_name': 'vari\xe1vel',
                'verbose_name_plural': 'vari\xe1veis',
            },
            bases=(models.Model,),
        ),
        migrations.AlterUniqueTogether(
            name='url',
            unique_together=set([('site', 'path')]),
        ),
        migrations.AddField(
            model_name='seo',
            name='template',
            field=models.ForeignKey(verbose_name='template', to='sodaseo.Template'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='seo',
            name='twitter_image',
            field=filer.fields.image.FilerImageField(related_name='seo_twitter_image', on_delete=django.db.models.deletion.SET_NULL, verbose_name='twitter:image', blank=True, to='filer.Image', null=True),
            preserve_default=True,
        ),
    ]
