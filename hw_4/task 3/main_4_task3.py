from __future__ import annotations
# task 3

class Dealership:

    def __init__(self, list_cars: list[Car] = None, list_salesperson: list[Salesperson] = None, list_customers: list[Customer] = None):
        self.__list_cars = list_cars
        self.__list_salesperson = list_salesperson
        self.__list_customers = list_customers

    def add_car(self, car: Car):
        self.__list_cars.append(car)

    def add_salesperson(self, salesperson: Salesperson):
        self.__list_salesperson.append(salesperson)


    def add_customer(self, customer: Customer):
        self.__list_customers.append(customer)

    def remove_car(self, car: Car):
        self.__list_cars.remove(car)

    def remove_salesperson(self, salesperson: Salesperson):
        self.__list_customers.remove(salesperson)

    def get_list_cars(self):
        return self.__list_cars

    def get_list_customers(self):
        return self.__list_customers

    def get_list_salesperson(self):
        return self.__list_salesperson


    def __str__(self):
        return f'Cars: {", ".join(str(i.get_brand() +" "+ i.get_model()) for i in self.__list_cars)}\n' \
               f'Customers: {", ".join(str(i.get_name()) for i in self.__list_customers)}\n' \
               f'Salesperson: {", ".join(str(i.get_name()) for i in self.__list_salesperson)}\n'

class Salesperson:

    def __init__(self, name: str, work_experience: float, list_sold_cars: list[Car] = None):
        self.__name = name
        self.__work_experience = work_experience
        self.__list_sold_cars = list_sold_cars

    def get_name(self):
        return self.__name

    def get_list_sold_car(self):
        return self.__list_sold_cars

    def add_sold_car(self, car: Car):
        self.__list_sold_cars.append(car)

    def remove_sold_car(self, car):
        self.__list_sold_cars.remove(car)

    def __str__(self):
        return f'Name: {self.__name}\n' \
               f'Work Experience: {self.__work_experience}\n' \
               f'List sold cars: {self.__list_sold_cars}\n'

class Car:

    def __init__(self, brand: str, model: str, year: int, price: float, status: str) -> object:
        self.__brand = brand
        self.__model = model
        self.__year = year
        self.__price = price
        self.__status = status

    def get_brand(self):
        return self.__brand

    def get_model(self):
        return self.__model

    def get_year(self):
        return self.__year

    def get_price(self):
        return self.__price

    def get_status(self):
        return self.__status

    def set_price(self, price):
        self.__price = price

    def set_status(self, status):
        self.__status = status

    def __str__(self):
        return f'Brand: {self.__brand}\n' \
               f'Model: {self.__model}\n' \
               f'Year: {self.__year}\n' \
               f'Price: {self.__price}\n' \
               f'Status: {self.__status}\n'

class Customer:

    def __init__(self, name: str, phone_number: str, email: str, list_cars: list[Car] = None) -> object:
        self.__name = name
        self.__phone_number = phone_number
        self.__email = email

        if not (list_cars is None):
            self.__list_cars = list_cars
        else:
            self.__list_cars = []

    def get_name(self):
        return self.__name

    def get_phone_number(self):
        return self.__phone_number

    def get_email(self):
        return self.__email

    def get_list_cars(self):
        return self.__list_cars

    def set_phone_number(self, phone_number):
        self.__phone_number = phone_number

    def set_email(self, email):
        self.__email = email

    def add_car(self, car):
        self.__list_cars.append(car)

    def remove_car(self, car):
        self.__list_cars.remove(car)

    def __str__(self):
        return f'Name: {self.__name}\n' \
               f'Phone_number: {self.__phone_number}\n' \
               f'Email: {self.__email}\n' \
               f'List cars: {", ".join(str(i.get_brand() + " " + i.get_model()) for i in self.__list_cars)}\n'


class Program:

    @staticmethod
    def main():
        car1 = Car('Nissan', 'Skyline', 1995, 19255.50, 'в наличии')
        car2 = Car('Vaz', '2101', 1990, 100, 'в наличии')
        customer1 = Customer('Ivan', '80808080', 'qwe@qwe.qwe', [car1])
        customer2 = Customer('Sasha', '812340', 'asd@asd.asd', [car1, car2])
        salerperson1 = Salesperson('Aleks', 3.5, [car1])
        dealership1 = Dealership([car1, car2],[salerperson1], [customer1])
        print(dealership1)
        print(customer1)
        print(customer2)
        


Program.main()

