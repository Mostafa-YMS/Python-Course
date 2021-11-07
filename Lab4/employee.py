from person import Person
from emailcomposer import email_composer
from validation.checkemail import chkmail
from car import Car


class Employee(Person):
    def __init__(self, name, money, mood, healthRate, id, email, car, distanceToWork):
        super().__init__(name, money, mood, healthRate)
        self.id = id
        self.car = car
        self.email = email
        self.distanceToWork = distanceToWork

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, salary):
        if not str(salary).isdigit() or salary < 1000:
            self.__salary = 1000
        else:
            self.__salary = salary

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, email):
        if chkmail(email):
            self.__email = email
        else:
            self.__email = None

    @property
    def car(self):
        return self.__car

    @car.setter
    def car(self, car):
        if type(car) is Car:
            self.__car = car
        else:
            self.__car = None

    def __call__(self, *args, **kwargs):
        return {"id": self.id, "name": self.name, "money": self.money, "mood": self.mood, "healthRate": self.healthRate,
                "email": self.email,  "distanceToWork": self.distanceToWork, "car": self.car.__dict__}

    def work(self, hours):
        if not str(hours).isdigit():
            print("hours should be a number")
            return -1
        if hours == 8:
            self.mood = self.moods[0]
        elif hours > 8:
            self.mood = self.moods[1]
        elif hours < 8:
            self.mood = self.moods[2]

    def drive(self, distance):
        if self.__car is not None:
            self.__car.run(self.__car.velocity, distance)
        else:
            print("you don't have a car")

    def refuel(self, gasAmount = 100):
        if self.__car is not None:
            self.__car.fuelRate = self.__car.fuelRate + gasAmount
        else:
            print("you don't have a car")

    def send_mail(self, to, subject, msg, receiver_name):
        if self.email is not None:
            email_composer(self.email, to, subject, msg, receiver_name)
        else:
            print("You don't have an email")
