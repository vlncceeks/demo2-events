import os
import django

# Установите переменную окружения для указания файла настроек Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')

# Инициализация Django
django.setup()

from django.contrib.auth.models import User





superuser = 'Adminn'




# Создание суперпользователя
if not User.objects.filter(username=superuser).exists():
    User.objects.create_superuser(superuser, 'admin@example.com', 'adminpassword')
    print("Суперпользователь создан успешно")
else:
    print("Суперпользователь уже существует")