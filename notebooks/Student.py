class Student:

    def __init__(self, name, major, gpa, is_on_probation):
        self.name = name
        self.major = major
        self.gpa = gpa
        self.is_on_probation = is_on_probation

    def on_honor_roll(self):
        if self.gpa >= 3.5:
            return True
        else:
            return False

student3 = Student("Joe", "Business", 4.1, False)
student4 = Student("Oleg", "PR", 3.4, False)

print("If", student4.name, "is on the honor roll?", student4.on_honor_roll())
print("If", student3.name, "is on the honor roll?", student3.on_honor_roll())