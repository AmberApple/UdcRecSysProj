from udc_rec_sys.core.assign_code.data_preprocessing.text_cleaner import delete_wrong_characters
from udc_rec_sys.core.assign_code.data_preprocessing.text_cleaner import delete_stopwords
from udc_rec_sys.core.assign_code.data_preprocessing.text_morph import get_morph_text


def get_text_after_preprocessing(*, article_text: str) -> str:
    text = delete_wrong_characters(article_text=article_text)
    text = delete_stopwords(article_text=text)
    text = get_morph_text(text=text)

    return text
