class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def display_info(self):
        print(f"Make: {self.make}")
        print(f"Model: {self.model}")


class Car(Vehicle):
    def __init__(self, make, model, num_doors):
        super().__init__(make, model)
        self.num_doors = num_doors

    def additional_info(self):
        print(f"Number of Doors: {self.num_doors}")


class LuxuryCar(Car):
    def __init__(self, make, model, num_doors, features):
        super().__init__(make, model, num_doors)
        self.features = features

    def additional_info(self):
        print(f"Luxury Features: {', '.join(self.features)}")


luxury_car = LuxuryCar("Mercedes-Benz", "S-Class", 4, ["Leather seats", "Sunroof", "Advanced sound system"])
print("Luxury Car Information:")
luxury_car.display_info()
luxury_car.additional_info()

# Task 2

class Employee:
    def __init__(self, name, position):
        self.name = name
        self.position = position

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Position: {self.position}")



class Manager(Employee):
    def __init__(self, name, position, department):
        super().__init__(name, position)
        self.department = department

    def additional_info(self):
        print(f"Department: {self.department}")


class Worker(Employee):
    def __init__(self, name, position, hours_worked):
        super().__init__(name, position)
        self.hours_worked = hours_worked

    def additional_info(self):
        print(f"Hours Worked: {self.hours_worked}")


manager = Manager("Alice Johnson", "Manager", "Sales")
worker = Worker("John Smith", "Worker", 40)

print("\nManager Information:")
manager.display_info()
manager.additional_info()

print("\nWorker Information:")
worker.display_info()
worker.additional_info()
