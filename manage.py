#!/usr/bin/env python
import os
import sys

DEBUG = os.environ.get("DEBUG")

if __name__ == "__main__":
    if DEBUG == 'True':
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "review.settings.dev")
    else:
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "review.settings.production")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
