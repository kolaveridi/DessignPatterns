class PatientFilemanager:
    def __init__(self):
        self.patients={}
        
    def _add_patients(self,patient_id,data):
        self.patients[patient_id]=data
        
    def _get_patients(self,patient_id):
        return  self.patients[patient_id]
    
class AccessManager(PatientFilemanager):
    def __init__(self,filemanager):
        self.filemanager=filemanager
     
    def add_patients(self,patient_id,data,password):
        if password == 'sudo':
            self.filemanager._add_patients(patient_id,data)
        else:
            print("wrong password")
            
    def get_patients(self,patient_id,password):
        if password =='sudo':
            return self.filemanager._get_patients(patient_id)
        else:
            print ("Only doctors can access")   
            
am = AccessManager(PatientFilemanager())
am.add_patients('Jessica', ['pneumonia 2020-23-03', 'shortsighted'], 'sudo')

print(am.get_patients('Jessica', 'sudo'))
                  
            
            
            
          
        
                
            