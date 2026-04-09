from newspaper import Article, Config


def extract_article(url: str) -> str:
    config = Config()
    config.browser_user_agent = (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
    )
    article = Article(url, config=config)
    article.download()
    article.parse()
    return article.text
