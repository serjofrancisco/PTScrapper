from ..database import search_news
from datetime import datetime


# Requisito 6
def search_by_title(title):
    news = search_news({"title": {'$regex': title, '$options': 'i'}})
    return [(query['title'], query['url']) for query in news]


# Requisito 7
def search_by_date(date):
    try:
        date_formated = datetime.fromisoformat(date).strftime("%d/%m/%Y")
        all_news = search_news({"timestamp": {"$eq": date_formated}})

        return [(news["title"], news["url"]) for news in all_news]
    except ValueError:
        raise ValueError("Data inválida")


# Requisito 8
def search_by_tag(tag):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
