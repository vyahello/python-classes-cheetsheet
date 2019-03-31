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
