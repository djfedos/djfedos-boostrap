# encapsulation

class SoftwareEngineer:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self._salary = None

    def code(self):
        self._num_bugs_solved += 1

    # getter
    @property
    def salary(self):
        return self._salary

    # setter
    @salary.setter
    def salary(self, value):
        self._salary = value

    @salary.deleter
    def salary(self):
        del self._salary

se = SoftwareEngineer('Max', 25)
print(se.name, se.age)

se.salary = 6000
print(se.salary)

# deleter works as expected
# del se.salary
# so when the _salary is deleted an attempt to print it out will lead to an error
# print(se.salary)



