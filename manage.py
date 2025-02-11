#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
from ai_portfolio_labs_base.ai_portfolio_labs_base_folder_path_getter import get_ai_portfolio_labs_base_folder_path


def main():
    try:
        django_apps_folder_path = \
            get_ai_portfolio_labs_base_folder_path() / 'b_source' / 'django_apps'

        sys.path.append(
            django_apps_folder_path.__str__())

        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ai_portfolio_labs.settings")

        from django.core.management import execute_from_command_line

        execute_from_command_line(
            sys.argv)

    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
