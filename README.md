# Django Test Project

1. Запускаем команду для создания контейнера:

  docker-compose up --build

2. Корректируем переменны в .env (можно все оставить, главное настроить переменные, связанные с почтой).

3. Далее создаем суперпользователя для управления админ панелем.

   docker-compose run web bash
   cd api/
   python manage.py createsuperuser

4. Заходим в админ панель: http://localhost:8000/admin/

5. Создаем авторов для их выбора при создании книг.

Ссылка для управления книгами: http://localhost:8000/api/books
Ссылка для регистрации пользователя: http://localhost:8000/api/account/signup
