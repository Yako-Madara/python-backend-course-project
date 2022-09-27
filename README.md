# python-backend-course-project
Репозиторий для курсового проекта по курсу Web services

Установка и запуск:
Для установки необходим менеджер пакетов [poetry](https://python-poetry.org/)

```conda create -n env_name python=3.10.4```

```conda activate env_name```

```poetry install```

```cd app```

```poetry run uvicorn main:app```

Запуск тестов

* Модульные: ```poetry run pytest tests/unit_tests.py```

* Интеграционные: в какой-то степени они уже есть в модульных
