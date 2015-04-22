import re


class Panda:

    def __init__(self, name, email, gender):
        self.name = name
        self.set_email(email)
        self.gender = gender

    def __str__(self):
        result = "name: {} email: {} gender: {}"
        return result.format(self.name, self.email, self.gender)

    def __repr__(self):
        return "Panda('{}', '{}', '{}')".format(self.name,
                                                self.email, self.gender)

    def __eq__(self, other):
        return self.name == other.name and self.email == other.email \
            and self.gender == other.gender

    def __hash__(self):
        return hash(str(self.name) + str(self.email) + str(self.gender))

    def is_male(self):
        return self.gender == "male"

    def is_female(self):
        return self.gender == "female"

    def set_email(self, email):
        if not re.match(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", email):
            raise ValueError
        else:
            self.email = email


