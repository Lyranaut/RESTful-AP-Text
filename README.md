# RESTful-AP-Text

# 1. Створіть і активуйте віртуальне середовище
python -m venv venv
source venv/bin/activate  # На Windows використовуйте `venv\Scripts\activate`

# 2. Встановіть необхідні бібліотеки
pip install -r requirements.txt

# Якщо у вас ще немає `requirements.txt`, ви можете створити його наступним чином:
# pip freeze > requirements.txt
# І додайте наступні бібліотеки до файлу `requirements.txt`:
# Django>=4.0,<5.0
# djangorestframework>=3.14.0,<4.0
# psycopg2-binary>=2.9.6,.0
# django-filter>=23.2,<24.0

# 3. Налаштуйте PostgreSQL
# Увійдіть в PostgreSQL та створіть базу даних і користувача:
psql -U postgres
CREATE DATABASE library_db;
CREATE USER library_user WITH PASSWORD 'yourpassword';
GRANT ALL PRIVILEGES ON DATABASE library_db TO library_user;
\q

# Відредагуйте файл `library_api/settings.py`, щоб налаштувати з'єднання з PostgreSQL:
# Знайдіть налаштування DATABASES і змініть їх наступним чином:
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'library_db',
#         'USER': 'library_user',
#         'PASSWORD': 'yourpassword',
#         'HOST': 'localhost',
#         'PORT': '5432',
#     }
# }

# 4. Застосуйте міграції для створення необхідних таблиць у базі даних
python manage.py makemigrations
python manage.py migrate

# 5. Запустіть сервер
python manage.py runserver

# 6. (Необов'язково) Запустіть тести, щоб переконатися, що все працює правильно
python manage.py test
