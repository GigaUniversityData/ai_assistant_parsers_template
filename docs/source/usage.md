# Использование

## Структура проекта

```haskell
.
├── output  # Выходные данные
│   └── parse_one  # Результат работы скрипта `parse_one`
├── poetry.lock  # Фиксированные версии пакетов
├── pyproject.toml  # Настройки Python зависимостей и сборка
├── sandbox  # Песочница
│   └── parse_many.ipynb  # Блокнот для парсинга нескольких URL-адресов
├── scripts  # Скрипты
│   └── mkinit.py  # Скрипт для автоматического заполнения `__init__.py` файлов
├── src
│   ├── cli  # CLI-скрипты
│   │   └── parse_one.py  # Скрипт для парсинга одного URL-адреса
│   ├── parsers
│   │   ├── domain  # Парсеры для одного домена
│   │   ├── multiple_domains  # Парсеры для нескольких доменов
│   │   └── page  # Парсеры для одной страницы
│   ├── refiners
│   │   ├── clean_aside.py  # Очищает тег `aside`
│   │   ├── clean_empty_tags.py  # Очищает пустые теги
│   │   └── hide_protected_mails.py  # Скрывает email-адреса под защитой
│   └── settings.py  # Настройки проекта
```

## Запуск

Используйте утилиту `parse_one` для парсинга одного сайта по URL-адресу:
```haskell
python3 -m src.cli.parse_one https://spbu.ru/universitet
```
Или попробуйте скрипт в [parse_many](sandbox/parse_many.ipynb) в `sandbox`

Результаты работы скриптов лежат в папке [output](output)
