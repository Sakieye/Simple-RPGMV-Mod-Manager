from unittest import TestCase

from mod_installer.src.language import Locale, Lang


class TestLang(TestCase):

    def test_construct(self):
        lang = Lang(loc=Locale.ZH_TW)
        assert (lang.language_pack is not None)

    def test_get_en(self):
        lang = Lang(loc=Locale.EN)
        assert (lang.get("welcome").startswith("Welcome"))

    def test_get_zh_tw(self):
        lang = Lang(loc=Locale.ZH_TW)
        assert (lang.get("welcome").startswith("歡迎"))

    def test_get_and_replace(self):
        lang = Lang(loc=Locale.EN)
        actual = lang.get_and_replace("cannot_find", {"file": "1", "root": "2"})
        assert ("cannot find '1' under '2'." == actual)
