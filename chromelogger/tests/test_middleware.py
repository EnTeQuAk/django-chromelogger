from django.http import HttpResponse
from django.test import RequestFactory

from chromelogger.middleware import LoggingMiddleware


HEADER = 'X-ChromeLogger-Data'
rf = RequestFactory()


def test_catches_logging():
    request = rf.get('/')
    response = HttpResponse()
    LoggingMiddleware().process_response(request, response)
    assert HEADER in response
