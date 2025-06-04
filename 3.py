class Car:
    def __init__(self, brand="Unknown", model="Unknown", year=0, mileage=0.0):
        self.brand = brand
        self.model = model
        self.year = year
        self.mileage = mileage

    def get_info(self):
        return f"Марка: {self.brand}, Модель: {self.model}, Рік: {self.year}, Пробіг: {self.mileage} км"

    def copy(self):
        return Car(self.brand, self.model, self.year, self.mileage)

    def __del__(self):
        print(f"Автомобіль {self.brand} {self.model} видалено з пам'яті.")

def read_car_data():
    brand = input("Введіть марку автомобіля: ")
    model = input("Введіть модель автомобіля: ")
    while True:
        try:
            year = int(input("Введіть рік випуску: "))
            break
        except ValueError:
            print("Помилка! Введіть ціле число для року.")
    while True:
        try:
            mileage = float(input("Введіть пробіг (км): "))
            break
        except ValueError:
            print("Помилка! Введіть число для пробігу.")
    return brand, model, year, mileage

def menu():
    cars = []
    while True:
        print("\n--- Меню ---")
        print("1. Створити автомобіль (стандартний конструктор)")
        print("2. Створити автомобіль (параметризований конструктор)")
        print("3. Створити автомобіль (копіювальний конструктор)")
        print("4. Показати інформацію про всі автомобілі")
        print("5. Видалити автомобіль")
        print("6. Вийти")

        choice = input("Оберіть пункт меню: ")

        if choice == "1":
            car = Car()
            cars.append(car)

        elif choice == "2":
            brand, model, year, mileage = read_car_data()
            car = Car(brand, model, year, mileage)
            cars.append(car)

        elif choice == "3":
            if not cars:
                print("Спочатку створіть хоча б один автомобіль, щоб його копіювати!")
            else:
                print("Оберіть автомобіль для копіювання:")
                for i, car in enumerate(cars):
                    print(f"{i+1}. {car.get_info()}")
                while True:
                    try:
                        idx = int(input("Номер автомобіля: ")) - 1
                        if 0 <= idx < len(cars):
                            break
                        else:
                            print("Неправильний номер.")
                    except ValueError:
                        print("Введіть число.")
                new_car = cars[idx].copy()
                cars.append(new_car)

        elif choice == "4":
            if not cars:
                print("Автомобілі відсутні.")
            else:
                print("\nІнформація про всі автомобілі:")
                for i, car in enumerate(cars):
                    print(f"{i+1}. {car.get_info()}")

        elif choice == "5":
            if not cars:
                print("Автомобілі відсутні, нічого видаляти.")
            else:
                print("Оберіть автомобіль для видалення:")
                for i, car in enumerate(cars):
                    print(f"{i+1}. {car.get_info()}")
                while True:
                    try:
                        idx = int(input("Номер автомобіля: ")) - 1
                        if 0 <= idx < len(cars):
                            break
                        else:
                            print("Неправильний номер.")
                    except ValueError:
                        print("Введіть число.")
                car_to_delete = cars.pop(idx)
                del car_to_delete  

        elif choice == "6":
            print("Вихід з програми...")
            break

        else:
            print("Невірний вибір, спробуйте ще раз.")

if __name__ == "__main__":
    menu()
