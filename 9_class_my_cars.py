from class_car import Car
from class_electric_car import ElectricCar
# from class_electric_car import *


my_beetle = Car('volkswagen', 'beetle', 2016)
print(my_beetle.get_descriptive_name())
my_tesla = ElectricCar('tesla', 'roadster', 2016)
print(my_tesla.get_descriptive_name())

# import class_electric_car
#
#
# my_beetle = class_electric_car.Car('volkswagen', 'beetle', 2016)
# print(my_beetle.get_descriptive_name())
# my_tesla = class_electric_car.ElectricCar('tesla', 'roadster', 2016)
# print(my_tesla.get_descriptive_name())