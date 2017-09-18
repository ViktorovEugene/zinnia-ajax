try:
    from threading import local
except ImportError:
    from django.utils._threading_local import local

from django.utils.deprecation import MiddlewareMixin

BASE_TEMPLATE = 'zinnia/skeleton.html'
BASE_REST_TEMPLATE = 'zinnia/skeleton_ajax.html'
AJAX_CONTENT_TEMPLATE = 'zinnia/skeleton_ajax_content.html'

_thread_locals = local()


def get_current_template():
    return getattr(_thread_locals, 'current_template', None) or BASE_TEMPLATE


class ZinniaCurrentTemplateMiddleware(MiddlewareMixin):
    def process_view(self, request, *args, **kwargs):
        if request.META.get('HTTP_ACCEPT') == 'text/ajax-content':
            _thread_locals.current_template = AJAX_CONTENT_TEMPLATE
        elif request.resolver_match.app_name == 'zinnia' \
                and request.resolver_match.url_name == 'ajax-home':
            _thread_locals.current_template = BASE_REST_TEMPLATE
        else:
            _thread_locals.current_template = None
