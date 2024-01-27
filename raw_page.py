# raw_page.py
import requests
from url_error import UrlError

class RawPage:
    """Представление необработанной страницы Википедии."""
    def __init__(self, url):
        self.url = url
        self._data = None
        self._headline = None

    @property
    def data(self):
        """Получение содержимого страницы, при необходимости загрузки."""
        if not self._data:
            self._download_page()
        return self._data

    @property
    def headline(self):
        """Получение заголовка страницы, при необходимости загрузки."""
        if not self._headline:
            self._download_page()
        return self._headline

    def _download_page(self):
        """Загрузка страницы и сохранение данных."""
        try:
            response = requests.get(self.url)
            response.raise_for_status()
            self._data = response.text
            self._headline = response.headers['Wikipedia-Page-Title']
        except requests.RequestException as e:
            raise UrlError(self.url)
