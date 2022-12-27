from udc_rec_sys.models import OntologyTable
from udc_rec_sys.models import UdcTable

from udc_rec_sys.core.variables import ontology_main_id_ontomathpro
from udc_rec_sys.core.service.json_worker import get_json_string_as_object


def get_main_ontomathpro_data():
    ontology = OntologyTable.objects.get(id=ontology_main_id_ontomathpro)
    return get_json_string_as_object(json_string=ontology.data), ontology.domain


def get_udc_maps():
    return UdcTable.objects.all()
