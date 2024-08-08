import pytesseract
from pdf2image import convert_from_path

# given path of poppler for support of pdf2image module, path to tesseract engine'exe'
POPPLER_PATH = 'C:\\Users\\Prashant Singh\\OneDrive\\Documents\\Codebasics\\Python\\source-code\\4_project_medical_data_extraction\\poppler-24.07.0\\Library\\bin'
pytesseract.pytesseract.tesseract_cmd = 'C:\\Users\\Prashant Singh\\OneDrive\\Documents\\Codebasics\\Python\\source-code\\4_project_medical_data_extraction\\Tesseract\\tesseract.exe'


import Util  # Ensure this module is available and contains preprocess_image


# Define paths to Poppler and Tesseract executables

def extract(file_path, file_format):
    # Extract text from PDF file
    pages = convert_from_path(file_path, poppler_path=POPPLER_PATH)
    document_text = ''

    for page in pages:
        processed_image = Util.preprocess_image(page)
        text = pytesseract.image_to_string(processed_image, lang="eng")
        document_text += text + '\n'  # Concatenate text from all pages

    return document_text

    # if file_format == 'prescription':
    #     pass  # Extract data from prescription
    # elif file_format == 'patient_details':
    #     pass  # Extract data from patient_details
    # ctrl +'/' is used to comment selected block in python

if __name__ == '__main__':
    data = extract('../Resource/prescription/pre_1.pdf', 'prescription')
    print(data)
