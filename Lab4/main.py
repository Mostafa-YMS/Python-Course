from employee import Employee
from car import Car
from office import Office
import json

samycar = Car("fiat 128", 50, 100)
samy = Employee("Samy", 1000, "happy", 50, 102, "samy@iti.eg", samycar, 20)
iti = Office("ITI", [samy])

data = json.dumps(iti(), indent=4)
with open('iti.json', 'w') as file:
    file.write(data)
