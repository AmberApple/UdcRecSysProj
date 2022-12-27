from udcrec.celery import app

from udc_rec_sys.models import Article, ArticleStatus

from udc_rec_sys.core.service.upload_data_to_db import upload_udcmaps_to_db_udctable
from udc_rec_sys.core.service.upload_data_to_db import upload_ontology_to_db_ontologytable
from udc_rec_sys.core.assign_code.assign_udc_code import start_assign_code

from django.utils import timezone
import logging
logger = logging.getLogger(__name__)


@app.task
def def_task(x, y):
    """
    Test task to check the performance of Celery.
    x + y
    """
    return x + y


@app.task
def upload_udc_map():
    """
    Task for manual loading of UDC maps to RecSys Data Base from core/service/data/udc_map/ .
    """
    upload_udcmaps_to_db_udctable()


@app.task
def upload_ontology():
    """
    Task for manual loading of Ontologies to RecSys Data Base from core/service/data/ontology/ .
    """
    upload_ontology_to_db_ontologytable()


@app.task
def assign_udc_code(*, pdf_file: str) -> None:
    """
    Task of assigning the UDC code of the article that the user has uploaded.
    Default start at views.article_upload().

    Return:
        Success -> Update article record and article status;
        Failed -> Set article status to "Error".
    """
    try:
        # update record info
        article_record = Article.objects.get(file=pdf_file)
        article_record.status = ArticleStatus(id=2)  # Processing
        article_record.save()

        # check file format
        check_pdf_format = pdf_file.split('/')[-1].split('.')[-1]
        if check_pdf_format != 'pdf':
            raise NameError('Not PDF')

        # start task
        start_assign_code(path_to_pdf_file=pdf_file)
        msg = f'{timezone.now()} | User {article_record.owner.username} | Article {pdf_file} | SUCCESS'
        logger.debug(msg)
    except Exception as exc:
        msg = f'{timezone.now()} | User {article_record.owner.username} | Article {pdf_file} | {str(exc)}'
        logger.debug(msg)
        # update record info
        article_record = Article.objects.get(file=pdf_file)
        article_record.status = ArticleStatus(id=4)  # Error
        article_record.save()
