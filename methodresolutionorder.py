#Real-World Example with MRO: Family Inheritance

class Grandparent:
    def greet(self):
        return "Hello from Grandparent!"

class ParentA(Grandparent):
    def greet(self):
        return "Hello from ParentA!"

class ParentB(Grandparent):
    def greet(self):
        return "Hello from ParentB!"

class Child(ParentA, ParentB):
    pass

# Instantiation and method call
child = Child()
print(child.greet())  