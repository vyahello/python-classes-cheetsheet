class Element:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return '"{1}" object has "value" {0} attribute with type <{2}> '.format(
            self.value, self.__class__.__name__, self.value.__class__.__name__
        )

    def __len__(self):
        return len(self.value)

    def __contains__(self, item):
        return item in self.value

    def __call__(self, value):
        print("Calling instance of an Element class")
        return Element(value)

    def __iter__(self):
        initial_counter = 0
        while initial_counter < len(self.value):
            yield self.value[initial_counter]
            initial_counter += 1


# instantiate an object
element = Element([3, 4])

# get a list of all magic methods
print([method for method in dir(element) if callable(getattr(element, method))])

# string representation
print(element)

# container representation
print(len(element))
print(3 in element)

# call an instance
print(element((5, 6)))

# iterate over an instance
for iteration in element:
    print(iteration)
