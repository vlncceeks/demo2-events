import os
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = 'Создает суперпользователя, если его еще нет'

    def handle(self, *args, **kwargs):
        # Проверяем, существует ли суперпользователь
        if not User.objects.filter(is_superuser=True).exists():
            User.objects.create_superuser(
                username=os.environ.get('SUPERUSER_USERNAME', 'admin'),
                email=os.environ.get('SUPERUSER_EMAIL', 'vlncceeks@gmail.com'),
                password=os.environ.get('SUPERUSER_PASSWORD', 'adminpassword')
            )
            self.stdout.write(self.style.SUCCESS('Суперпользователь был успешно создан!'))
        else:
            self.stdout.write(self.style.SUCCESS('Суперпользователь уже существует!'))