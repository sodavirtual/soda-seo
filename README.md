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

No base.html inserir a tag do sodaseo

```python
{% load sodaseo_tags %}
<!doctype html>
<html lang="pt-br" {% if sodaseo.itemscope_itemtype %}itemscope itemtype="{{ sodaseo.itemscope_itemtype }}"{% endif %}>
<head>
  <meta charset="utf-8">
  {% sodaseo_render_tags site_id=1 %}
</head>

<body>
  {% block body %}{% endblock %}
  {% sodaseo_render_analytics %}
</body>
</html>
```

## Como Funciona

O funcionamento é bastante simples, os passos iniciais são esses:

1. Cadastrar um template padrão em /admin/sodaseo/template/.
2. Configurar as informações básicas do site em /admin/sodaseo/config/.
3. Criar a configuração para as urls do site em /admin/sodaseo/url/.
4. Criar a configuração para os objetos do site. Exemplo: Post de um Blog.

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
* {{ sodaseo.fb_profile_id }} - Profile id do facebook.

Geralmente usamos bastante o {{ sodaseo.site_name }} nos campos.
