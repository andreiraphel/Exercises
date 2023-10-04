import pytest
from employee_management import Employee, Manager, Engineer, Salesperson

# Test Employee class
def test_employee():
    employee = Employee("John", 1, 60000)
    assert employee.name == "John"
    assert employee.id == 1
    assert employee.salary == 60000

# Test Manager class
def test_manager():
    manager = Manager("Alice", 2, 70000, 35)
    assert manager.name == "Alice"
    assert manager.id == 2
    assert manager.salary == 70000
    assert manager.age == 35

# Test Engineer class
def test_engineer():
    engineer = Engineer("Bob", 3, 55000, 30)
    assert engineer.name == "Bob"
    assert engineer.id == 3
    assert engineer.salary == 55000
    assert engineer.age == 30

# Test Salesperson class
def test_salesperson():
    salesperson = Salesperson("Eve", 4, 50000, 28)
    assert salesperson.name == "Eve"
    assert salesperson.id == 4
    assert salesperson.salary == 50000
    assert salesperson.age == 28

if __name__ == "__main__":
    pytest.main()
