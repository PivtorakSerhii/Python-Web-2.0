from abc import abstractmethod, ABC

class UserInterface(ABC):
    @abstractmethod
    def show_user_info(self):
        pass

class View(UserInterface):
    def __init__(self, name, phone, birth="", email="", status="", note=""):
        self.name = name
        self.phone = phone
        self.birth = birth
        self.email = email
        self.status = status
        self.note = note

    def separation(self):
        return 'x' * 50
    def show_user_info(self):
        return f"Name: {self.name}\nPhone: {self.phone}\nBirthday:{self.birth}\nEmail:{self.email}\nStatus:{self.status}\nNote:{self.note}"


user_1 = View('Alina', '067-111-88-99').show_user_info()


result = []
result.append(View('Alina', '067-111-88-99').show_user_info())
print(result)
