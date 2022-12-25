id_person = {
    1:{
        "name":"Lucia", 
        "age":22
        },
    2:{
        "name":"Matias",
        "age":17
        },
    3:{
        "name":"Fernando", 
        "age":40
        },
    4:{
        "name":"Martina", 
        "age":20
        },
    5:{
        "name":"Lucila", 
        "age":50
        },
}

def show_person():
    person_id = 1
    if person_id not in id_person:
        return {"HTTP_404_NOT_FOUND":"¡This person doesn't exist!"}
    
    dic = dict(id_person[person_id])
    name = dict(id_person[person_id])["name"]
    age = dict(id_person[person_id])["age"]
    print(name)
    print(age)
    print({dic["name"]:dic["age"]})

show_person()