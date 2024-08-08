from Backend.src.parser_generic import MedicalDocumentParser
import re
class PerscriptionParser(MedicalDocumentParser):
    def __init__(self, text):
        MedicalDocumentParser.__init__(self, text)

    #code refractoring
    def parse(self):
        return {
            'patient_name':self.get_filed('patient_name'),
            'patient_address':self.get_filed('patient_address'),
            'medicine':self.get_filed('medicine'),
            'directions':self.get_filed('directions'),
            'refill':self.get_filed('refill')
        }

    #u can use tuple or dictionary to make this code compact
    def get_filed(self, filed_name):
        pattern_dic ={
            "patient_name":{'pattern': 'Name:(.*)Date', 'flags':0},
            "patient_address": {'pattern': 'Address:(.*)\n', 'flags': 0},
            "medicine": {'pattern': 'Address:[^\n]*(.*)Directions', 'flags': re.DOTALL},
            "directions": {'pattern': 'Directions:(.*)Refill', 'flags': re.DOTALL},
            "refill": {'pattern': 'Refill:.*(\d+).times', 'flags': 0},
        }
        pattern_object = pattern_dic[filed_name]
        if pattern_object:
            matches = re.findall(pattern_object['pattern'], self.text, flags=pattern_object["flags"])
            if matches:
                return matches[0].strip()
        return ''


if __name__ == "__main__":
    text = '''Dr John >mith, M.D

2 Non-Important street,
New York, Phone (900)-323- ~2222

Name:  Virat Kohli Date: 2/05/2022

Address: 2 cricket blvd, New Delhi

| Omeprazole 40 mg

Directions: Use two tablets daily for three months

Refill: 3 times'''
    pp = PerscriptionParser(text)
    print(pp.parse())

       '
=======================================================================================================================

#WAY OF USING IF>>>ELSE MANY TIMES=====>
    # def get_filed(self, field_name):
    #     pattern=''
    #     if field_name == 'patient_name':
    #         pattern='Name:(.*)Date'
    #     elif field_name == 'patient_address':
    #         pattern= "Address:(.*)\n"

#LONG WAY====>
    # def parse(self):
    #     return{
    #         'patient_name': self.get_name(),
    #         'patient_address': self.get_address(),
    #         'medicines': self.get_medicine(),
    #         'Directions': self.get_Directions(),
    #         'refill': self.get_refill()
    #     }
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
