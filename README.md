# Тестовое задание.

Описание задания в файле [task.md](task.md).

Пример входного файла [example.xlsx](example.xlsx).

# Выполнение.

Выполнено создание базы данных (без ручного написания DDL, использован ORM SQLAlchemy).
Написан скрипт, который парсит файл .xlsx.
Написана функция, которая заносит данные из файла в базу данных.
Swagger-документация автоматическая от FastAPI (и неточная).
Упаковано в контейнеры.

# Запуск
Для использования базы данных Postgresql проекту требуется файл окружения .env, шаблон c тестовыми данными присутствует.
В ином случае (тестирование?) используется SQLite.
Запуск из папки с проектом
```docker-compose up -d```
После запуска проект доступен по адресу ```http://{your_domain}:8000/```
Автоматическая документация ```http://{your_domain}:8000/docs/```