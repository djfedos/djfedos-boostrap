# inheritance

# we can: inherit, extend, override
class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def work(self):
        print(f'{self.name} is working...')

class SoftwareEngineer(Employee):
    def __init__(self, name, age, salary, level):
        super().__init__(name, age, salary)
        self.level = level

    def debug(self):
        print(f'{self.name} is debugging...')

    def work(self):
        print(f'{self.name} is coding...')


class Designer(Employee):
    def draw(self):
        print(f'{self.name} is drawing...')

    def work(self):
        print(f'{self.name} is designing...')


def inheritance_demo():
    se1 = SoftwareEngineer('Max', 25, 6000, 'Junior')

    print(se1.name, se1.age)
    print(se1.level)
    se1.work()
    se1.debug()

    d = Designer('Philipp', 27, 7000)
    print(d.name, d.age)
    d.work()
    d.draw()

    w1 = Employee('Joe', 36, 7000)
    w1.work()


# polymorphism
employees = [SoftwareEngineer('Max', 25, 6000, 'Junior'),
             SoftwareEngineer('Lisa', 30, 9000, 'Senior'),
             Designer('Philipp', 27, 7000),
             Employee('Adam', 33, 5000)]


# due to polymorphism this function will call work function on child class instances from their class
# and on employee class itself from employee class itself
def motivate_employees(employees):
    for employee in employees:
        employee.work()


if __name__ == '__main__':
    motivate_employees(employees)
    # inheritance_demo ()