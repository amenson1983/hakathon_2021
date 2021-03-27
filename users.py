import sqlite3
import logging
server_local = "hakaton_base.db"




logging.basicConfig(filename='process_flow.log', level=logging.INFO, format='%(asctime)s %(message)s', datefmt='%d/%m/%Y %I:%M:%S %p')


class CUser:
    def __init__(self, surname,name,father_name,adress,phone):

        self.surname = surname
        self.name = name
        self.father_name = father_name
        self.adress = adress
        self.phone = phone
    def __str__(self):
        return f"Фамилия: {self.surname}\nИмя: {self.name}\nОтчество: {self.father_name}\nАдрес: {self.adress}\nТел.:{self.phone}"
class CDoctor():
    def __init__(self, surname,name,father_name,adress,phone,doc_speciality,hospital_name,hospital_adress,login,password):
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

class CCustomer:
    def __init__(self, surname,name,father_name,phone,id_number_or_passport):
        self.id_number_or_passport = id_number_or_passport
        self.surname = surname
        self.name = name
        self.father_name = father_name
        self.phone = phone
    def __str__(self):
        return f"Фамилия: {self.surname}\nИмя: {self.name}\nОтчество: {self.father_name}\nТел.:{self.phone}\nID: {self.id_number_or_passport}"

class CDoctor_workout:
    def get_logins_passwords_dict(self):
        with sqlite3.connect(server_local) as conn:
            cursor = conn.cursor()
            cursor.execute(
                f"select logins_passwords.login, logins_passwords.password from logins_passwords")
            results = cursor.fetchall()
            print(results)
    def registration(self,logins_dict,surname,name,father_name,adress,phone,doc_speciality,hospital_name,hospital_adress,login,password):
        x = CDoctor(surname,name,father_name,adress,phone,doc_speciality,hospital_name,hospital_adress,login,password)
        if x.login in logins_dict:
            print('try again')
        else: logins_dict.update({x.login:x.password})
        if x.login not in logins_dict:
            with sqlite3.connect(server_local) as conn:
                logging.info("Connecting to 'hakaton_base.db' - OK")
                cursor = conn.cursor()
                #cursor.execute("DROP TABLE logins_passwords")
                cursor.execute("CREATE TABLE IF NOT EXISTS logins_passwords (login,password);")
                logging.info("Creating the table 'logins_passwords' at 'hakaton_base.db' - OK")

                strin = [x.login,x.password]
                cursor.execute("INSERT INTO logins_passwords VALUES (?,?);",strin)
                conn.commit()
                logging.info("'logins_passwords'  - OK")


class Clogging:
    def __init__(self,login,password):
        self.login = login
        self.password = password

class Clogging_workout:
    def logging_to_system(self,login,password,logins_dict):
        if login in logins_dict:
            if password == logins_dict[password]:
                print('OK')
            else: print('Password is incorrect')
        else: print('No such user')




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
    #provisor = CProvisor(surname,name,father_name,adress,phone,id_card,pharmacy_name,pharmacy_adress)
    #print(provisor)
    #customer = CCustomer(surname,name,father_name,phone,id_card)
    #print(customer)
    logins_dict = {}
    doc_w = CDoctor_workout()
    doc_w.registration(logins_dict, surname, name, father_name, adress, phone, doc_speciality, hospital_name,
                 hospital_adress, login, password)
    doc_w.get_logins_passwords_dict()