import re

from bs4 import BeautifulSoup, Tag, NavigableString
from ai_assistant_parsers_core.magic_url import MagicURL
from ai_assistant_parsers_core.refiners import ABCParsingRefiner


_MAIL_TEXT_WITH_OLD_PROTECTION = re.compile(
    "Этот адрес электронной почты защищен от спам-ботов. У вас должен быть включен JavaScript для просмотра."
)
_PROTECTED_MAIL_REPLACE_TEXT = "[Не удалось получить электронную почту]"


class HideProtectedMailsParsingRefiner(ABCParsingRefiner):
    def refine(self, soup: BeautifulSoup, magic_url: MagicURL) -> None:
        # Cloak protection
        for cloak_tag in soup.select('span[id^="cloak"]'):
            if not isinstance(cloak_tag, Tag):
                continue

            cloak_tag.string = _PROTECTED_MAIL_REPLACE_TEXT

        # Old protection
        for string in soup.find_all(string=_MAIL_TEXT_WITH_OLD_PROTECTION):
            if not isinstance(string, NavigableString):
                continue

            string.replace_with(_PROTECTED_MAIL_REPLACE_TEXT)
