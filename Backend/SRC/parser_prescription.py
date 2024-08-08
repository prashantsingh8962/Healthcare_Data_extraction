import re
from parser_generic import MedicalDocParser
class PrescriptionParser(MedicalDocParser):
    def __init__(self, text):
        MedicalDocParser.__init__(self, text)

    # def parse(self):
    #     return{
    #         'patient_name': self.get_name(),
    #         'patient_address': self.get_address(),
    #         'medicines': self.get_medicine(),
    #         'Directions': self.get_Directions(),
    #         'refill': self.get_refill()
    #     }

#code refractoring
    def parse(self):
        return {
            'patient_name': self.get_field('patient_name'),
            'patient_address': self.get_field('patient_address'),
            'medicines': self.get_field('medicines'),
            'Directions': self.get_field('Directions'),
            'refills': self.get_field('refills')
        }

#u can use tuple or dictionary to make this compact
    def get_field(self, field_name):
        pattern_dict = {
            'patient_name': {'pattern': 'Name:(.*)Date', 'flags': 0},
            'patient_address': {'pattern': 'Address:(.*)\n', 'flags': 0},
            'medicines': {'pattern': "Address:[^P]*(.*)Directions", 'flags': re.DOTALL},
            'directions': {'pattern': 'Directions:(.*)Refill', 'flags': re.DOTALL},
            'refills': {'pattern': 'Refill:(.*)times', 'flags': 0},
        }

        pattern_object = pattern_dict.get(field_name)
        if pattern_object:
            matches = re.findall(pattern_object['pattern'], self.text, flags=pattern_object['flags'])
            if len(matches) > 0:
                return matches[0].strip()
        return ''


#WAY OF USING IF>>>ELSE MANY TIMES=====>
    # def get_filed(self, field_name):
    #     pattern=''
    #     if field_name == 'patient_name':
    #         pattern='Name:(.*)Date'
    #     elif field_name == 'patient_address':
    #         pattern= "Address:(.*)\n"

#LONG WAY====>
    # def get_name(self):
    #     pattern ='Name:(.*)Date'
    #     matches = re.findall(pattern, self.text)
    #     if len(matches)>0:
    #         return matches[0].strip()
    #
    # def get_address(self):
    #     pattern ="Address:(.*)\n"
    #     matches = re.findall(pattern, self.text)
    #     if len(matches)>0:
    #         return matches[0].strip()
    #
    # def get_medicines(self):
    #     pattern ="Address:[^P]*(.*)Directions"
    #     matches = re.findall(pattern, self.text, flags=re.DOTALL)
    #     if len(matches)>0:
    #         return matches[0].strip()
    #
    # def get_Directions(self):
    #     pattern ="Directions:(.*)Refill"
    #     matches = re.findall(pattern, self.text, , flags=re.DOTALL)
    #     if len(matches)>0:
    #         return matches[0].strip()
    #
    # def get_refill(self):
    #     pattern ="Refill:(.*)times"
    #     matches = re.findall(pattern, self.text)
    #     if len(matches)>0:
    #         return matches[0].strip()





if __name__ == '__main__':
    document_text = '''Name: Marta Sharapova Date: 5/11/2022
Address: 9 tennis court, new Russia, DC
-—s-« Prednisone 20 mg
Lialda 2.4 gram

Directions:

Prednisone, Taper 5 mig every 3 days,
Finish in 2.5 weeks
Lialda - take 2 pill everyday for 1 month

Refill: 2 times
'''
    pp = PrescriptionParser(document_text)
    print(pp.parse())




