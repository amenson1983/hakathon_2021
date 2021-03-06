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
    def __init__(self,surname,name,father_name,adress,phone,id_card,pharmacy_name,pharmacy_adress,login,password):
        self.password1 = password
        self.login1 = login
        self.pharmacy_adress1 = pharmacy_adress
        self.pharmacy_name1 = pharmacy_name
        self.id_card1 = id_card
        self.surname1 = surname
        self.name1 = name
        self.father_name1 = father_name
        self.adress1 = adress
        self.phone1 = phone

    def __str__(self):
        return f"Фамилия: {self.surname1}\nИмя: {self.name1}\nОтчество: {self.father_name1}\nАдрес: {self.adress1}\nТел.:{self.phone1}\nID провизора:{self.id_card1}\nАптека:{self.pharmacy_name1}\nАптека адрес: {self.pharmacy_adress1}"

class CCustomer:
    def __init__(self, surname,name,father_name,phone,id_number_or_passport):
        self.id_number_or_passport = id_number_or_passport
        self.surname = surname
        self.name = name
        self.father_name = father_name
        self.phone = phone
    def __str__(self):
        return f"Фамилия: {self.surname}\nИмя: {self.name}\nОтчество: {self.father_name}\nТел.:{self.phone}\nID: {self.id_number_or_passport}"
class CProvisor_workout():
    def get_logins_passwords_dict1(self):
        with sqlite3.connect(server_local) as conn:
            cursor = conn.cursor()

            cursor.execute(
                f"select logins_passwords_provisor.login1, logins_passwords_provisor.password1 from logins_passwords_provisor")
            results = cursor.fetchall()
            results_classifyed = {}
            for i in results:
                classif_string = Clogging1(i[0], i[1])
                results_classifyed.update({classif_string.login1:classif_string.password1})
            return results_classifyed

    def registration1(self,logins_dict1,surname1,name1,father_name1,adress1,phone1,id_card1,pharmacy_name1,pharmacy_adress1,login1,password1):
        x = CProvisor(surname1,name1,father_name1,adress1,phone1,id_card1,pharmacy_name1,pharmacy_adress1,login1,password1)



        if x.login1 not in logins_dict1:
            with sqlite3.connect(server_local) as conn:
                logins_dict1.update({x.login1: x.password1})
                logging.info("Connecting to 'hakaton_base.db' - OK")
                cursor = conn.cursor()
                #cursor.execute("DROP TABLE logins_passwords_provisor")
                cursor.execute("CREATE TABLE IF NOT EXISTS logins_passwords_provisor (login1,password1);")
                strin1 = [x.login1,x.password1]
                cursor.execute("INSERT INTO logins_passwords_provisor VALUES (?,?);",strin1)
                conn.commit()
                logging.info("'logins_passwords_provisor'  - OK")
        else: print('try again')
    def log_in_to_system1(self, login1, password1):
        prov = CProvisor_workout()
        logins_password_list_from_base1 = prov.get_logins_passwords_dict1()
        entering = Clogging_workout()
        status1 = entering.logging_to_system1(login1, password1, logins_password_list_from_base1)
        return status1

class CDoctor_cabinet:
    def enter_the_cabinet(self,login, password):
        doc_w = CDoctor_workout()
        doc_stat_ = doc_w.log_in_to_system(login, password)
        if doc_stat_ == True:
            print('OK Doc')
class CProvisor_cabinet:
    def enter_provisor_the_cabinet(self,login1, password1):
        doc_w = CProvisor_workout()
        doc_stat_ = doc_w.log_in_to_system1(login1, password1)
        if doc_stat_ == True:
            print('OK Provisor')
class CDoctor_workout:
    def get_logins_passwords_dict(self):
        with sqlite3.connect(server_local) as conn:
            cursor = conn.cursor()
            cursor.execute(
                f"select logins_passwords.login, logins_passwords.password from logins_passwords")
            results = cursor.fetchall()
            results_classifyed = {}
            for i in results:
                classif_string = Clogging(i[0], i[1])
                results_classifyed.update({classif_string.login:classif_string.password})
            return results_classifyed

    def registration(self,logins_dict,surname,name,father_name,adress,phone,doc_speciality,hospital_name,hospital_adress,login,password):
        x = CDoctor(surname,name,father_name,adress,phone,doc_speciality,hospital_name,hospital_adress,login,password)
        if x.login not in logins_dict:
            with sqlite3.connect(server_local) as conn:
                logins_dict.update({x.login: x.password})
                logging.info("Connecting to 'hakaton_base.db' - OK")
                cursor = conn.cursor()
                #cursor.execute("DROP TABLE logins_passwords")
                cursor.execute("CREATE TABLE IF NOT EXISTS logins_passwords (login,password);")
                strin = [x.login,x.password]
                cursor.execute("INSERT INTO logins_passwords VALUES (?,?);",strin)
                conn.commit()
                logging.info("'logins_passwords'  - OK")
        else: print('try again')
    def log_in_to_system(self, login, password):
        doc_w = CDoctor_workout()
        logins_password_list_from_base = doc_w.get_logins_passwords_dict()
        entering = Clogging_workout()
        status = entering.logging_to_system(login, password, logins_password_list_from_base)
        return status


class Clogging:
    def __init__(self,login,password):
        self.login = login
        self.password = password
class Clogging1:
    def __init__(self,login1,password1):
        self.login1 = login1
        self.password1 = password1

class Clogging_workout:
    def logging_to_system(self,login,password,logins_dict):
        if login in logins_dict:
            if str(password) == logins_dict[login]:
                return True
            else: return False
        else: return False
    def logging_to_system1(self,login1,password1,logins_dict):
        if login1 in logins_dict:
            if str(password1) == logins_dict[login1]:
                return True
            else: return False
        else: return False




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
    surname1 = 'Турчин1'
    name1 = "Андрей1"
    father_name1 = "Викторович1"
    adress1 = "Житомир, ул.Замковая, 11"
    phone1  = "09899229471"
    login1 = "login1"
    hospital_adress1 = "hospital_adress1"
    hospital_name1 = "hospital_name1"
    doc_speciality1 = "doc_speciality1"
    password1 = "1232"
    id_card1 = '4441'
    pharmacy_name1 = 'Unknown1'
    pharmacy_adress1 = 'Unknown1'
    #user = CUser(surname,name,father_name,adress,phone)
    doc_w = CDoctor_workout()
    logins_dict = doc_w.get_logins_passwords_dict()
    doc_w.registration(logins_dict, surname, name, father_name, adress, phone, doc_speciality, hospital_name,
                       hospital_adress, login, password)
    doc_stat_ = doc_w.log_in_to_system(login, password)

    prov = CProvisor_workout()


    #prov.registration1(logins_dict1,surname1,name1,father_name1,adress1,phone1,id_card1,pharmacy_name1,pharmacy_adress1,login1,password1)
    logins_dict1 = prov.get_logins_passwords_dict1()
    prov_stat = prov.log_in_to_system1(login1, password1)

    doc_enter = CDoctor_cabinet()
    doc_enter.enter_the_cabinet(login, password)
    prov_enter = CProvisor_cabinet()
    prov_enter.enter_provisor_the_cabinet(login1, password1)
    #