
## Дипломный проект

Сайт интернет-магазина.

## Документация по проекту

Для запуска проекта необходимо:

Установить зависимости:

```bash
pip install -r requirements.txt
```

Провести миграцию:

```bash
python manage.py migrate
```

Загрузить тестовые данные:

```bash
python manage.py loaddata fixtures.json
```

Запустить отладочный веб-сервер проекта:

```bash
python manage.py runserver
```