class Person:
    def __init__(self, first_name):
        self.first_name = first_name

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, name):
        if not isinstance(name, str):
            raise TypeError(
                "Expected to see an <str> type but got type <{}>!!!".format(
                    name.__class__.__name__
                )
            )
        self._first_name = name

    @first_name.deleter
    def first_name(self):
        raise AttributeError('Cannot delete "first_name" attribute!!!')


person = Person("Luke")
print(person.first_name)

person.first_name = "Mike"
print(person.first_name)

person.first_name = 10

del person.first_name
