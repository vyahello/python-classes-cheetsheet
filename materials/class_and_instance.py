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
