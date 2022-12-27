from udc_rec_sys.core.orm_manipulation.get_orm_data import get_main_ontomathpro_data
from udc_rec_sys.core.orm_manipulation.get_orm_data import get_udc_maps

from udc_rec_sys.core.service.json_worker import get_json_string_as_object

from scipy.spatial import distance
import numpy as np


def get_vector(*, json_file: dict, json_domain: str) -> list:
    """
    Function returns a normalized vector containing data about occurrences of each term.
    """
    vector = []
    for exp_class in json_file.get(json_domain):
        for unit in json_file[json_domain][exp_class]:
            vector.append(unit["count"])

    vector = np.array(vector)
    unit_vector = vector / np.linalg.norm(vector)

    return unit_vector


def get_score(*, article_map: dict) -> dict:
    """
    Function compares the article map and the UDC map using a cosine measure and returns the Dict{UDC_code: score_float}
    """
    _, ontology_domain = get_main_ontomathpro_data()
    article_score = {}
    article_vector = get_vector(json_file=article_map, json_domain=ontology_domain)
    for u_map in get_udc_maps():
        map_code = u_map.udc_code
        map_data = get_json_string_as_object(json_string=u_map.udc_map)
        map_vector = get_vector(json_file=map_data, json_domain=ontology_domain)
        distance_value = distance.cosine(article_vector, map_vector)
        article_score[map_code] = distance_value

    return article_score

