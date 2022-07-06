# encapsulation

class SoftwareEngineer:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self._salary = None
        self._num_bugs_solved = 0
        # the attribute below is private, we can't access it directly
        self.__hidden_property = True

    def code(self):
        self._num_bugs_solved += 1

    # getter
    def get_salary(self):
        return self._salary

    # setter
    def set_salary(self, base_value):
        if base_value < 1000:
            print('Stop being greed, increase the value')
        elif base_value > 20000:
            print('Stop being wasteful, decrease the value')
        else:
            if self._num_bugs_solved < 10:
                self._salary = base_value
            if self._num_bugs_solved < 100:
                self._salary = base_value * 2
            if self._num_bugs_solved >= 100:
                self._salary = base_value * 3
        print(f'Current salary is {se._salary}')




se = SoftwareEngineer('Max', 25)
print(se.name, se.age)

# the _salary attribute is protected: it's technically visible, but by convention we shouldn't access it directly
# here we do it just as an example to show that it's possible
se._salary = 6000
print(se._salary)

# and now we do it properly with setter and getter methods:
se.set_salary(900)

for i in range(70):
    se.code()

print(se._num_bugs_solved)
se.set_salary(5000)
print(se.get_salary())
# and the line below won't work
# print(se.__hidden_property)

