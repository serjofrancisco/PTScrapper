from requests import get, ReadTimeout
import time
from parsel import Selector
from tech_news.database import create_news


# Requisito 1
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
    url = selector.css("link[rel=canonical]::attr(href)").get()
    title = selector.css("h1.entry-title::text").get().rstrip()
    timestamp = selector.css("li.meta-date::text").get()
    writer = selector.css("li.meta-author a::text").get()
    comments_count = selector.css("h5.title-block::text").re_first(r"\d") or 0
    summary = selector.xpath("string(//p)").get().rstrip()
    tags = selector.css(".post-tags li a::text").getall()
    category = selector.css("a.category-style span.label::text").get()

    return {
        "url": url,
        "title": title,
        "timestamp": timestamp,
        "writer": writer,
        "comments_count": comments_count,
        "summary": summary,
        "tags": tags,
        "category": category
    }


# Requisito 5
def get_tech_news(amount):
    tech_news = []
    url = "https://blog.betrybe.com/"
    while len(tech_news) < amount:
        html_content = fetch(url)
        news_urls = scrape_novidades(html_content)
        for news_url in news_urls:
            if len(tech_news) < amount:
                tech_news.append(scrape_noticia(fetch(news_url)))
        url = scrape_next_page_link(html_content)
    create_news(tech_news)
    return tech_news
