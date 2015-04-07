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

<!-- Base -->

{% if sodaseo.title %}
<title>{{ sodaseo.title }} - {{ sodaseo.site_name }}</title>
{% endif %}

{% if sodaseo.keywords %}
<meta name="keywords" content="{{ sodaseo.keywords }}">
{% endif %}

{% if sodaseo.description %}
<meta name="description" content="{{ sodaseo.description }}">
{% endif %}

{% if sodaseo.author %}
<meta name="author" content="{{ sodaseo.author }}">
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
<meta property="og:site_name" content="{{ sodaseo.og_site_name }}" />
{% endif %}

{% if sodaseo.og_title %}
<meta property="og:title" content="{{ sodaseo.og_title }}" />
{% endif %}

{% if sodaseo.og_type %}
<meta property="og:type" content="{{ sodaseo.og_type }}" />
{% endif %}

{% if sodaseo.og_image %}
<meta property="og:image" content="http://{{ request.get_host }}{% thumbnail sodaseo.og_image 600x315 upscale crop="smart" %}" />
{% endif %}

{% if sodaseo.og_url %}
<meta property="og:url" content="{{ sodaseo.og_url }}" />
{% else %}
<meta property="og:url" content="{{ request.build_absolute_uri }}" />
{% endif %}

{% if sodaseo.og_description %}
<meta property="og:description" content="{{ sodaseo.og_description }}" />
{% endif %}

{% if sodaseo.article_published_time %}
<meta property="article:published_time" content="{{ sodaseo.article_published_time }}" />
{% endif %}

{% if sodaseo.article_modified_time %}
<meta property="article:modified_time" content="{{ sodaseo.article_modified_time }}" />
{% endif %}

{% if sodaseo.article_section %}
<meta property="article:section" content="{{ sodaseo.article_section }}" />
{% endif %}

{% if sodaseo.article_tag %}
<meta property="article:tag" content="{{ sodaseo.article_tag }}" />
{% endif %}

<meta property="og:locale" content="pt_BR" />

<!-- Google Plus -->
{% if sodaseo.itemprop_name %}
<meta itemprop="name" content="{{ sodaseo.itemprop_name }}">
{% endif %}

{% if sodaseo.itemprop_description %}
<meta itemprop="description" content="{{ sodaseo.itemprop_description }}">
{% endif %}

{% if sodaseo.itemprop_image %}
<meta itemprop="image" content="http://{{ request.get_host }}{% thumbnail sodaseo.itemprop_image 600x315 upscale crop="smart" %}">
{% endif %}

<!-- Twitter Card -->

{% if sodaseo.twitter_card %}
<meta name="twitter:card" content="{{ sodaseo.twitter_card }}">
{% endif %}

{% if sodaseo.twitter_site %}
<meta name="twitter:site" content="{{ sodaseo.twitter_site }}">
{% endif %}

{% if sodaseo.twitter_title %}
<meta name="twitter:title" content="{{ sodaseo.twitter_title }}">
{% endif %}

{% if sodaseo.twitter_description %}
<meta name="twitter:description" content="{{ sodaseo.twitter_description }}">
{% endif %}

{% if sodaseo.twitter_creator %}
<meta name="twitter:creator" content="{{ sodaseo.twitter_creator }}">
{% endif %}

{% if sodaseo.twitter_image %}
<meta name="twitter:image" content="http://{{ request.get_host }}{% thumbnail sodaseo.twitter_image 120x120 upscale crop="smart" %}">
{% endif %}
```

No geral vamos trabalhar com estruturas de if/elif/else/endif nesse template. 

Um objeto sodaseo é carregado e com ele temos todos os campos que foram cadastrados.

## Exemplo prático

Vamos pensar em um aplicativo de blog que contém categorias, tags, posts e arquivos por mês/ano.

Nesse app inicialmente teremos as seguintes urls:

* /blog/ - Lista com todos os posts + paginação
* /blog/slug/ - Detalhe de um post específico

Para o /blog/ é só cadastrar uma configuração para essa mesma url em /admin/sodaseo/url/. Já no caso do /blog/slug/ a configuração é feita no próprio cadastro do post.

Mas as configurações não param por ai, no caso do /blog/ existem vários filtros que são aplicados a essa url:

* /blog/?tag=tag1 - Filtra os posts por tag.
* /blog/?categoria=categoria-1 - Filtra os posts por categoria.
* /blog/?arquivo=04/2015 - Filtra os posts por mês/ano.
* /blog/?busca=busca - Filtra os posts por busca.

Nesse caso, é interessante que seja possível mudar algumas tags de acordo com esses filtros, nesse exemplo vamos alterar apenas as tags title e description.

Para isso, vamos criar um novo template em /admin/sodaseo/template/ e o seu conteúdo será esse:

```python
{% load thumbnail %}

<!-- Base -->

