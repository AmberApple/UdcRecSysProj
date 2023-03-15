import os
import nltk

from udcrec.settings import BASE_DIR
from udcrec.settings import MEDIA_ROOT


# --- Check PATH ---
tesseract_cmd_path = r'/usr/bin/tesseract'
URS_CORE_ROOT = os.path.join(BASE_DIR, 'udc_rec_sys/core/')
path_to_ontology = os.path.join(URS_CORE_ROOT, "service/data/ontology/")
ontology_domain = "Mathematical knowledge object"
urs_swap_folder = os.path.join(MEDIA_ROOT, 'extraction_swap/')
path_to_udc_maps = os.path.join(URS_CORE_ROOT, "service/data/udc_map/")
nltk.data.path.append(os.path.join(URS_CORE_ROOT, 'service/nltk_data/'))

# --- Service vars ---
top_result_counter = 3
ontology_main_ver_ontomathpro = '1.12.16'
ontology_main_id_ontomathpro = 1
tesseract_ocr_slice_size = int(os.environ.get('TESS_OCR_SLICE_SIZE', default=10))
tesseract_ocr_dpi = int(os.environ.get('TESS_OCR_DPI', default=300))


default_expert_class_coefficients_dict = {
    "Value": 1,
    "Geometric object": 1,
    "Conjecture": 1,
    "Proof": 1,
    "Problem": 1,
    "Method": 1,
    "Set": 1,
    "Inequality": 1,
    "Operator": 1,
    "Operation": 1,
    "Definition": 1,
    "Map": 1,
    "Bound": 1,
    "Transformation": 1,
    "Identity": 1,
    "Tensor": 1,
    "Theorem": 1,
    "Equation": 1,
    "Statement": 1,
    "Formula": 1,
    "Property": 1,
    "Number": 1
}



