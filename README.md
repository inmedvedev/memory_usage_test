# Тестовое задание

## Описание

Реализованы три метода api:
- /api/memory_usage/create - POST запрос созадния объекта
- /api/memory_usage/< memory_usage_id >/update - PUT запрос изменения объекта
- /api/memory_usage/ - GET запрос

Периодичная celery таска для получения использования RAM в % и записи в MongoDB

## Как запустить

```bash
docker compose up -d
```