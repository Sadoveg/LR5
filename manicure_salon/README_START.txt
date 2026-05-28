Как запустить проект:

1. Откройте папку LR5/manicure_salon в VS Code.
2. Активируйте окружение из корневой папки LR5:
   source venv/Scripts/activate
3. Перейдите в папку проекта:
   cd manicure_salon
4. Выполните миграции:
   python manage.py migrate
5. Запустите сервер:
   python manage.py runserver
6. Откройте в браузере:
   http://127.0.0.1:8000/

Страницы сайта:
/ — главная
/services/ — услуги
/masters/ — мастера
/booking/ — запись
/contacts/ — контакты
/admin/ — админ-панель
