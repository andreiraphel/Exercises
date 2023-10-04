class Employee:
    def __init__(self, name, id, salary):
        self.name = name
        self.id = id
        self.salary = salary

class Manager(Employee):
    def __init__(self, name, id, salary, age):
        super().__init__(name, id, salary)
        self.age = age


class Engineer(Employee):
    def __init__(self, name, id, salary, age):
        super().__init__(name, id, salary)
        self.age = age

class Salesperson(Employee):
    def __init__(self, name, id, salary, age):
        super().__init__(name, id, salary)
        self.age = age

def main():
    manager = Manager("John", 1, 60000, 40)
    engineer = Engineer("Alice", 2, 55000, 30)
    salesperson = Salesperson("Bob", 3, 50000, 35)

    print(manager.name, manager.id, manager.salary, manager.age)
    print(engineer.name, engineer.id, engineer.salary, engineer.age)
    print(salesperson.name, salesperson.id, salesperson.salary, salesperson.age)

if __name__ == "__main__":
    main()