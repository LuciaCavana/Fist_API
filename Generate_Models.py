
           
class Person():
    person_id   =int         
    first_name  =str         
    last_name   =str          
    age         = int         
    hair_color  = str
    is_married  =bool         
    person_email=str    
    earnings    = float
    password    = str          
    
    def __init__(self, person_id, first_name,last_name,age, hair_color, is_married, person_email, earnings,password):
        self.person_id = person_id
        self.first_name= first_name
        self.last_name = last_name
        self.age = age
        self.hair_color = hair_color
        self.is_married = is_married
        self.person_email = person_email
        self.earnings = earnings
        self.password = password
               


           
def Create_person():
    person = Person(self,1, "Lucia","Cavana", 22,"brown", False, "luciacavana@yahoo.com",120000,"admin123" )
    print(person)
    return person

Create_person()