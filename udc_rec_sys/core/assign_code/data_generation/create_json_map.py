import math

from udc_rec_sys.core.orm_manipulation.get_orm_data import get_main_ontomathpro_data
from udc_rec_sys.core.assign_code.data_preprocessing.text_morph import get_morph_text


import Levenshtein
# Coeff for Levenshtein distance
coefficient_mistake_lev = 0.85


def get_count_occurrences_of_term(*, term: str, text: str) -> int:
    """
    the function counts the number of occurrences of the term in the text of the article using the Levenshtein distance.
    The length of the ontology term is taken into account.
    """
    text = text.split()
    count_word_in_text = len(text)
    counter_term = 0
    count_word_in_term = len(term.split())

    for i in range(count_word_in_text):
        text_slice = []
        if i + count_word_in_term > count_word_in_text:
            text_slice = text[-count_word_in_term:]
        else:
            text_slice = text[i:i + count_word_in_term]

        slice_str = ' '.join(w for w in text_slice)

        slice_len = len(slice_str)
        term_len = len(term)
        count_mistakes_lev = math.ceil(term_len * (1 - coefficient_mistake_lev))

        if term_len - count_mistakes_lev <= slice_len <= term_len + count_mistakes_lev:
            replacement_count = Levenshtein.distance(term, slice_str)

            if replacement_count <= count_mistakes_lev:
                counter_term += 1

    return counter_term


def create_map(*, article_text: str, json_template: dict, onto_domain: str) -> dict:
    """
    Function counts the occurrence of each term of the ontology in the text of the article
    and enters the data into the JSON dict of the article.
    """
    article_json = json_template.copy()
    for exp_class in article_json.get(onto_domain):
        for dict_unit in article_json[onto_domain][exp_class]:
            name = dict_unit.get("name")
            term_pm2 = get_morph_text(text=name)
            count_occurrences = get_count_occurrences_of_term(term=term_pm2, text=article_text)
            dict_unit["count"] = count_occurrences

    return article_json


def get_article_map(*, article_text: str) -> dict:
    """
    Function extracts the terms of the ontology from the text of the article and forms the JSON dict of the article
    based on the structure of the ontology.
    """
    ontology_structure, ontology_domain = get_main_ontomathpro_data()
    article_json = create_map(article_text=article_text, json_template=ontology_structure, onto_domain=ontology_domain)

    return article_json
