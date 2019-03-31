# Python classes bootcamp
My own implementation of python classes cheetsheet which is aimed on helping to comprehend a python classes by newcomers.

## Table of contents
- [Class and instance](#class-and-instance)
- [Class VS instance VS static methods](#class-vs-instance-vs-static-methods)
- [Class and instance variables](#class-and-instance-variables)
- [Properties](#properties)
- [Magic methods](#magic-methods)
- [Basics of classes inheritance](#basics-of-classes-inheritance)
- [Additional materials](#additional-materials)

### Class and instance
```python
# class_and_instance.py
class ClassName:
    
    def method(self):
        pass


print(dir(ClassName))

print(ClassName)
print(type(ClassName))

print(ClassName())
print(type(ClassName()))

print(isinstance(ClassName(), ClassName))
print(isinstance(ClassName, ClassName))
```

### Class VS instance VS static methods
```python
# class_instance_static.py
class ClassName:
    
    def instance_method(self):
        return self

    @staticmethod
    def static_method():
        return 'nothing...'
    
    @classmethod
    def class_method(cls):
        return cls


print(ClassName().instance_method())
print(ClassName().static_method())
print(ClassName().class_method())

print(ClassName.instance_method(ClassName()))
print(ClassName.static_method())
print(ClassName.class_method())
```

### Class and instance variables
```python
# class_instance_vars.py
class MyClass:

    class_var = 7

    def __init__(self, inst_var):
        self.inst_var = inst_var

    def add(self):
        return self.inst_var + self.class_var

# save class into a variable
cls = MyClass

# instantiate a class and save it into a variable
instance = cls(10)

# access to class and instance variables
print(cls.class_var)
print(instance.inst_var)
print(instance.class_var)
print(cls.inst_var)

# add class and instance variables via instance method
print(instance.add())

# redeclare class and instance variables
cls.class_var = 8
instance.inst_var = 20
print(cls.class_var)
print(instance.inst_var)
print(instance.add())

# declare new class and instance variables
cls.class_var1 = 'new class variable'
instance.inst_var3 = 'new instance variable'
print(cls.class_var1)
print(instance.inst_var3)

# delete class an instance variables
del cls.class_var
del instance.inst_var
print(cls.class_var)
print(instance.inst_var)
```

### Properties
# `@property` decorator returns a property attribute. It helps to create `getter` for read-only option, `setter` to manage set value option and `deleter` to manage delete option of an attribute.
```python
# properties.py
class Person:

    def __init__(self, first_name):
        self.first_name = first_name

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, name):
        if not isinstance(name, str):
            raise TypeError('Expected to see an <str> type but got type <{}>!!!'.format(name.__class__.__name__))
        self._first_name = name

    @first_name.deleter
    def first_name(self):
        raise AttributeError('Cannot delete "first_name" attribute!!!')


person = Person('Luke')
print(person.first_name)

person.first_name = 'Mike'
print(person.first_name)

person.first_name = 10

del person.first_name
```

### Magic methods
# `magic methods` provide a simple way to make objects behave like `built-in` types.
```python
# magic.py
class Element(object):

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return '"{1}" object has "value" {0} attribute with type <{2}> '.format(self.value,
                                                                                self.__class__.__name__,
                                                                                self.value.__class__.__name__)

    def __len__(self):
        return len(self.value)

    def __contains__(self, item):
        return item in self.value

    def __call__(self, value):
        print('Calling instance of an Element class')
        return Element(value)

    def __iter__(self):
        n = 0
        while n < len(self.value):
            yield self.value[n]
            n += 1


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
for i in element:
    print(i)
```

### Basics of classes inheritance
```python
# inheritance.py
class Animal:

    def __init__(self, name, age, alive=True, hungry=False):
        self.name = name
        self.age = age
        self.alive = alive
        self.hungry=hungry

    def description(self):
        return "Name of an animal is {} and it is {} years old".format(self.name, self.age)

    def is_alive(self):
        return self.alive

    def is_hungry(self):
        return self.hungry


class Parrot(Animal):

    def say(self):
        return 'Krrr...'

    def type(self):
        return 'Domestic'


class Panther(Animal):

    def say(self):
        return 'Shhh...'

    def type(self):
        return 'Wild'


parrot = Parrot('Jake', 2)
print(parrot.description())
print(parrot.is_alive())
print(parrot.is_hungry())
print(parrot.say())
print(parrot.type())

panther = Panther('Sky', 3)
print(panther.description())
print(panther.is_alive())
print(panther.is_hungry())
print(panther.say())
print(panther.type())
```

### Additional materials
- [https://docs.python.org/3.6/tutorial/classes.html](https://docs.python.org/3.6/tutorial/classes.html)
- [http://book.pythontips.com/en/latest/classes.html](http://book.pythontips.com/en/latest/classes.html)
- [https://docs.python.org/3/library/functions.html#classmethod](https://docs.python.org/3/library/functions.html#classmethod)
- [https://docs.python.org/3/library/functions.html#staticmethod](https://docs.python.org/3/library/functions.html#staticmethod)
- [https://realpython.com/instance-class-and-static-methods-demystified](https://realpython.com/instance-class-and-static-methods-demystified)
- [https://rszalski.github.io/magicmethods](https://rszalski.github.io/magicmethods)
- [http://www.diveintopython3.net/special-method-names.html](http://www.diveintopython3.net/special-method-names.html)

# Contributing
- clone the repository
- configure Git for the first time after cloning with your name and email
  ```bash
  git config --local user.name "Volodymyr Yahello"
  git config --local user.email "vyahello@gmail.com"
  ```
- `python3.6` is required to run the code