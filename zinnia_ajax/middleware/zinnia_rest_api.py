try:
    from threading import local
except ImportError:
    from django.utils._threading_local import local

from django.utils.deprecation import MiddlewareMixin
from zinnia_ajax import settings


SKELETON_ORIGIN = settings.ZINNIA_AJAX_ORIGIN_SKELETON_TEMPLATE
SKELETON_AJAX = settings.ZINNIA_AJAX_SKELETON_TEMPLATE
SKELETON_AJAX_RESPONSE = settings.ZINNIA_AJAX_RESPONSE_SKELETON_TEMPLATE

_thread_locals = local()


def get_current_template():
    return getattr(_thread_locals, 'current_template', None) or \
           SKELETON_ORIGIN


class ZinniaCurrentTemplateMiddleware(MiddlewareMixin):
    def process_view(self, request, *args, **kwargs):
        if request.META.get('HTTP_ACCEPT') == 'text/ajax-content':
            _thread_locals.current_template = SKELETON_AJAX_RESPONSE
        elif request.resolver_match.app_name == 'zinnia' \
                and request.resolver_match.url_name == 'ajax-home':
            _thread_locals.current_template = SKELETON_AJAX
        else:
            _thread_locals.current_template = None
