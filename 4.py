class Transport:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def get_info(self):
        return f"Марка: {self.brand}, Модель: {self.model}, Рік: {self.year}"

class Car(Transport):
    def __init__(self, brand, model, year, passenger_count):
        super().__init__(brand, model, year)
        self.passenger_count = passenger_count

    def get_passenger_capacity(self):
        return self.passenger_count

    def get_info(self):
        base_info = super().get_info()
        return f"{base_info}, Пасажирів: {self.passenger_count}"

class Truck(Transport):
    def __init__(self, brand, model, year, cargo_capacity):
        super().__init__(brand, model, year)
        self.cargo_capacity = cargo_capacity

    def get_cargo_capacity(self):
        return self.cargo_capacity

    def get_info(self):
        base_info = super().get_info()
        return f"{base_info}, Вантажопідйомність: {self.cargo_capacity} тонн"

class Bike(Transport):
    def __init__(self, brand, model, year, engine_volume):
        super().__init__(brand, model, year)
        self.engine_volume = engine_volume

    def get_engine_volume(self):
        return self.engine_volume

    def get_info(self):
        base_info = super().get_info()
        return f"{base_info}, Об'єм двигуна: {self.engine_volume} куб.см"

def input_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Будь ласка, введіть ціле число.")

def input_float(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Будь ласка, введіть число.")

def create_car():
    brand = input("Введіть марку автомобіля: ")
    model = input("Введіть модель автомобіля: ")
    year = input_int("Введіть рік випуску: ")
    passenger_count = input_int("Введіть кількість пасажирів: ")
    return Car(brand, model, year, passenger_count)

def create_truck():
    brand = input("Введіть марку вантажівки: ")
    model = input("Введіть модель вантажівки: ")
    year = input_int("Введіть рік випуску: ")
    cargo_capacity = input_float("Введіть вантажопідйомність (тонн): ")
    return Truck(brand, model, year, cargo_capacity)

def create_bike():
    brand = input("Введіть марку мотоцикла: ")
    model = input("Введіть модель мотоцикла: ")
    year = input_int("Введіть рік випуску: ")
    engine_volume = input_float("Введіть об'єм двигуна (куб.см): ")
    return Bike(brand, model, year, engine_volume)

def menu():
    vehicles = []
    while True:
        print("\n--- Меню ---")
        print("1. Додати автомобіль")
        print("2. Додати вантажівку")
        print("3. Додати мотоцикл")
        print("4. Показати всі транспортні засоби")
        print("5. Вийти")

        choice = input("Оберіть пункт меню: ")

        if choice == "1":
            car = create_car()
            vehicles.append(car)
            print("Автомобіль додано.")

        elif choice == "2":
            truck = create_truck()
            vehicles.append(truck)
            print("Вантажівку додано.")

        elif choice == "3":
            bike = create_bike()
            vehicles.append(bike)
            print("Мотоцикл додано.")

        elif choice == "4":
            if not vehicles:
                print("Список транспортних засобів порожній.")
            else:
                for i, v in enumerate(vehicles, 1):
                    print(f"{i}. {v.get_info()}")

        elif choice == "5":
            print("Вихід з програми.")
            break

        else:
            print("Невірний вибір. Спробуйте ще раз.")

if __name__ == "__main__":
    menu()
