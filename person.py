import datetime

class Person:

    def __init__(self, name, dob, height, weight, role):
        self.name = name
        self.dob = dob
        self.height = height
        self.weight = weight
        self.role = role
        self.dtformat = "%d %m %Y"

    def __str__(self):
        return f"{self.name}\nDOB: {self.dob.strftime(self.dtformat)}"

x = Person("Oof", datetime.datetime.now(), 140, 32, "Oof")
print(x.__str__())
