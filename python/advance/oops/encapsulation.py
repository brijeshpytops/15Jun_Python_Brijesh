class car:
    def __init__(self, brand, model, year, color):
        self.brand = brand # public
        self.model = model # public
        self.year = year # public
        self.__color = color # private

    def display_car_info(self):
        return f"Brand: {self.brand}, Model: {self.model}, Year: {self.year}, Color: {self.__color}"
    
car1 = car("Toyota", "Camry", 2020, "Blue")

# name mangling
print(car1._car__color)

# print(car1.display_car_info())

# print(car1.brand)
# print(car1.__color)

# print(car1.display_car_info())

# car2 = car("ABC", "xyz#25646", 2022, "red")

# print(car2.display_car_info())