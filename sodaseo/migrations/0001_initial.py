from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('sites', '0002_alter_domain_unique'),
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Config',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Atualizado em')),
                ('site_name', models.CharField(max_length=255, verbose_name='site_name')),
                ('google_site_verification', models.CharField(blank=True, max_length=255, verbose_name='google-site-verification')),
                ('google_analytics_id', models.CharField(blank=True, max_length=255, verbose_name='google-analytics-id')),
                ('fb_appid', models.CharField(blank=True, max_length=255, verbose_name='fb:app_id')),
                ('fb_profile_id', models.CharField(blank=True, max_length=255, verbose_name='fb:profile_id')),
                ('extra_head', models.TextField(blank=True, verbose_name='extra head')),
                ('extra_body', models.TextField(blank=True, verbose_name='extra body')),
                ('site', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='sodaseo_config', to='sites.Site', verbose_name='site')),
            ],
            options={
                'verbose_name': 'configuração',
                'verbose_name_plural': 'configurações',
            },
        ),
        migrations.CreateModel(
            name='Seo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Atualizado em')),
                ('language', models.CharField(blank=True, db_index=True, max_length=10, verbose_name='Idioma')),
                ('title', models.CharField(max_length=255, verbose_name='title')),
                ('keywords', models.CharField(blank=True, max_length=255, verbose_name='keywords')),
                ('description', models.CharField(max_length=255, verbose_name='description')),
                ('author', models.CharField(blank=True, max_length=255, verbose_name='author')),
                ('image', models.ImageField(blank=True, max_length=255, upload_to='sodaseo_images/', verbose_name='image')),
                ('og_site_name', models.CharField(blank=True, max_length=255, verbose_name='og:site_name')),
                ('og_title', models.CharField(blank=True, max_length=255, verbose_name='og:title')),
                ('og_type', models.CharField(blank=True, choices=[('website', 'website'), ('article', 'article')], max_length=255, verbose_name='og:type')),
                ('og_image', models.ImageField(blank=True, max_length=255, upload_to='sodaseo_images/', verbose_name='og:image')),
                ('og_video', models.URLField(blank=True, max_length=255, verbose_name='og:video')),
                ('og_audio', models.URLField(blank=True, max_length=255, verbose_name='og:audio')),
                ('og_url', models.CharField(blank=True, max_length=255, verbose_name='og:url')),
                ('og_description', models.CharField(blank=True, max_length=255, verbose_name='og:description')),
                ('og_see_also', models.TextField(blank=True, verbose_name='og:see_also')),
                ('article_published_time', models.DateTimeField(blank=True, null=True, verbose_name='article:published_time')),
                ('article_modified_time', models.DateTimeField(blank=True, null=True, verbose_name='article:modified_time')),
                ('article_section', models.CharField(blank=True, max_length=255, verbose_name='article:section')),
                ('article_author', models.CharField(blank=True, max_length=255, verbose_name='article:author')),
                ('article_publisher', models.CharField(blank=True, max_length=255, verbose_name='article:publisher')),
                ('article_tag', models.CharField(blank=True, max_length=255, verbose_name='article:tag')),
                ('itemscope_itemtype', models.CharField(blank=True, choices=[('http://schema.org/Article', 'Article'), ('http://schema.org/Blog', 'Blog'), ('http://schema.org/Book', 'Book'), ('http://schema.org/Event', 'Event'), ('http://schema.org/LocalBusiness', 'LocalBusiness'), ('http://schema.org/Organization', 'Organization'), ('http://schema.org/Person', 'Person'), ('http://schema.org/Product', 'Product'), ('http://schema.org/Review', 'Review'), ('http://schema.org/Other', 'Other'), ('http://schema.org/WebSite', 'WebSite')], max_length=255, verbose_name='itemscope itemtype')),
                ('itemprop_name', models.CharField(blank=True, max_length=255, verbose_name='itemprop=name')),
                ('itemprop_description', models.CharField(blank=True, max_length=255, verbose_name='itemprop=description')),
                ('itemprop_image', models.ImageField(blank=True, max_length=255, upload_to='sodaseo_images/', verbose_name='itemprop=image')),
                ('twitter_card', models.CharField(blank=True, max_length=255, verbose_name='twitter:card')),
                ('twitter_site', models.CharField(blank=True, max_length=255, verbose_name='twitter:site')),
                ('twitter_title', models.CharField(blank=True, max_length=255, verbose_name='twitter:title')),
                ('twitter_description', models.CharField(blank=True, max_length=255, verbose_name='twitter:description')),
                ('twitter_creator', models.CharField(blank=True, max_length=255, verbose_name='twitter:creator')),
                ('twitter_image', models.ImageField(blank=True, max_length=255, upload_to='sodaseo_images/', verbose_name='twitter:image')),
                ('object_id', models.PositiveIntegerField()),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType')),
            ],
            options={
                'verbose_name': 'entrada seo',
                'verbose_name_plural': 'entradas seo',
                'ordering': ('created_at',),
            },
        ),
        migrations.CreateModel(
            name='Template',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Atualizado em')),
                ('name', models.CharField(max_length=255, verbose_name='nome')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='identificador')),
                ('body', models.TextField(verbose_name='conteúdo')),
            ],
            options={
                'verbose_name': 'template',
                'verbose_name_plural': 'templates',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Url',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Atualizado em')),
                ('path', models.CharField(help_text='Formato: /url-da-pagina/', max_length=255, verbose_name='caminho')),
                ('description', models.TextField(blank=True, verbose_name='instruções de ajuda')),
                ('site', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='sodaseo_urls', to='sites.Site', verbose_name='site')),
            ],
            options={
                'verbose_name': 'url',
                'verbose_name_plural': 'urls',
                'ordering': ['path'],
            },
        ),
        migrations.CreateModel(
            name='Var',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Atualizado em')),
                ('name', models.CharField(max_length=255, verbose_name='nome')),
                ('description', models.TextField(verbose_name='descrição')),
                ('url', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vars', to='sodaseo.Url', verbose_name='url')),
            ],
            options={
                'verbose_name': 'variável',
                'verbose_name_plural': 'variáveis',
                'ordering': ['name'],
            },
        ),
        migrations.AddField(
            model_name='seo',
            name='template',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sodaseo.Template', verbose_name='template'),
        ),
        migrations.AlterUniqueTogether(
            name='url',
            unique_together=set([('site', 'path')]),
        ),
    ]
