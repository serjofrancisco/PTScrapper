# Requisito 1
from requests import get, ReadTimeout
import time
from parsel import Selector


def fetch(url):
    headers = {"user-agent": "Fake user-agent"}
    timeout = 3

    try:
        response = get(url, timeout=timeout, headers=headers)
        time.sleep(1)
        if(response.status_code == 200):
            return response.text
        else:
            return None
    except ReadTimeout:
        return None


# Requisito 2
def scrape_novidades(html_content):
    selector = Selector(text=html_content)
    return selector.css("a.cs-overlay-link::attr(href)").getall()


# Requisito 3
def scrape_next_page_link(html_content):
    selector = Selector(text=html_content)
    return selector.css("a.next::attr(href)").get()


# Requisito 4
def scrape_noticia(html_content):
     selector = Selector(text=html_content)


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
