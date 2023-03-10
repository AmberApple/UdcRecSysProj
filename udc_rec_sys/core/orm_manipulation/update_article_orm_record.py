from udc_rec_sys.models import Article, ArticleStatus

from udc_rec_sys.core.variables import top_result_counter
from udc_rec_sys.core.service.json_worker import get_json_object_as_string


def update_record(*, path_to_article: str, article_json: dict, result_dict: dict) -> None:
    """
    Function saves the article map to the media folder and writes the article classification data
    to the database via ORM, displaying the top 3 ratings.
    """
    sorted_score = dict(sorted(result_dict.items(), key=lambda item: item[1]))
    keys = list(sorted_score.keys())

    article_record = Article.objects.get(file=path_to_article)
    article_record.file_structure = get_json_object_as_string(json_object=article_json)
    article_record.status = ArticleStatus(id=3)

    main_udc_code = ''
    other_udc_code = ''
    for i in range(top_result_counter):
        if i == 0:
            main_udc_code += f'{keys[i]}'
        elif i == 1:
            other_udc_code += f'{keys[i]}'
        else:
            other_udc_code += f' | {keys[i]}'

    article_record.main_rec_udc = main_udc_code
    article_record.other_rec_udc = other_udc_code

    article_record.save()
