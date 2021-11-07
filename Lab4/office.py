from employee import Employee


class Office:
    employeesNum = 0

    def change_emps_num(self, num):
        self.employeesNum = num

    def __init__(self, name, employees=[]):
        self.name = name
        self.employees = employees

    def __call__(self, *args, **kwargs):
        return {"Office_name": self.name, "employees": self.get_all_employees()}

    @property
    def employees(self):
        return self.__employees

    @employees.setter
    def employees(self, employees):
        if type(employees) is list:
            self.__employees = employees
        elif type(employees) is Employee:
            self.__employees = [employees]
        else:
            print("Employees must be a list or instance of Employee class")

    def get_all_employees(self):
        return list(map(lambda x:x(), self.employees))

    def get_employee(self, empid):
        for emp in self.employees:
            if emp.id == empid:
                return emp()

    def hire(self, employee):
        if employee not in self.employees:
            self.employeesNum += 1
            if type(employee) is Employee:
                self.employees.append(employee)
            else:
                print("employee must be of class Employee")
        else:
            print("Already hired")

    def fire(self, employee):
        if employee in self.employees:
            self.employeesNum -= 1
            if type(employee) is Employee:
                self.employees.remove(employee)
            else:
                print("employee must be of class Employee")
        else:
            print("this employee is not hired")

    @staticmethod
    def calculate_lateness(targetHour, moveHour, distance, velocity):
        availabletime = targetHour - moveHour
        time = distance / velocity
        if time <= availabletime:
            return False
        else:
            return True

    def check_lateness(self, empid, moveHour):
        for emp in self.employees:
            if emp.id == empid:
                self.calculate_lateness(9, moveHour, emp.distanceToWork, emp.car.velocity)

    def deduct(self, empid, deduction):
        for emp in self.employees:
            if emp.id == empid:
                emp.salary = emp.salary - deduction

    def reward(self, empid, reward):
        for emp in self.employees:
            if emp.id == empid:
                emp.salary = emp.salary + reward
