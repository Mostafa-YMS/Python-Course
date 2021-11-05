class Person:
    moods = ("happy", "tired", "lazy")

    def __init__(self, name, money, mood, healthRate):
        self.name = name
        self.money = money
        self.mood = mood
        self.healthRate = healthRate

    @property
    def healthRate(self):
        return self.__healthRate

    @healthRate.setter
    def healthRate(self, healthRate):
        if not str(healthRate).isdigit() or healthRate < 0:
            self.__healthRate = 0
        elif healthRate > 100:
            self.__healthRate = 100
        else:
            self.__healthRate = healthRate

    def sleep(self, hours):
        if not str(hours).isdigit():
            print("hours should be a number")
            return -1
        if hours == 7:
            self.mood = self.moods[0]
        elif hours < 7:
            self.mood = self.moods[1]
        elif hours > 7:
            self.mood = self.moods[2]

    def eat(self, meals):
        if not str(meals).isdigit() or meals > 3 or meals < 1:
            print("meals should be a number")
            return -1
        elif meals == 3:
            self.healthRate = 100
        elif meals == 2:
            self.healthRate = 75
        elif meals == 1:
            self.healthRate = 50

    def buy(self, items):
        if not str(items).isdigit():
            print("hours should be a number")
            return -1
        elif (items * 10) > self.money:
            print("Not enough money!!")
        else:
            self.money = self.money - (items * 10)
