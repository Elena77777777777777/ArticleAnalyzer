# extractor.py
from bs4 import BeautifulSoup

class Extractor:
    """Извлечение предложений и слов из необработанной страницы."""
    @staticmethod
    def extract_sentences(raw_page, page_content):
        """Извлечение предложений и сохранение в объекте PageContent."""
        soup = BeautifulSoup(raw_page.data, 'html.parser')
        sentences = [sentence.text for sentence in soup.find_all('p')]
        page_content.sentences = sentences

    @staticmethod
    def extract_words(raw_page, page_content):
        """Извлечение слов и сохранение в объекте PageContent."""
        words = []
        for sentence in page_content.sentences:
            words.extend(sentence.split())
        page_content.words = words
