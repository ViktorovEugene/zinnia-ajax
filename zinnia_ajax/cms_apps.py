"""Application hooks for cmsplugin_zinnia with AJAX browsing utils"""
import warnings

from django.utils.translation import ugettext_lazy as _

try:
    from cms.apphook_pool import apphook_pool
    from cmsplugin_zinnia.cms_apps import ZinniaApphook
except ImportError:
    warnings.warn('Cannot import CMS application for Zinnia', RuntimeWarning)
else:
    class ZinniaAjaxApphook(ZinniaApphook):
        """
        Zinnia's AJAX Apphook
        """
        name = _('Zinnia AJAX Weblog')
        app_name = 'zinnia'

        def get_urls(self, page=None, language=None, **kwargs):
            from zinnia_ajax.urls import get_urlpatterns
            try:
                app_suburl = page.application_namespace
            except AttributeError:
                return [get_urlpatterns()]
            return [get_urlpatterns(app_suburl)]

    apphook_pool.register(ZinniaAjaxApphook)
