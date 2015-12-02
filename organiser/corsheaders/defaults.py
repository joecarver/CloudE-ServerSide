from django.conf import settings

default_headers = (
    'x-requested-with',
    'content-type',
    'content-range',
    'content-disposition',
    'content-description',
    'accept',
    'origin',
    'authorization',
    'x-csrftoken',
    'user-agent',
    'accept-encoding',
)

CORS_ALLOW_HEADERS = getattr(settings, 'CORS_ALLOW_HEADERS', default_headers)

default_methods = (
    'GET',
    'POST',
    'OPTIONS',
    'PUT',
    'PATCH',
    'DELETE',
)
CORS_ALLOW_METHODS = getattr(settings, 'CORS_ALLOW_METHODS', default_methods)

CORS_ALLOW_CREDENTIALS = getattr(settings, 'CORS_ALLOW_CREDENTIALS', False)

CORS_PREFLIGHT_MAX_AGE = getattr(settings, 'CORS_PREFLIGHT_MAX_AGE', 1728000)

CORS_ORIGIN_ALLOW_ALL = getattr(settings, 'CORS_ORIGIN_ALLOW_ALL', True)

CORS_ORIGIN_WHITELIST = getattr(settings, 'CORS_ORIGIN_WHITELIST', ())

CORS_ORIGIN_REGEX_WHITELIST = getattr(
    settings,
    'CORS_ORIGIN_REGEX_WHITELIST',
    ())

CORS_EXPOSE_HEADERS = getattr(settings, 'CORS_EXPOSE_HEADERS', ())

CORS_URLS_REGEX = getattr(settings, 'CORS_URLS_REGEX', '^.*$')

CORS_MODEL = getattr(settings, 'CORS_MODEL', None)

CORS_REPLACE_HTTPS_REFERER = getattr(
    settings,
    'CORS_REPLACE_HTTPS_REFERER',
    True)
