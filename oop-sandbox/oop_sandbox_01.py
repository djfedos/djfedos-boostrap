# basic class properties recap
# following this tutorial: https://youtu.be/-pEs-Bss8Wc

# create class
class SoftwareEngineer():

    # class attribute
    department = 'IT'


    # works on class itself and on its instances. without @staticmethod decorator it will work on class only
    @staticmethod
    def entry_salary(age):
        if age < 21:
            return 5000
        if age < 25:
            return 6000
        else:
            return 7000

    def __init__(self, name, age, level, salary):
        # instance attributes
        self.name = name
        self.age = age
        self.level = level
        self.salary = salary

    def code(self):
        print(f'{self.name} is writing code...')

    def code_in_language(self, language):
        print(f'{self.name} is writing code in {language}')

    # what to print when we print an instance of the class
    def __str__(self):
        information = f"name: {self.name}, age: {self.age}, level: {self.level}, department: {SoftwareEngineer.department}"
        return information

    # what to compare when we compare two class instances (watch out for non-unique attributes!)s
    def __eq__(self, other):
        return self.name == other.name and self.age == other.age


# create instances
se1 = SoftwareEngineer('Max', 20, 'Junior', 5000)
se2 = SoftwareEngineer('Julia', 25, 'Mid', 7000)
se3 = SoftwareEngineer('Julia', 25, 'Mid', 7000)
se4 = SoftwareEngineer('Julia', 24, 'Mid', 7000)

print(se2 == se3)
print(se2 == se4)
print(se1.entry_salary(24))
print(SoftwareEngineer.entry_salary(24))

print(se1)
print(se2)
# print(se1.name, se1.salary, se1.department)
# print(se2.name, se2.salary, se2.department)
#
# # print(SoftwareEngineer.name) throws an error, name is an instance attribute, not a class attribute
# print(SoftwareEngineer.department)
#
# se1.code()
# se2.code()
# se1.code_in_language('Python')
# se2.code_in_language('Rust')
