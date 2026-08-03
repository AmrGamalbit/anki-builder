from newspaper import Article, Config
from urllib.parse import urlparse, parse_qs
from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api._errors import InvalidVideoId
import re


ytt_api = YouTubeTranscriptApi()


def extract_content(url: str) -> str:
    if _is_youtube_url(url):
        return _extract_youtube_text(url)
    else:
        return _extract_article_text(url)


def _is_youtube_url(url: str) -> bool:
    parsed = urlparse(url)
    domain = parsed.netloc
    return "youtube.com" in domain or "youtu.be" in domain


def _extract_video_id(video_url: str) -> str:
    parsed = urlparse(video_url)
    query_v = parse_qs(parsed.query).get("v")
    if query_v:
        return query_v[0]
    path_parts = parsed.path.rstrip("/").split("/")
    if path_parts:
        return path_parts[-1]
    raise InvalidVideoId(video_url)


def _clean_transcript(text: str) -> str:
    # 1. Remove bracketed annotations like [Music] or (Laughter)
    text = re.sub(r"\([^)]*\)", "", text)
    text = re.sub(r"\[[^\]]*\]", "", text)

    # 2. Remove musical symbols
    text = re.sub(r"[♪♫]", "", text)

    # 3. Remove weird unicode symbols, but KEEP word characters, spaces, and punctuation
    text = re.sub(r"[^\w\s\.\,\!\?\'-]", "", text)

    # 4. Normalize multiple spaces/newlines into single spaces
    text = re.sub(r"\s+", " ", text)

    return text.strip()


def _extract_youtube_text(video_url: str) -> str:
    video_id = _extract_video_id(video_url)
    transcript = ytt_api.fetch(video_id)
    full_text = " ".join([snippet.text for snippet in transcript])
    text = _clean_transcript(full_text)
    return text


def _extract_article_text(url: str) -> str:
    config = Config()
    config.browser_user_agent = (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/124.0.0.0 Safari/537.36"
    )
    config.fetch_images = False
    config.memoize_articles = False
    article = Article(url, config=config)
    article.download()
    article.parse()
    print(article.text)
    return article.text
