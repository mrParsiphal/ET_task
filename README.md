Сервер для сбора данных об утилизации ЦП клиентов linux и выдачи 100 последних сообщений в виде страницы или json файла.

Сервер можно запустить через Docker.

Для запуска вручную необходимо:
1)Установить в ВО django и gunicorn
2)Выполнить миграции для создания БД sqllite.
3)Собрать staticfiles.
4)Выполнить комманду "gunicorn -b 0.0.0.0:80 ET_task.wsgi:application" (порт на своё усмотрение) для запуска сервера gunicorn.
