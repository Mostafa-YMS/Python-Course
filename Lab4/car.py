class Car:
    def __init__(self, name, fuelRate, velocity):
        self.name = name
        self.fuelRate = fuelRate
        self.velocity = velocity

    @property
    def velocity(self):
        return self.__velocity

    @velocity.setter
    def velocity(self, velocity):
        if not str(velocity).isdigit() or velocity < 0:
            self.__velocity = 0
        elif velocity > 200:
            self.__velocity = 200
        else:
            self.__velocity = velocity

    @property
    def fuelRate(self):
        return self.__fuelRate

    @fuelRate.setter
    def fuelRate(self, fuelRate):
        if not str(fuelRate).isdigit() or fuelRate < 0:
            self.__fuelRate = 0
        elif fuelRate > 100:
            self.__fuelRate = 100
        else:
            self.__fuelRate = fuelRate

    def stop(self, remaining):
        self.velocity = 0
        if remaining == 0:
            print("Arrived to destination")
        else:
            print(f"You're out of fuel the remaining distance is {remaining}")

    def run(self, velocity, distance):
        self.velocity = velocity
        if distance <= self.fuelRate:
            self.fuelRate = self.fuelRate - distance
            self.stop(0)
        elif distance > self.fuelRate:
            remaining = distance - self.fuelRate
            self.fuelRate = 0
            self.stop(remaining)
