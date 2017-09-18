"""Defaults urls for the Zinnia AJAX project"""
from django.conf.urls import url
from django.conf.urls import include
from django.utils.text import slugify

from zinnia.views.archives import EntryIndex


def get_urlpatterns(blog_url='blog'):
    from zinnia.urls import urlpatterns
    return [
        url(r'^$', EntryIndex.as_view(), name='ajax-home'),
        url(r'^%s/' % slugify(blog_url), include(urlpatterns))
    ]
