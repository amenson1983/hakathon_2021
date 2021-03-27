

class CUser:
    def __init__(self,surname,name,father_name,adress,phone):
        self.surname = surname
        self.name = name
        self.father_name = father_name
        self.adress = adress
        self.phone = phone
    def __str__(self):
        return f"Фамилия: {self.surname}\nИмя: {self.name}\nОтчество: {self.father_name}\nАдрес: {self.adress}\nТел.:{self.phone}"
class CDoctor():
    def __init__(self,surname,name,father_name,adress,phone,doc_speciality,hospital_name,hospital_adress,login,password):
        self.password = password
        self.login = login
        self.hospital_adress = hospital_adress
        self.hospital_name = hospital_name
        self.doc_speciality = doc_speciality
        self.surname = surname
        self.name = name
        self.father_name = father_name
        self.adress = adress
        self.phone = phone
    def __str__(self):
        return f"Фамилия: {self.surname}\nИмя: {self.name}\nОтчество: {self.father_name}\nАдрес: {self.adress}\nТел.:{self.phone}\nСпециальность:{self.doc_speciality}\nГоспиталь:{self.hospital_name}\nГоспиталь:{self.hospital_adress}\nЛогин:{self.login}\nПароль:{self.password}"

class CProvisor:
    def __init__(self,surname,name,father_name,adress,phone,id_card,pharmacy_name,pharmacy_adress):
        self.pharmacy_adress = pharmacy_adress
        self.pharmacy_name = pharmacy_name
        self.id_card = id_card
        self.surname = surname
        self.name = name
        self.father_name = father_name
        self.adress = adress
        self.phone = phone

    def __str__(self):
        return f"Фамилия: {self.surname}\nИмя: {self.name}\nОтчество: {self.father_name}\nАдрес: {self.adress}\nТел.:{self.phone}\nID провизора:{self.id_card}\nАптека:{self.pharmacy_name}\nАптека адрес: {self.pharmacy_adress}"

#class CDoctor_workout:
    #def registration(self):
    #def login_to_system(self):


if __name__ == '__main__':
    surname = 'Турчин'
    name = "Андрей"
    father_name = "Викторович"
    adress = "Житомир, ул.Замковая, 1"
    phone  = "0989922947"
    login = "login"
    hospital_adress = "hospital_adress"
    hospital_name = "hospital_name"
    doc_speciality = "doc_speciality"
    password = "123"
    id_card = '444'
    pharmacy_name = 'Unknown'
    pharmacy_adress = 'Unknown'
    #user = CUser(surname,name,father_name,adress,phone)
    #print(user.__str__())
    #doc = CDoctor(surname,name,father_name,adress,phone,doc_speciality,hospital_name,hospital_adress,login,password)
    #print(doc)
    provisor = CProvisor(surname,name,father_name,adress,phone,id_card,pharmacy_name,pharmacy_adress)
    print(provisor)