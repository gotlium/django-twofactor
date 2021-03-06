# -*- coding: utf8 -*-

from setuptools import setup

version = '0.0.1'
description = 'django auth integration with twofactor and googleauthentication'

setup(
    name='django-twofactor',
    version=version,
    description=description,
    long_description=open('README.mdown').read(),
    keywords='django auth googleauthenticator multifactor twofactor',
    author='Sven Aßmann',
    author_email='sven.assmann@lubico.biz',
    url='https://github.com/sassman/django-twofactor',
    download_url='https://github.com/sassman/django-twofactor.git',
    packages=[
        'django_twofactor',
    ],
    package_data={'django_twofactor': [
        'templates/admin/includes_grappelli/*.html',
        'templates/twofactor_admin/*.html',
        'templates/twofactor_admin/registration/*.html',
    ]},
    include_package_data=True,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ],
    zip_safe=False,
    install_requires=[
        'oath>=1.0',
        'django>=1.4,<1.5.99',
        'pycrypto',
        'setuptools',
    ]
)
