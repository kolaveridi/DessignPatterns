class SingletonGoverment:
    __instance__=None
    
    
    def __init__(self):
        if SingletonGoverment.__instance__ is None:
            SingletonGoverment.__instance__=self
        else:
            raise Exception('You cannot create another singleton goverment class')
        
    @staticmethod
    def get_instance():
        if not SingletonGoverment.__instance__:
            SingletonGoverment()
        return SingletonGoverment.__instance__

print(SingletonGoverment.__instance__)  
goverment1 = SingletonGoverment()
goverment2 =SingletonGoverment.get_instance()
print(SingletonGoverment.__instance__)  
print(goverment1) 
print(goverment2)           
            
            