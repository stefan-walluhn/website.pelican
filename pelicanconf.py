#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Stefan'
SITENAME = u'Stefan Walluhn'
SITESUBTITLE = u'Systemadministrator'
SITEURL = 'https://stefan.walluhn.de'

PATH = 'content'

TIMEZONE = 'Europe/Berlin'

DEFAULT_LANG = u'de'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = 'feeds/all.atom'
FEED_ALL_RSS = 'feeds/all.rss'
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

STATIC_PATHS = ['images', 'extra/favicon.ico', 'extra/logo.svg']
EXTRA_PATH_METADATA = {
    'extra/favicon.ico': {'path': 'favicon.ico'},
    'extra/logo.svg': {'path': 'logo.svg'}
}

MENUITEMS = [('Archiv', '/archives.html')]

THEME = 'nest'
NEST_CSS_MINIFY = True
NEST_SITEMAP_MENU = [('Archiv', '/archives.html'),('Tags','/tags.html'), ('Kategorien','/categories.html')]
NEST_INDEX_HEAD_TITLE = u'Stefan Walluhn'
NEST_INDEX_HEADER_TITLE = u'Systemadministrator'
NEST_INDEX_HEADER_SUBTITLE = u'Gedanken, Erfahrungen, Eindrücke'
NEST_INDEX_CONTENT_TITLE = u'Letzte Einträge'
NEST_ARCHIVES_HEAD_TITLE = u'Archiv'
NEST_ARCHIVES_HEAD_DESCRIPTION = u'Posts Archives'
NEST_ARCHIVES_HEADER_TITLE = u'Archiv'
NEST_ARCHIVES_HEADER_SUBTITLE = u'Archiv aller Posts'
NEST_ARCHIVES_CONTENT_TITLE = u'Archiv'
NEST_ARTICLE_HEADER_BY = u'Von'
NEST_ARTICLE_HEADER_MODIFIED = u'verändert'
NEST_ARTICLE_HEADER_IN = u'veröffentlich in'
NEST_CATEGORIES_HEAD_TITLE = u'Kategorien'
NEST_CATEGORIES_HEAD_DESCRIPTION = u'Archives listed by category'
NEST_CATEGORIES_HEADER_TITLE = u'Kategorien'
NEST_CATEGORIES_HEADER_SUBTITLE = u'Archives listed by category'
NEST_CATEGORY_HEAD_TITLE = u'Archiv Kategorie'
NEST_CATEGORY_HEAD_DESCRIPTION = u'Archiv Kategorie'
NEST_CATEGORY_HEADER_TITLE = u'Kategorie'
NEST_CATEGORY_HEADER_SUBTITLE = u'Archiv Kategorie'
NEST_TAGS_HEAD_TITLE = u'Tags'
NEST_TAGS_HEAD_DESCRIPTION = u'Tags List'
NEST_TAGS_HEADER_TITLE = u'Tags'
NEST_TAGS_HEADER_SUBTITLE = u'Tags List'
NEST_TAGS_CONTENT_TITLE = u'Tags List'
NEST_TAGS_CONTENT_LIST = u'tagged'
NEST_TAG_HEAD_TITLE = u'Archiv Tag'
NEST_TAG_HEAD_DESCRIPTION = u'Archiv Tag'
NEST_TAG_HEADER_TITLE = u'Tag'
NEST_TAG_HEADER_SUBTITLE = u'Archiv Tag'
NEST_PAGINATION_PREVIOUS = u'Previous'
NEST_PAGINATION_NEXT = u'Next'

