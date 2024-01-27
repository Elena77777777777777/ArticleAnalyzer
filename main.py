# main.py
from url_error import UrlError
from raw_page import RawPage
from page_content import PageContent
from extractor import Extractor
from page_analytics import PageAnalytics
if __name__ == "__main__":
    # Создание объектов RawPage для трех статей
    article_urls = [
        "https://en.wikipedia.org/wiki/Python_(programming_language)",
        "https://en.wikipedia.org/wiki/Machine_learning",
        "https://en.wikipedia.org/wiki/Data_science"
"https://en.wikipedia.org/wiki/Data_science"
from url_error import UrlError
from raw_page import RawPage
from page_content import PageContent  # Import PageContent here
from extractor import Extractor
from page_analytics import PageAnalytics

if __name__ == "__main__":
    # The rest of the code remains unchanged
# main.py
from url_error import UrlError
from raw_page import RawPage
from page_content import PageContent
from extractor import Extractor
from page_analytics import PageAnalytics

if __name__ == "__main__":
    # Создание объектов RawPage для трех статей
    article_urls = [
        "https://en.wikipedia.org/wiki/Python_(programming_language)",
        "https://en.wikipedia.org/wiki/Machine_learning",
        "https://en.wikipedia.org/wiki/Data_science"
    ]

    articles = []
    for url in article_urls:
        try:
            raw_page = RawPage(url)
            page_content = PageContent()
            extractor = Extractor()
            extractor.extract_sentences(raw_page, page_content)
            extractor.extract_words(raw_page, page_content)
            articles.append(PageAnalytics(page_content))
        except UrlError as e:
            print(f"Error processing URL {e.url}: {e}")

    # Анализ статей
    for article in articles:
        article.make_analytics()
        print(article)

    # Сравнение статей
    comparison_result = compare_articles(articles)
    print("\nComparison Result:")
    for key, value in comparison_result.items():
        print(f"{key}: {value}")
"https://en.wikipedia.org/wiki/Data_science"
"https://en.wikipedia.org/wiki/Data_science"

    ]

    articles = []
    for url in article_urls:
        try:
            raw_page = RawPage(url)
            page_content = PageContent()
            extractor = Extractor()
            extractor.extract_sentences(raw_page, page_content)
            extractor.extract_words(raw_page, page_content)from page_content import PageContent
from raw_page import RawPage
# main.py
from url_error import UrlError
from raw_page import RawPage
from page_content import PageContent  # Import PageContent here

# Rest of the code remains unchanged
# main.py
from url_error import UrlError
from raw_page import RawPage
from page_content import PageContent  # Import PageContent here

if __name__ == "__main__":
    # Rest of the code remains unchanged
# main.py
from url_error import UrlError
from raw_page import RawPage
from page_content import PageContent  # Import PageContent here
from extractor import Extractor  # Make sure to import the Extractor class as well

if __name__ == "__main__":
    # Rest of the code remains unchanged
# main.py
from url_error import UrlError
from raw_page import RawPage
from page_content import PageContent  # Import PageContent here
from extractor import Extractor  # Import Extractor here

if __name__ == "__main__":
    # Rest of the code remains unchanged

            articles.append(PageAnalytics(page_content))
        except UrlError as e:
            print(f"Error processing URL {e.url}: {e}")

    # Анализ статей
    for article in articles:
        article.make_analytics()
        print(article)

    # Сравнение статей
    comparison_result = compare_articles(articles)
    print("\nComparison Result:")
    for key, value in comparison_result.items():
        print(f"{key}: {value}")
