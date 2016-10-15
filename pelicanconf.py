#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Stefan'
SITENAME = u'Stefan Walluhn'
SITESUBTITLE = u'Systemadministrator'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Berlin'

DEFAULT_LANG = u'de'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Neuland.io', 'http://www.neuland.io/'),
         ('Terminal.21', 'http://www.terminal21.de/'),
         ('Radio Corax', 'http://www.radiocorax.de/'),
         ('Eigenbaukombinat', 'http://www.eigenbaukombinat.de'),)

# Social widget
SOCIAL = (('Github', 'https://github.com/stefan-walluhn'),
          ('code.neuland.io', 'https://code.neuland.io/u/stefan'),)

DEFAULT_PAGINATION = 10

RELATIVE_URLS = True

THEME = 'nest'
NEST_CSS_MINIFY = True
MENUITEMS = [('Homepage', '/'),('Categories','/categories.html')]
NEST_SITEMAP_MENU = [('Archives', '/archives.html'),('Tags','/tags.html'), ('Categories','/categories.html')]
