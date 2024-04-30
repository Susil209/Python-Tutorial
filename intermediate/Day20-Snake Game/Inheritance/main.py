
# parent class
class Employee:
    raise_amt = 1.4

    def __init__(self, fname, lname, pay):
        self.first = fname
        self.last = lname
        self.email = self.first + "." + self.last + "@company.com"
        self.pay = pay

    def fullname(self):
        return f"{self.first} {self.last}"

    def apply_raise(self):
        self.pay = self.pay * self.raise_amt


# child class
class Developer(Employee):
    raise_amt = 1.5

    def __init__(self, fname, lname, pay, prog_lang):
        super().__init__(fname, lname, pay)
        self.prog = prog_lang


dev1 = Developer("Arman", "Shukla", 30000, 'Python')
dev2 = Developer("Arjun", "Kamran", 30000, 'Java')
print(dev1.fullname())
print(dev1.prog)


class Manager(Employee):
    def __init__(self, fname, lname, pay, employees=None):
        super().__init__(fname, lname, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emp(self):
        for emp in self.employees:
            print("-->", emp.fullname())


mgr1 = Manager("Pradeep", "Sethi", 50000, [dev1,dev2])
print(mgr1.fullname())
mgr1.print_emp()

print(isinstance(mgr1, Manager)) # True
print(isinstance(mgr1, Employee)) # True
print(isinstance(mgr1, Developer)) # False

print(issubclass(Developer, Employee))  # True
print(issubclass(Manager, Employee))  # True
print(issubclass(Manager, Developer))  # False