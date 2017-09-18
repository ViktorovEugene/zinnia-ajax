"""Apps for Zinnia AJAX"""
from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class ZinniaAjaxConfig(AppConfig):
    """
    Config for Zinnia AJAX application.
    """
    name = 'zinnia-ajax'
    label = 'zinnia-ajax'
    verbose_name = _('Zinnia Blog AJAX')
