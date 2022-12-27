import os

from udc_rec_sys.models import UdcTable
from udc_rec_sys.models import OntologyTable

from udc_rec_sys.core.variables import default_expert_class_coefficients_dict as decc_dict
from udc_rec_sys.core.variables import path_to_udc_maps as path_to_map
from udc_rec_sys.core.variables import path_to_ontology
from udc_rec_sys.core.variables import ontology_domain

from udc_rec_sys.core.service.json_worker import get_object_from_json_file
from udc_rec_sys.core.service.json_worker import get_json_object_as_string


def start_upload() -> None:
    """
    Function generates an initial record for each created UDC map in DB UdcTable
    """
    # NEED REFACTOR
    for map_json in os.listdir(path_to_map):
        # UdcTable.objects.create(udc_code=map_json.split('.json')[0], name=map_json.split('.json')[0],
        #                       udc_map="udc_map/" + map_json, exp_class_coefficient=def_str)
        udc = UdcTable(udc_code=map_json.split('.json')[0], name=map_json.split('.json')[0],
                       udc_map="udc_map/" + map_json, exp_class_coefficient=str(decc_dict))
        udc.save()


def upload_udcmaps_to_db_udctable() -> None:
    """
    Function generate records for each created UDC map in DB UdcTable
    """
    for map_json in os.listdir(path_to_map):
        code = map_json.split('.json')[0]
        data = get_json_object_as_string(
            json_object=get_object_from_json_file(json_file=os.path.join(path_to_map, map_json)))
        coeff = str(decc_dict)

        udc_map = UdcTable(udc_code=code, udc_map=data, exp_class_coefficient=coeff)
        udc_map.save()


def upload_ontology_to_db_ontologytable() -> None:
    """
    Function generate records for each Ontology in DB OntologyTable
    """
    for ontology_json in os.listdir(path_to_ontology):
        name = ontology_json.split('_version')[0]
        domain = ontology_domain
        version = ontology_json.split('_version')[1].split('.json')[0]
        data = get_json_object_as_string(
            json_object=get_object_from_json_file(json_file=os.path.join(path_to_ontology, ontology_json)))

        ontology = OntologyTable(name=name, domain=domain, version=version, data=data)
        ontology.save()
