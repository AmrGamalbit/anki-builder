from urllib.parse import urlparse, parse_qs
from youtube_transcript_api import YouTubeTranscriptApi
from nltk.corpus import stopwords
import re


ytt_api = YouTubeTranscriptApi()
cachedStopWords = stopwords.words("english")


def extract_video_id(video_url):
    u_pars = urlparse(video_url)
    quer_v = parse_qs(u_pars.query).get("v")
    if quer_v:
        return quer_v[0]
    pth = u_pars.path.split("/")
    if pth:
        return pth[-1]
    print("This is the path \n\n\n\n")
    print(pth)
    return pth


def clean_transcript(text):
    # Strip music cues, sound descriptions, and symbols from raw transcript
    text = re.sub(r"\([^)]*\)", "", text)  # remove (sound descriptions)
    text = re.sub(r"\[[^\]]*\]", "", text)  # remove [bracketed notes]
    text = re.sub(r"♪|♫", "", text)  # remove music symbols
    text = re.sub(
        r"[^\w\s\'-]", "", text
    )  # remove punctuation except hyphens and apostrophes
    text = re.sub(r"\s+", " ", text)  # normalize whitespace
    return text.strip()


def get_transcript(video_url):
    video_id = extract_video_id(video_url)
    transcript = ytt_api.fetch(video_id)
    full_text = " ".join([snippet.text for snippet in transcript])
    text = clean_transcript(full_text)
    # This was for removing duplicates & stopwords from the transcript
    # & but I changed my mind and thought it's better to keep it,
    # so  idioms and phrasal verbs can be detected in context

    # words = [w for w in words if w not in cachedStopWords]
    # words = list(dict.fromkeys(words))

    return " ".join(text)
