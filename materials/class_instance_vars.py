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
