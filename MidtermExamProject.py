class Employee:
    def __init__(self, emp_id, username, date_joined, gender, salary):
        self.emp_id = emp_id
        self.username = username
        self.date_joined = date_joined
        self.gender = gender
        self.salary = salary

class EmployeeSystem:
    def __init__(self):
        self.employees = {}
        self.load_employees_from_file("employee_data.txt")
        self.auto_increment_id = len(self.employees) + 1 

    def load_employees_from_file(self, filename):
        try:
            with open(filename, 'r') as file:
                lines = file.readlines()
                for line in lines:
                    emp_id, username, date_joined, gender, salary = line.strip().split(', ')
                    self.employees[emp_id] = Employee(emp_id, username, date_joined, gender, int(salary))
        except FileNotFoundError:
            print("File not found.")