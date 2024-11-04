# object oriented programming

class Employee:
    def __init__(self, name, id_number, dob, gender):
        self.name = name
        self.id_number = id_number
        self.dob = dob
        self.gender = gender

    def print_details(self):
        print(f"Name: {self.name}\nID: {self.id_number}\nDOB: {self.dob}\nGender: {self.gender}")


class PermanentEmployee(Employee):
    def __init__(self, name, id_number, dob, gender, salary):
        super().__init__(name, id_number, dob, gender)
        self.salary = salary
    def print_salary(self):
        print(f"Salary is {self.salary}")

    def print_details(self):
        super().print_details()
        print(f"salary is {self.salary}")

class TemporaryEmployee(Employee):
    def __init__(self, name, id_number, dob, gender, hourly_pay, end_date):
        super().__init__(name, id_number, dob, gender)
        self.hourly_pay = hourly_pay
        self.end_date = end_date

    def print_hourly_pay(self):
        print(f"Hourly payment is {self.hourly_pay}")

    def print_end_date(self):
        print(f"End date is {self.end_date}")


p1 = PermanentEmployee(salary=20000, name= "jane said", id_number= "676754541", dob= 11/4/87, gender= "Female")
p1.print_details()
p1.print_salary()

t1 = TemporaryEmployee("hein", 3432316, "4/5/93", "male", 1000, "7/8/30")
t1.print_details()