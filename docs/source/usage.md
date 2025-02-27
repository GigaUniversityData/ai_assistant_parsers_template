# Использование

Это руководство поможет вам разобраться в структуре проекта и начать использовать его.

## Структура проекта

```bash
├── poetry.lock                         # Фиксированные версии зависимостей
├── pyproject.toml                      # Конфигурация проекта и зависимостей
├── output                              # Директория для выходных данных
│   └── parse_one                       # Результаты работы скрипта `parse_one`
├── scripts                             # Вспомогательные скрипты
│   ├── parse_one.py                    # Скрипт для парсинга одного URL
│   └── mkinit.py                       # Скрипт для авто-генерации `__init__.py` файлов
└── src                                 # Исходный код проекта
    └── [имя_вашего_пакета]
        ├── settings.py                 # Настройки проекта
        ├── parsers                     # Модули парсеров
        │   ├── domain                  # Парсеры для конкретных доменов
        │   ├── multiple_domains        # Парсеры для нескольких доменов
        │   └── page                    # Парсеры для отдельных страниц
        └── refiners                    # Модули для пост-обработки данных
```

## Основные компоненты

1. **Парсеры** - модули, отвечающие за извлечение данных из Интернет-страниц для AI-помощника.
2. **Рефайнеры** - модули, обрабатывающие и очищающие данные после работы парсеров (пост-обработка). 
Их отличительной чертой является то, что они применяются **ко всем** парсерам после их работы.

## Настройка проекта

Самый важный файл в проекте - `src/[имя_вашего_пакета]/settings.py`, именно он будет использоваться для сбора данных.

Обратите особое внимание на этот файл, так как он играет важную роль в работе вашего проекта.

## Добавление новых компонентов в настройки

1. Добавление новых **парсеров**:
   - Создайте новый класс **парсера** в `src/[имя_вашего_пакета]/parsers/`
   - Добавьте **парсер** в список `PARSERS` в `settings.py`
2. Добавление новых **рефайнеров**:
   - Создайте новый класс **рефайнера** в `src/[имя_вашего_пакета]/refiners/`
   - Добавьте **рефайнер** в список `PARSING_REFINERS` в `settings.py`
3. Добавление **конфигурации фетчеров**:
   - Смотрите подробнее: [Конфигурация фетчеров](./advanced_usage/fetchers_config.md)


## Запуск парсинга

### Парсинг одного URL

Используйте скрипт `parse_one` для парсинга одного сайта:

```bash
python -m scripts.parse_one https://spbu.ru/universitet
```

Результаты будут сохранены в директории `output/parse_one/`.

### Парсинг нескольких URL

Для парсинга нескольких URL используйте Jupyter ноутбук `sandbox/parse_many.ipynb`.


## Дополнительная информация

Для более подробной информации о возможностях базовой библиотеки обратитесь к документации [AI Assistant Parsers Core](https://github.com/GigaUniversity/ai_assistant_parsers_core).

```{include} _additional_resources.md
```
