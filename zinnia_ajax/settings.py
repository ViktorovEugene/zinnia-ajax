"""Settings of Zinnia AJAX"""
from django.conf import settings

ZINNIA_AJAX_ORIGIN_SKELETON_TEMPLATE = getattr(
    settings, 'ZINNIA_AJAX_ORIGIN_SKELETON_TEMPLATE', 'zinnia/skeleton.html')

ZINNIA_AJAX_SKELETON_TEMPLATE = getattr(
    settings, 'ZINNIA_AJAX_SKELETON_TEMPLATE', 'zinnia/skeleton_ajax.html')

ZINNIA_AJAX_RESPONSE_SKELETON_TEMPLATE = getattr(
    settings, 'ZINNIA_AJAX_RESPONSE_SKELETON_TEMPLATE',
    'zinnia/skeleton_ajax_response.html')
