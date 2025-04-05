from bs4 import BeautifulSoup
import re
from crawl import crawl_vnexpress_ai  # Import từ file chính

def clean_html(raw_text):
    """
    Loại bỏ thẻ HTML và làm sạch khoảng trắng thừa.
    """
    if not raw_text:
        return ""
    
    text = BeautifulSoup(raw_text, "html.parser").get_text()
    text = re.sub(r'\s+', ' ', text).strip()
    return text

def clean_articles_data(raw_articles):
    """
    Nhận danh sách bài viết dạng dict, làm sạch và trả về danh sách mới.
    """
    cleaned = []
    for article in raw_articles:
        cleaned_article = {
            'title': clean_html(article.get('title')),
            'url': article.get('url').strip(),
            'summary': clean_html(article.get('summary')),
            'time': clean_html(article.get('time')),
            'author': clean_html(article.get('author')),
        }
        cleaned.append(cleaned_article)
    return cleaned

if __name__ == "__main__":
    raw_articles = crawl_vnexpress_ai()
    cleaned_articles = clean_articles_data(raw_articles)

    for i, article in enumerate(cleaned_articles, 1):
        print(f"📄 Article {i}:")
        print(f"Title  : {article['title']}")
        print(f"URL    : {article['url']}")
        print(f"Summary: {article['summary']}")
        print(f"Time   : {article['time']}")
        print(f"Author : {article['author']}")
        print("-" * 60)
