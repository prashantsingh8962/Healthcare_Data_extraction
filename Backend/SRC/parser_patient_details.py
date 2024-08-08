import re
from parser_generic import MedicalDocParser
class PatientDetailsParser(MedicalDocParser):
    def __init__(self, text):
        MedicalDocParser.__init__(self, text)



    def parse(self):
        return {
            'patient_name': self.get_patient_name(),
            'Phone_number': self.get_field('Phone_number'),
            'medical_problems': self.get_field('medical_problems'),
            'Hepatitis_b_vaccination': self.get_field('Hepatitis_b_vaccination'),
        }

    def get_patient_name(self):
        pattern = 'Patient Information(.*?)\(\d{3}\)'
        matches = re.findall(pattern, text, flags=re.DOTALL)
        name =''
        if matches:
            self.remove_noise_from_name(matches[0])
        return name

    def remove_noise_from_name(self,name):
        name = name.replace("Birth Date", "").strip()
        date_pattern = '((Jan|Feb|Mar|Apr|May|June|July|Aug|Sep|Oct|Nov|Dec)[ \d]+)'
        date_matches = re.findall(date_pattern, name)

        if date_matches:
            date = date_matches[0][0]
            name = name.replace(date, '').strip()
        return name