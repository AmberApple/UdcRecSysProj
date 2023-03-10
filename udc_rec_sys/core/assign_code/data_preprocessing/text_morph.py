import pymorphy2

from udc_rec_sys.core.variables import pm2_morph_analyzer_lang as pm2_lang

lang_morph = pymorphy2.MorphAnalyzer(lang=pm2_lang)


def get_morph_text(*, text: str) -> str:
    """
    Function starts the lemmatization process for each term in the list using the pymorphy2 library.
    """
    text_tokens = text.split()
    pm2_data = []
    for unit in text_tokens:
        pm2_result = lang_morph.parse(unit)[0]
        pm2_data.append(pm2_result.normal_form)

    morph_text = ' '.join(w for w in pm2_data).strip()
    return morph_text
