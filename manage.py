#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
    try:
        from django.core.management import execute_from_command_line
        import django
        # Инициализация Django
        django.setup()
        from django.contrib.auth.models import User
        superuser = 'ADMIN'
        # Создание суперпользователя
        if not User.objects.filter(username=superuser).exists():
            User.objects.create_superuser(superuser, 'admin@example.com', 'adminpassword')
            print("Суперпользователь создан успешно")
        else:
            print("Суперпользователь уже существует")
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
