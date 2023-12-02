# This file is part of TaskFlow
# A task management application in Python
# v0.4.dev1 (2 Dec 2023, main/fe9cd22)


class Person:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def to_dict(self):
        """Convert the person object to a dictionary."""
        return {'name': self.name, 'email': self.email}

    @classmethod
    def from_dict(cls, data):
        """Create a Person object from a dictionary."""
        return cls(data['name'], data['email'])

    def write_to_file(self, filename):
        """Write person details to a file."""
        with open(filename, 'w') as file:
            file.write(f"{self.name},{self.email}")

    @classmethod
    def read_from_file(cls, filename):
        """Read person details from a file and create a Person object."""
        with open(filename, 'r') as file:
            data = file.readline().strip().split(',')
        return cls(data[0], data[1])
