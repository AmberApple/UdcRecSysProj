import os

from PIL import Image
import pytesseract
from pdf2image import convert_from_path, pdfinfo_from_path

from udcrec.settings import MEDIA_ROOT
from udc_rec_sys.core.variables import urs_swap_folder as swap_path
from udc_rec_sys.core.variables import tesseract_cmd_path
from udc_rec_sys.core.variables import tesseract_ocr_slice_size as slice_size


pytesseract.pytesseract.tesseract_cmd = tesseract_cmd_path


def get_file_text_with_ocr(*, path_to_pdf: str) -> str:
    """
    Function extract text from PDF file using Tesseract OCR.
    PDF file is split into slices. The slices convert into photos that are recognized and then deleted.
    """
    pdf_name = path_to_pdf.split('/')[-1].split('.pdf')[0]
    path_to_pdf = os.path.join(MEDIA_ROOT, path_to_pdf)
    pdf_info = pdfinfo_from_path(pdf_path=path_to_pdf)
    pages_in_pdf = pdf_info['Pages']
    file_text = ''

    if not os.path.exists(swap_path):
        os.mkdir(swap_path)

    for file_page in range(1, pages_in_pdf + 1, slice_size):
        pdf_slice = convert_from_path(pdf_path=path_to_pdf, dpi=300, first_page=file_page,
                                      last_page=min(file_page + slice_size - 1, pages_in_pdf))
        image_counter = 1
        jpeg_for_delete = []
        for page in pdf_slice:
            filename = swap_path + pdf_name + '_page_' + str(image_counter) + '.jpg'
            page.save(filename, 'JPEG')
            jpeg_for_delete.append(filename)
            image_counter += 1

        start_page = 1
        text_page_limit = image_counter - 1
        for page_number in range(start_page, text_page_limit + 1):
            filename = swap_path + pdf_name + '_page_' + str(page_number) + '.jpg'
            text = str(pytesseract.image_to_string(Image.open(filename), lang='rus'))
            text = text.replace('-\n', '')
            file_text += text

        for jpeg in jpeg_for_delete:
            os.remove(jpeg)

    return file_text
