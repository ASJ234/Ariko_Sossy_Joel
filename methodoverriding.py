#Real-World Example 1: Vehicle Class Hierarchy

class Vehicle:
    def start_engine(self):
        print("Engine starting with a generic sound..") 

class Car(Vehicle):
    def start_engine(self):  
        print("Car engine starting with a vroom sound") 

class Motorcycle(Vehicle):
    def start_engine(self):  
        print("Motorcycle engine starting with a rev sound!")

# Insantiation and method calls
car = Car()
motorcycle = Motorcycle()
car.start_engine()
motorcycle.start_engine()