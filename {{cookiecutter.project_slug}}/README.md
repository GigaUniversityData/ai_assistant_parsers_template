# AI Assistant Parsers {{cookiecutter.university_name}} (Пример проекта)

# Установка

1. Иметь Python 3.12 и выше
2. Установить Poetry: https://python-poetry.org/docs/#installation (Poetry - это инструмент для управления зависимостями и упаковки в Python)
3. В настройках проекта PyCharm добавить интерпретатор на основе Poetry
4. Вы молодцы! Проект готов к работе!

# Использование

Используйте утилиту `parse_one` для парсинга одного сайта по URL-адресу:
```haskell
python3 -m src.cli.parse_one https://spbu.ru/universitet
```
Или попробуйте скрипт в [parse_many](sandbox/parse_many.ipynb) в `sandbox`

Результаты работы скриптов лежат в папке [output](output)

# Структура проекта

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
