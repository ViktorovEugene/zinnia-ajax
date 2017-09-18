"""Context Processors for Zinnia AJAX"""
from zinnia_ajax.middleware.zinnia_rest_api import get_current_template


def template(request):
    """
    Provides appropriate template depending on the request type.
    """
    return {'ZINNIA_TEMPLATE': get_current_template()}
