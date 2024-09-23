# Туториал

## Основы

Все парсеры в проекте делятся на 3 группы:

1. Парсеры одного домена (`domain`)
2. Парсеры нескольких доменов (`multiple_domains`)
3. Парсеры одной страницы (`page`)

Все они располагаются в папке `src/parsers/` в соответствующих папках. <br>
В каждой папке есть файлы `_template.py` в начальным кодом для копирования.

Давайте для начала напишем парсеры для группы `domain`.

# Domain парсеры

Давайте напишем парсер для домена `abiturient.spbu.ru`. <br>
Я скопирую код с `_template.py`:
```py
from bs4 import BeautifulSoup

from ai_assistant_parsers_core.parsers.utils.clean_blocks import *
from ai_assistant_parsers_core.parsers.utils.restructure_blocks import *
from ai_assistant_parsers_core.parsers import SimpleSelectDomainBaseParser


class ВСТАВИТЬ_ТЕКСТ_СЮДАDomainParser(SimpleSelectDomainBaseParser):
    def __init__(self) -> None:
        super().__init__(
            allowed_domains_paths=["ВСТАВИТЬ_ТЕКСТ_СЮДА"],
            select_arguments=["ВСТАВИТЬ_ТЕКСТ_СЮДА"]
        )
```
Теперь мы можем изменить название парсера на `AbiturientDomainParser`, а аргументом для `allowed_domains_paths` передать `["abiturient.spbu.ru"]`:
```py
class AbiturientDomainParser(SimpleSelectDomainBaseParser):
    def __init__(self) -> None:
        super().__init__(
            allowed_domains_paths=["abiturient.spbu.ru"],
            select_arguments=["ВСТАВИТЬ_ТЕКСТ_СЮДА"],
        )
```
Как мы видим нам ещё требуется `select_arguments`, но что же это?

CSS-Selector - это шаблоны, по которым парсер может находить HTML-документы. <br/>
Если вы не знакомы с ними, то можете почитать про них подробнее здесь, в них нет ничего трудного:
- https://developer.mozilla.org/ru/docs/Web/CSS/CSS_selectors
- https://facelessuser.github.io/soupsieve/selectors/


А от нас требуют как раз список специальных CSS-Selector, которые укажут парсеру какие HTML-теги вместе с их детьми оставить в структуре HTML-кода. <br/>
Все остальные теги будут удалены из структуры HTML-кода. Например, шапка и подвал, которые встречаются на всех страницах, но не несут полезной нам информации. <br/>

Простыми словами: мы указываем такие HTML-теги, в которых храниться действительно полезный контент страницы. <br/>

Давайте рассмотрим какую-то страницу из нашего поддомена, например https://abiturient.spbu.ru/programs/bakalavriat/.
Через консоль разработчика не сложно определить, что это `.page-main`.

Тогда наш код будет следующим:
```py
class AbiturientDomainParser(SimpleSelectDomainBaseParser):
    def __init__(self) -> None:
        super().__init__(
            allowed_domains_paths=["abiturient.spbu.ru"],
            select_arguments=[".page-main"],
        )
```
Но погодите, у нас захватывается так же `.page-main > aside` в нашем HTML-коде, который не является полезным.

К счастью в этом случае у нас есть 2 метода для реализации в нашем классе: 
- `_clean_parsed_html` - для очистки HTML-кода.
- `_restructure_parsed_html` - для изменения структуры HTML-кода.

Давайте воспользуемся методом `_clean_parsed_html` и утилитами из `ai_assistant_parsers_core.parsers.utils.clean_blocks`:
```py
from bs4 import BeautifulSoup

from ai_assistant_parsers_core.parsers.utils.clean_blocks import clean_one_by_select
...
class AbiturientDomainParser(SimpleSelectDomainBaseParser):
    def __init__(self) -> None:
        super().__init__(
            allowed_domains_paths=["abiturient.spbu.ru"],
            select_arguments=[".page-main"],
        )
        
    def _clean_parsed_html(self, soup: BeautifulSoup) -> None:
        clean_one_by_select(soup, ".page-main > aside")
```
Та-дам, теперь у нас очищается `.page-main > aside` - прекрасно.

Но есть ещё пара проблем - давайте рассмотрим их по порядку

1. Блоки `.useful-info` обрабатываются не корректно. 
А именно: блок `.useful-info__link` не нужен, а блок `h2.info-definition__title` должен иметь тег `h4`, а не `h2`
2. Блоки `.accordion__button > span` не помечены тегом заголовка, но несут его смысловую нагрузку.


Давайте это исправим, используя `_restructure_parsed_html` и `ai_assistant_parsers_core.parsers.utils.restructure_blocks`.
Тогда наш полный код будет выглядеть следующим образом:
```py
from bs4 import BeautifulSoup

from ai_assistant_parsers_core.parsers.utils.clean_blocks import clean_all_by_select, clean_one_by_select
from ai_assistant_parsers_core.parsers.utils.restructure_blocks import rename_all_by_select
from ai_assistant_parsers_core.parsers import SimpleSelectDomainBaseParser


class AbiturientDomainParser(SimpleSelectDomainBaseParser):
    def __init__(self) -> None:
        super().__init__(
            allowed_domains_paths=["abiturient.spbu.ru"],
            select_arguments=[".page-main"],
        )
        
    def _clean_parsed_html(self, soup: BeautifulSoup) -> None:
        clean_one_by_select(soup, ".page-main > aside")

    def _restructure_parsed_html(self, soup: BeautifulSoup) -> None:
        clean_all_by_select(soup, "button.useful-info__link")  # Кнопки "подробнее" не нужны из-за кривой структуры
        rename_all_by_select(
            soup,
            "h2.info-definition__title",
            "h4",
        )

        rename_all_by_select(soup, ".accordion__button > span", "h3")
```
И ура, мы написали парсер, который выполняет нужным нам функции!

## Multiple domains парсеры

Абсолютно такие же парсеры, как и "Domain парсеры", но у них в параметре `allowed_domains_paths` задаётся список не с одним элементом, а со множеством.

Пример:
```py
from ai_assistant_parsers_core.parsers import SimpleSelectDomainBaseParser


_ALLOWED_SUBDOMAINS_PATHS = [
    "students.spbu.ru",
    "nauka.spbu.ru",
    "mil.spbu.ru",
]


class TMContentParser(SimpleSelectDomainBaseParser):
    def __init__(self) -> None:
        super().__init__(
            allowed_domains_paths=_ALLOWED_SUBDOMAINS_PATHS,
            select_arguments=["#tm-content"],
        )
```

## Page парсеры

Такие же, как и "Domain парсеры", н вместо `allowed_domains_paths` требуют `allowed_paths`.

Пример:
```py
from ai_assistant_parsers_core.parsers import SimpleSelectPageBaseParser


class AbiturientMainPageParser(SimpleSelectPageBaseParser):
    def __init__(self) -> None:
        super().__init__(
            allowed_paths=["abiturient.spbu.ru/"],
            select_arguments=["main"],
        )
```

## Использование

## Пример проекта
