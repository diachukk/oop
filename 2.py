import uuid

class BankAccount:
    def __init__(self, owner_name, balance):
        self.__account_number = self.__generate_account_number()
        self.__owner_name = None
        self.set_owner_name(owner_name)
        if not isinstance(balance, (int, float)) or balance < 0:
            raise ValueError("Початковий баланс має бути додатнім числом.")
        self.__balance = float(balance)

    def __generate_account_number(self):
        return str(uuid.uuid4())[:12].replace('-', '')

    def get_account_number(self):
        return self.__account_number

    def get_owner_name(self):
        return self.__owner_name

    def get_balance(self):
        return self.__balance

    def set_owner_name(self, new_name):
        if isinstance(new_name, str) and len(new_name.strip()) >= 3:
            self.__owner_name = new_name.strip()
        else:
            raise ValueError("Ім’я власника має бути не коротше 3 символів.")

    def deposit(self, amount):
        if not isinstance(amount, (int, float)) or amount <= 0:
            raise ValueError("Сума поповнення має бути додатнім числом.")
        self.__balance += amount

    def withdraw(self, amount):
        if not isinstance(amount, (int, float)) or amount <= 0:
            raise ValueError("Сума зняття має бути додатнім числом.")
        if amount > self.__balance:
            raise ValueError("Недостатньо коштів на рахунку.")
        self.__balance -= amount

try:
    name = input("Введіть ім’я власника рахунку: ")
    balance = float(input("Введіть початковий баланс: "))
    account = BankAccount(name, balance)
    print(f"Рахунок створено. Номер: {account.get_account_number()}, Баланс: {account.get_balance()}")

    while True:
        print("\nВиберіть дію:")
        print("1 — Поповнити рахунок")
        print("2 — Зняти кошти")
        print("3 — Переглянути баланс")
        print("4 — Змінити ім’я власника")
        print("0 — Вихід")
        choice = input("Ваш вибір: ")

        if choice == "1":
            amt = float(input("Сума для поповнення: "))
            account.deposit(amt)
            print("Баланс оновлено.")
        elif choice == "2":
            amt = float(input("Сума для зняття: "))
            account.withdraw(amt)
            print("Кошти знято.")
        elif choice == "3":
            print(f"Поточний баланс: {account.get_balance()}")
        elif choice == "4":
            new_name = input("Нове ім’я власника: ")
            account.set_owner_name(new_name)
            print("Ім’я змінено.")
        elif choice == "0":
            print("Вихід з програми.")
            break
        else:
            print("Невідома команда.")

except Exception as e:
    print("Помилка:", e)
