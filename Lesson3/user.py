class User:
    
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def SayFName(self):
        print(self.first_name)
        
    def SayLName(self):
        print(self.last_name)
        
    def SayFLName(self):
        print(self.first_name, self.last_name)
    
