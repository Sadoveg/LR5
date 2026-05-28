Как запустить проект Beauty Nails Tula

1. Перейдите в папку проекта:
   cd D:/Web/LR5/manicure_salon

2. Активируйте виртуальное окружение:
   source ../venv/Scripts/activate

3. Установите зависимости, если нужно:
   pip install -r requirements.txt

4. Выполните миграции:
   python manage.py migrate

5. Запустите сервер:
   python manage.py runserver

6. Откройте сайт:
   http://127.0.0.1:8000/

Страницы сайта:
- /
- /services/
- /masters/
- /booking/
- /contacts/

Задачи по Python находятся в папке:
../python_tasks/
