# page_content.py

class PageContent:
    """Представление содержимого страницы."""
    def __init__(self):
        self._sentences = []
        self._words = []

    @property
    def sentences(self):
        """Получение списка предложений."""
        return self._sentences

    @property
    def words(self):
        """Получение списка слов."""
        return self._words

    @sentences.setter
    def sentences(self, value):
        """Установка списка предложений."""
        self._sentences = value

    @words.setter
    def words(self, value):
        """Установка списка слов."""
        self._words = value
