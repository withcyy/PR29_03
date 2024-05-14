class ElectronicWallet:
    def __init__(self):
        self.__balance = 0

    def add_money(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Гроші у розмірі {amount} були успішно додані до гаманця.")
        else:
            print("Сума для додавання повинна бути більше 0.")

    def remove_money(self, amount):
        if amount > 0:
            if amount <= self.__balance:
                self.__balance -= amount
                print(f"Гроші у розмірі {amount} були успішно вилучені з гаманця.")
            else:
                print("Недостатньо коштів у гаманці.")
        else:
            print("Сума для вилучення повинна бути більше 0.")

    def check_balance(self):
        return self.__balance

wallet = ElectronicWallet()

wallet.add_money(100)
print("Поточний баланс:", wallet.check_balance())  # Виведе: Поточний баланс: 100

wallet.remove_money(50)
print("Поточний баланс:", wallet.check_balance())  # Виведе: Поточний баланс: