try:
    from django.utils.deprecation import MiddlewareMixin
except ImportError:
    class MiddlewareMixin(object):
        """
        If this middleware doesn't exist, this is an older version of django
        and we don't need it.
        """
        pass
