

class CUser:
    def __init__(self,surname,name,father_name,adress,phone):
        self.surname = surname
        self.name = name
        self.father_name = father_name
        self.adress = adress
        self.phone = phone
    def __str__(self):
        return f"Фамилия: {self.surname}\nИмя: {self.name}\nОтчество: {self.father_name}\nАдрес: {self.adress}\nТел.:{self.phone}"
#class CDoctor(CUser):



if __name__ == '__main__':
    surname = 'Турчин'
    name = "Андрей"
    father_name = "Викторович"
    adress = "Житомир, ул.Замковая, 1"
    phone  = "0989922947"
    x = CUser(surname,name,father_name,adress,phone)
    print(x.__str__())
