from __future__ import annotations
# task 3

class Dealership:

    def __init__(self, list_cars: list[Car] = None, list_salesperson: list[Salesperson] = None, list_customers: list[Customer] = None)
        self.__list_cars = list_cars
        self.__list_salesperson = list_salesperson
        self.__list_customers = list_customers

    def add_car(self):
        pass

    def add_salesperson(self):
        pass

    def add_customer(self):
        pass

    def remove_car(self):
        pass

    def remove_salesperson(self):
        pass

    def get_list_cars(self):
        pass

    def get_list_customers(self):
        pass

    def get_list_salesperson(self):
        pass


    def __str__(self):
        pass

class Salesperson:

    def __init__(self, name: str, work_experience: float, list_sold_cars: list[Car] = None):
        self.__name = name
        self.__work_experience = work_experience
        self.__list_sold_cars = list_sold_cars

    def get_name(self):
        pass

    def get_list_sold_car(self):
        pass

    def add_sold_car(self):
        pass

    def remove_sold_car(self):
        pass

    def __str__(self):
        pass

class Car:
    pass

class Customer:
    pass

class Program:

    @staticmethod
    def main():
        pass

