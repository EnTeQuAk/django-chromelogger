import base64
import json
import logging
import threading

from .compat import MiddlewareMixin


HEADER_DATA = {
    'version': 1,
    'columns': ['log', 'backtrace', 'type'],
}

STORAGE = threading.local()


def map_level(level):
    """Maps a logging level to a string understood by browser devtools."""
    if level >= logging.ERROR:
        return 'error'
    elif level >= logging.WARNING:
        return 'warn'
    elif level >= logging.INFO:
        return 'info'
    return ''


def encode_data(data):
    """Return a base64 encoded json dump."""
    encoded = base64.b64encode(
        json.dumps(data).encode('utf-8')
    )

    assert len(encoded) < 250 * 1024
    return encoded


class ChromeLoggerHandler(logging.Handler):
    def emit(self, record):
        try:
            STORAGE.records.append(record)
        except AttributeError:
            pass


class LoggingMiddleware(MiddlewareMixin):

    def process_response(self, request, response):
        STORAGE.records = log_records = []

        try:
            logging_data = HEADER_DATA.copy()
            rows = [
                [
                    ['{}:'.format(record.name), record.getMessage().strip()],
                    '{} : {}'.format(record.pathname, record.lineno),
                    map_level(record.levelno)
                ]
                for record in log_records
            ]

            msg = '{} request to {}'.format(
                request.method, request.get_full_path()
            )

            rows.insert(0, [[msg], '', 'group'])
            rows.append([[], '', 'groupEnd'])
            logging_data['rows'] = rows
            response['X-ChromeLogger-Data'] = encode_data(logging_data)
            return response
        finally:
            del STORAGE.records
