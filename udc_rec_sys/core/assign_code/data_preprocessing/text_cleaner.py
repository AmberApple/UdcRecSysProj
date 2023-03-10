import re
import nltk

#nltk.download('stopwords')
from nltk.corpus import stopwords


def delete_wrong_characters(*, article_text: str) -> str:
    """
    Function removes line breaks and carriage returns, characters other than Russian and English letters and numbers,
    extra spaces.
    """
    text_to_clean = re.sub(r'\r\n', '', article_text)
    clearable_text = text_to_clean.strip()
    clearable_text = re.sub(r"[^a-zA-Z0-9а-яА-ЯёЁ -]", ' ', clearable_text)
    clearable_text = re.sub(' +', ' ', clearable_text)

    clear_text = clearable_text
    return clear_text


def delete_stopwords(*, article_text: str) -> str:
    """
    Function removes the stop word from the text using the NLTK library.
    """
    text_tokens = article_text.split()
    text_without_sw = [word for word in text_tokens if not word in stopwords.words('russian')]

    text = ' '.join(w for w in text_without_sw)
    return text
