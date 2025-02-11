import re

from bs4 import BeautifulSoup, Tag
from ai_assistant_parsers_core.magic_url import MagicURL
from ai_assistant_parsers_core.refiners import ABCParsingRefiner


_STYLE_TAGS_REGEX = re.compile(r"""
^(?:
    h[1-6]         # Заголовки h1-h6
    | strong       # Жирный текст (строгий)
    | b            # Жирный текст
    | i            # Курсив
    | em           # Выделение (обычно курсив)
    | mark         # Выделение маркером
    | small        # Мелкий текст
    | del          # Удаленный текст
    | ins          # Вставленный текст
    | sub          # Нижний индекс
    | sup          # Верхний индекс
    | u            # Невыраженная аннотация (Волнистое подчеркивание).
)$
""", flags=re.VERBOSE)


class CleanEmptyTagsParsingRefiner(ABCParsingRefiner):
    def refine(self, soup: BeautifulSoup, magic_url: MagicURL) -> None:
        _clean_empty_style_tags(soup)
        _clean_empty_list_items(soup)


def _clean_empty_style_tags(soup: BeautifulSoup):
    style_tags = soup.find_all(_STYLE_TAGS_REGEX)
    for tag in style_tags.copy():
        content = _get_tag_text_without_spaces(tag)
        if not content:
            tag.decompose()


def _clean_empty_list_items(soup: BeautifulSoup):
    tags = soup.find_all("li")
    for tag in tags.copy():
        content = _get_tag_text_without_spaces(tag)
        if not content:
            tag.decompose()


def _get_tag_text_without_spaces(tag: Tag) -> str:
    return re.sub(r"\s", "", tag.get_text())
