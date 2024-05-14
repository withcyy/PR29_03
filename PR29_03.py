class User:
    def __init__(self, name, age, email):
        self.__name = name
        self.__age = age
        self.__email = email

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def get_email(self):
        return self.__email

    def set_name(self, name):
        self.__name = name

    def set_age(self, age):
        self.__age = age

    def set_email(self, email):
        self.__email = email

user1 = User("Igor", 30, "igor123@gmail.com")

print("Ім'я користувача:", user1.get_name())
print("Вік користувача:", user1.get_age())
print("Email користувача:", user1.get_email())

user1.set_name("Oleg")
user1.set_age(25)
user1.set_email("oleg@gmail.com")

print("Нове ім'я користувача:", user1.get_name())
print("Новий вік користувача:", user1.get_age())
print("Новий email користувача:", user1.get_email())