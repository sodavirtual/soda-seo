# -*- coding: utf-8 -*-
from setuptools import setup
import sodaseo

version = sodaseo.__version__

requires = [
    'Django>=1.6',
    'django-suit>=0.2.12',
    'django-filer>=0.9.9',
    'django-ace>=1.0.2',
    'django-qurl>=0.1.1',
    'coverage>=3.7.1',
    'model-mommy>=1.2.3',
    'South>=1.0.2',
    'six>=1.9.0',
]

setup(
    name='soda-seo',
    version=version,
    author='Allisson Azevedo',
    author_email='allisson@gmail.com',
    packages=['sodaseo', ],
    license='MIT',
    description='Soda SEO',
    long_description='App para gerenciar as informações de SEO.',
    url='http://gitlab.sodavirtual.com.br/sodavirtual/soda-seo',
    include_package_data=True,
    zip_safe=False,
    install_requires=requires
)
