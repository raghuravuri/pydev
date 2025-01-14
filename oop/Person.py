import datetime # we will use this for date objects

class Person:

    # area to define class level member variables
    TITLES = ('Dr', 'Mr', 'Mrs', 'Ms')
    pets = []

    # constructor
    def __init__(self, title, name, surname, birthdate, height, address, telephone, email, allowed_titles=TITLES):

        # validation using class level variable
        if title not in self.TITLES:
            raise ValueError("%s is not a valid title." % title)

        # area to set instance level variables
        self.name = name
        self.surname = surname
        self.birthdate = birthdate

        self.address = address
        self.telephone = telephone
        self.email = email

        self.height = height

    # method of class
    def age(self):
        today = datetime.date.today()
        age = today.year - self.birthdate.year

        if today < datetime.date(today.year, self.birthdate.month, self.birthdate.day):
            age -= 1

        return age

    # method
    def add_pet(self, pet):
        self.pets.append(pet)

    @classmethod
    def allowed_titles_starting_with(cls, startswith): # class method
        # class or instance object accessible through cls
        return [t for t in cls.TITLES if t.startswith(startswith)]

    @staticmethod
    def allowed_titles_ending_with(endswith): # static method
        # no parameter for class or instance object
        # we have to use Person directly
        return [t for t in Person.TITLES if t.endswith(endswith)]

    # sample of getters and setters, not needed in python
    def get_height(self):
        return self.height

    def set_height(self, height):
        self.height = height


    @property
    def fullname(self):
        return "%s %s" % (self.name, self.surname)

    # overriding magic methods!
    # defines toString rep of an object
    def __str__(self):
        return "%s %s, born %s\nAddress: %s\nTelephone: %s\nEmail:%s" % (self.name, self.surname, self.birthdate, self.address, self.telephone, self.email)

    def __eq__(self, other):  # does self == other?
        return self.name == other.name and self.surname == other.surname

    def __gt__(self, other):  # is self > other?
        if self.surname == other.surname:
            return self.name > other.name
        return self.surname > other.surname

    # now we can define all the other methods in terms of the first two

    def __ne__(self, other):  # does self != other?
        return not self == other  # this calls self.__eq__(other)

    def __le__(self, other):  # is self <= other?
        return not self > other  # this calls self.__gt__(other)

    def __lt__(self, other):  # is self < other?
        return not (self > other or self == other)

    def __ge__(self, other):  # is self >= other?
        return not self < other

# instantiate a class with inputs to create Object
person = Person(
    "Mr",
    "Jane",
    "Doe",
    datetime.date(1992, 3, 12), # year, month, day
    153,
    "No. 12 Short Street, Greenville",
    "555 456 0987",
    "jane.doe@example.com"
)

person.add_pet("cat")
person.add_pet("dog")

# Print attributes of the class
print(person.name)
print(person.email)
print(person.age())
print(person.TITLES)
print(Person.TITLES)
print(person.allowed_titles_ending_with("M"))
print(Person.allowed_titles_ending_with("s"))
person.height += 1 # increase height by 1, through direct access
person.set_height(person.height+1) # increase again
print(person.get_height()) # print through getter and not getter
print(person.height)
print(person.fullname)  # no brackets, because of the property decorator!
print(dir(person)) # inspect an object!
print(person) # calls string convertion of an object
