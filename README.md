# Soda SEO

Aplicativo para gerenciar as configurações de meta tags para SEO no django.

Para o correto funcionamento, o projeto Django deve ter o django-suit, django-filer e easy-thumbnails pré instalados.

## Instalação

Adicione a seguinte linha no requirements.txt do projeto

```
-e git+git@gitlab.sodavirtual.com.br:sodavirtual/soda-seo.git#egg=soda-seo-master
```

Depois instale as dependências do projeto normalmente

```
pip install -r requirements.txt
```

No settings.py adicione o sodaseo e django_ace no INSTALLED_APPS

```python
INSTALLED_APPS = (
    # django suit first
    'suit',
    # django core apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.sitemaps',
    # third party apps
    'filer',
    'easy_thumbnails',
    'django_ace',
    'sodaseo',
    # local apps
    'apps.core',
)
```

## Como Funciona

O funcionamento é bastante simples, os passos iniciais são esses:

1. Cadastrar um template padrão em /admin/sodaseo/template/.
2. Configurar as informações básicas do site em /admin/sodaseo/config/.
3. Criar a configuração para as urls do site em /admin/sodaseo/url/.
4. Criar a configuração para os objetos do site. Exemplo: Post de um Blog.

## Template padrão

O sistema funciona usando a sintaxe de template do próprio Django, atualmente o template padrão é esse:

```python
{% load thumbnail %}
{% load sodaseo_tags %}

<!-- Base -->

{% if sodaseo.title %}
<title>{% sodaseo_render_value sodaseo.title %}</title>
{% endif %}

{% if sodaseo.description %}
<meta name="description" content="{% sodaseo_render_value sodaseo.description %}">
{% endif %}

{% if sodaseo.keywords %}
<meta name="keywords" content="{% sodaseo_render_value sodaseo.keywords %}">
{% endif %}

{% if sodaseo.author %}
<meta name="author" content="{% sodaseo_render_value sodaseo.author %}">
{% endif %}

<!-- Facebook/Google -->

{% if sodaseo.google_site_verification %}
<meta name="google-site-verification" content="{{ sodaseo.google_site_verification }}">
{% endif %}

{% if sodaseo.fb_appid %}
<meta property="fb:app_id" content="{{ sodaseo.fb_appid }}" />
{% endif %}

<!-- OpenGraph -->

{% if sodaseo.og_site_name %}
<meta property="og:site_name" content="{% sodaseo_render_value sodaseo.og_site_name %}" />
{% endif %}

{% if sodaseo.og_title %}
<meta property="og:title" content="{% sodaseo_render_value sodaseo.og_title %}" />
{% endif %}

{% if sodaseo.og_type %}
<meta property="og:type" content="{% sodaseo_render_value sodaseo.og_type %}" />
{% endif %}

{% if sodaseo.og_image %}
<meta property="og:image" content="http://{{ request.get_host }}{% thumbnail sodaseo.og_image 600x315 upscale crop="smart" %}" />
{% endif %}

{% if sodaseo.og_url %}
<meta property="og:url" content="{% sodaseo_render_value sodaseo.og_url %}" />
{% else %}
<meta property="og:url" content="{{ request.build_absolute_uri }}" />
{% endif %}

{% if sodaseo.og_description %}
<meta property="og:description" content="{% sodaseo_render_value sodaseo.og_description %}" />
{% endif %}

{% if sodaseo.article_published_time %}
<meta property="article:published_time" content="{% sodaseo_render_value sodaseo.article_published_time %}" />
{% endif %}

{% if sodaseo.article_modified_time %}
<meta property="article:modified_time" content="{% sodaseo_render_value sodaseo.article_modified_time %}" />
{% endif %}

{% if sodaseo.article_section %}
<meta property="article:section" content="{% sodaseo_render_value sodaseo.article_section %}" />
{% endif %}

{% if sodaseo.article_tag %}
<meta property="article:tag" content="{% sodaseo_render_value sodaseo.article_tag %}" />
{% endif %}

<meta property="og:locale" content="pt_BR" />

<!-- Google Plus -->
{% if sodaseo.itemprop_name %}
<meta itemprop="name" content="{% sodaseo_render_value sodaseo.itemprop_name %}">
{% endif %}

{% if sodaseo.itemprop_description %}
<meta itemprop="description" content="{% sodaseo_render_value sodaseo.itemprop_description %}">
{% endif %}

{% if sodaseo.itemprop_image %}
<meta itemprop="image" content="http://{{ request.get_host }}{% thumbnail sodaseo.itemprop_image 600x315 upscale crop="smart" %}">
{% endif %}

<!-- Twitter Card -->

{% if sodaseo.twitter_card %}
<meta name="twitter:card" content="{% sodaseo_render_value sodaseo.twitter_card %}">
{% endif %}

{% if sodaseo.twitter_site %}
<meta name="twitter:site" content="{% sodaseo_render_value sodaseo.twitter_site %}">
{% endif %}

{% if sodaseo.twitter_title %}
<meta name="twitter:title" content="{% sodaseo_render_value sodaseo.twitter_title %}">
{% endif %}

{% if sodaseo.twitter_description %}
<meta name="twitter:description" content="{% sodaseo_render_value sodaseo.twitter_description %}">
{% endif %}

{% if sodaseo.twitter_creator %}
<meta name="twitter:creator" content="{% sodaseo_render_value sodaseo.twitter_creator %}">
{% endif %}

{% if sodaseo.twitter_image %}
<meta name="twitter:image" content="http://{{ request.get_host }}{% thumbnail sodaseo.twitter_image 120x120 upscale crop="smart" %}">
{% endif %}
```

Um objeto sodaseo é carregado e com ele temos todos os campos que foram cadastrados.

Usamos a tag {% sodaseo_render_value valor %} para carregar as informações. Essa tag é responsável por processar as variáveis que são inseridas nos campos.

## Exemplo prático

Vamos pensar em um aplicativo de blog que contém categorias, tags, posts e arquivos por mês/ano.

Nesse app teremos as seguintes urls:

* /blog/ - Lista com todos os posts
* /blog/?page={{ page }} - Lista com todos os posts com paginação
* /blog/?tag={{ tag }} - Filtro por tag
* /blog/?tag={{ tag }}&page={{ page }} - Filtro por tag com paginação
* /blog/?categoria={{ categoria }} - Filtro por categoria
* /blog/?categoria={{ categoria }}&page={{ page }} - Filtro por categoria com paginação
* /blog/?arquivo={{ arquivo }} - Filtro por mês/ano
* /blog/?arquivo={{ arquivo }}&page={{ page }} - Filtro por mês/ano com paginação
* /blog/?busca={{ busca }} - Filtro por termo
* /blog/?busca={{ busca }}&page={{ page }} - Filtro por termo com paginação
* /blog/slug/ - Detalhe de um post específico

Cada url dessa vai estar cadastrada no sistema, com exceção do /blog/slug/, nesse caso as informações vem da configuração no próprio post.

## Variáveis globais

Os campos definidos na configuração em /admin/sodaseo/config/ se tornam globais, são esses os campos:

* {{ sodaseo.site_name }} - Nome do site.
* {{ sodaseo.google_site_verification }} - Código para o google webtools
* {{ sodaseo.fb_appid }} - App id do facebook.

Geralmente usamos bastante o {{ sodaseo.site_name }} nos campos.


