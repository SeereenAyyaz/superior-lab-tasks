class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")


class Employee:
    def __init__(self, employee_id, position):
        self.employee_id = employee_id
        self.position = position

    def display_info(self):
        print(f"Employee ID: {self.employee_id}")
        print(f"Position: {self.position}")

class Staff(Person, Employee):
    def __init__(self, name, age, employee_id, position, department):
        Person.__init__(self, name, age)
        Employee.__init__(self, employee_id, position)
        self.department = department

    def additional_info(self):
        print(f"Department: {self.department}")


def read_employees_from_file(filename):
    employees = []
    try:
        with open(filename, 'r') as file:
            for line in file:
                name, age, employee_id, position, department = line.strip().split(', ')
                employees.append(Staff(name, int(age), employee_id, position, department))
    except FileNotFoundError:
        print(f"The file '{filename}' does not exist. A new file will be created upon saving.")
    return employees


def add_employee(employees):
    name = input("Enter the employee's name: ").strip()
    age = int(input("Enter the employee's age: ").strip())
    employee_id = input("Enter the employee's ID: ").strip()
    position = input("Enter the employee's position: ").strip()
    department = input("Enter the employee's department: ").strip()

    new_employee = Staff(name, age, employee_id, position, department)
    employees.append(new_employee)
    print("New employee added successfully!")


def save_employees_to_file(filename, employees):
    with open(filename, 'w') as file:
        for employee in employees:
            file.write(f"{employee.name}, {employee.age}, {employee.employee_id}, {employee.position}, {employee.department}\n")
    print(f"Employee information saved to '{filename}' successfully!")



filename = "employees.txt"
employees = read_employees_from_file(filename)

print("\nCurrent Employee Details:")
for employee in employees:
    employee.display_info()
    employee.additional_info()
    print()

add_employee(employees)
save_employees_to_file(filename, employees)
