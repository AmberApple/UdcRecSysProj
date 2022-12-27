from udc_rec_sys.core.assign_code.data_extraction.parse_OCR import get_file_text_with_ocr
from udc_rec_sys.core.assign_code.data_preprocessing.text_preprocessing import get_text_after_preprocessing
from udc_rec_sys.core.assign_code.data_generation.create_json_map import get_article_map
from udc_rec_sys.core.assign_code.data_evaluation.proximity_score import get_score

from udc_rec_sys.core.orm_manipulation.update_article_orm_record import update_record


def start_assign_code(*, path_to_pdf_file: str) -> None:
    """
    Function preprocesses the text of the article and calculates the recommended UDC code.
    """
    article_text = get_file_text_with_ocr(path_to_pdf=path_to_pdf_file)
    clear_article_text = get_text_after_preprocessing(article_text=article_text)
    article_json = get_article_map(article_text=clear_article_text)
    result_score_dict = get_score(article_map=article_json)

    update_record(path_to_article=path_to_pdf_file, article_json=article_json, result_dict=result_score_dict)