{% if sodaseo.title %}
    {% if tag %}
    <title>{{ sodaseo.title }} - {{ sodaseo.site_name }} - Busca por tag {{ tag.name }}</title>
    {% elif categoria %}
    <title>{{ sodaseo.title }} - {{ sodaseo.site_name }} - Busca por categoria {{ categoria.name }}</title>
    {% elif arquivo %}
    <title>{{ sodaseo.title }} - {{ sodaseo.site_name }} - Busca por mês {{ arquivo }}</title>
    {% elif busca %}
    <title>{{ sodaseo.title }} - {{ sodaseo.site_name }} - Busca por termo {{ busca }}</title>
    {% else %}
    <title>{{ sodaseo.title }} - {{ sodaseo.site_name }}</title>
    {% endif %}
{% endif %}

{% if sodaseo.keywords %}
<meta name="keywords" content="{{ sodaseo.keywords }}">
{% endif %}

{% if sodaseo.description %}
    {% if tag %}
    <meta name="description" content="{{ sodaseo.description }} - {{ tag.name }}">
    {% elif categoria %}
    <meta name="description" content="{{ sodaseo.description }} - {{ categoria.name }}">
    {% elif arquivo %}
    <meta name="description" content="{{ sodaseo.description }} - {{ arquivo }}">
    {% elif busca %}
    <meta name="description" content="{{ sodaseo.description }} - {{ busca }}">
    {% else %}
    <meta name="description" content="{{ sodaseo.description }}">
    {% endif %}
{% endif %}

{% if sodaseo.author %}
<meta name="author" content="{{ sodaseo.author }}">
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
<meta property="og:site_name" content="{{ sodaseo.og_site_name }}" />
{% endif %}

{% if sodaseo.og_title %}
<meta property="og:title" content="{{ sodaseo.og_title }}" />
{% endif %}

{% if sodaseo.og_type %}
<meta property="og:type" content="{{ sodaseo.og_type }}" />
{% endif %}

{% if sodaseo.og_image %}
<meta property="og:image" content="http://{{ request.get_host }}{% thumbnail sodaseo.og_image 600x315 upscale crop="smart" %}" />
{% endif %}

{% if sodaseo.og_url %}
<meta property="og:url" content="{{ sodaseo.og_url }}" />
{% else %}
<meta property="og:url" content="{{ request.build_absolute_uri }}" />
{% endif %}

{% if sodaseo.og_description %}
<meta property="og:description" content="{{ sodaseo.og_description }}" />
{% endif %}

{% if sodaseo.article_published_time %}
<meta property="article:published_time" content="{{ sodaseo.article_published_time }}" />
{% endif %}

{% if sodaseo.article_modified_time %}
<meta property="article:modified_time" content="{{ sodaseo.article_modified_time }}" />
{% endif %}

{% if sodaseo.article_section %}
<meta property="article:section" content="{{ sodaseo.article_section }}" />
{% endif %}

{% if sodaseo.article_tag %}
<meta property="article:tag" content="{{ sodaseo.article_tag }}" />
{% endif %}

<meta property="og:locale" content="pt_BR" />

<!-- Google Plus -->
{% if sodaseo.itemprop_name %}
<meta itemprop="name" content="{{ sodaseo.itemprop_name }}">
{% endif %}

{% if sodaseo.itemprop_description %}
<meta itemprop="description" content="{{ sodaseo.itemprop_description }}">
{% endif %}

{% if sodaseo.itemprop_image %}
<meta itemprop="image" content="http://{{ request.get_host }}{% thumbnail sodaseo.itemprop_image 600x315 upscale crop="smart" %}">
{% endif %}

<!-- Twitter Card -->

{% if sodaseo.twitter_card %}
<meta name="twitter:card" content="{{ sodaseo.twitter_card }}">
{% endif %}

{% if sodaseo.twitter_site %}
<meta name="twitter:site" content="{{ sodaseo.twitter_site }}">
{% endif %}

{% if sodaseo.twitter_title %}
<meta name="twitter:title" content="{{ sodaseo.twitter_title }}">
{% endif %}

{% if sodaseo.twitter_description %}
<meta name="twitter:description" content="{{ sodaseo.twitter_description }}">
{% endif %}

{% if sodaseo.twitter_creator %}
<meta name="twitter:creator" content="{{ sodaseo.twitter_creator }}">
{% endif %}

{% if sodaseo.twitter_image %}
<meta name="twitter:image" content="http://{{ request.get_host }}{% thumbnail sodaseo.twitter_image 120x120 upscale crop="smart" %}">
{% endif %}
```

Nas configurações da url o backend do projeto deve cadastrar quais variáveis estão disponíveis e como elas devem ser usadas.

Para esse exemplo as informações sobre as variáveis tag, categoria, arquivo e busca, estariam cadastradas, bem como uma descrição de como deve ser o seu uso.

