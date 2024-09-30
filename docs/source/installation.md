# Инструкция по установке требований

Эта инструкция поможет вам установить необходимые инструменты для работы с шаблоном парсеров для AI-помощника. 
Инструкция ориентирована на пользователей Windows. 
Пользователям macOS и Linux может потребоваться адаптировать некоторые команды.

## Установка `pipx`

`pipx` - это инструмент для установки и запуска Python-приложений в изолированных средах.

1. Установите `pipx`:
    ```bash
    py -m pip install --user pipx
    ```
2. Если появится предупреждение о том, что скрипт не находится в PATH:
    ```bash
    WARNING: The script pipx.exe is installed in `<USER folder>\AppData\Roaming\Python\Python3x\Scripts` which is not on PATH
    ```
   Выполните следующую команду:
   ```bash
   py -m pipx ensurepath
   ```
3. Перезапустите командную строку.
4. Проверьте установку:
   ```bash
   pipx --version
   ```

## Установка `Poetry`

Poetry - это инструмент для управления зависимостями и пакетами Python.

1. Установите Poetry через `pipx`:
   ```haskell
   pipx install poetry
   ```
2. Проверьте установку:
   ```bash
   poetry --version
   ```

## Установка `Cookiecutter`

Cookiecutter - это инструмент для создания проектов из шаблонов.

1. Установите `Cookiecutter` через `pipx`:
   ```haskell
   pipx install cookiecutter
   ```
2. Проверьте установку:
   ```bash
   cookiecutter --version
   ```

## Заключение

Теперь у вас установлены все необходимые инструменты для работы с шаблоном парсинга AI-ассистента. 
Вы можете приступать к созданию вашего проекта.

```{include} _additional_resources.md
```
