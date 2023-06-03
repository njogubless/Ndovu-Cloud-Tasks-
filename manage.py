#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
from http.server import HTTPServer, SimpleHTTPRequestHandler

def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'report_system.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    if 'runserver' in sys.argv:
        # Start the HTTP server on port 8000
        httpd = HTTPServer(('localhost', 8000), SimpleHTTPRequestHandler)
        httpd.serve_forever()
    else:
       from django.core.management import execute_from_command_line
       execute_from_command_line()
     

