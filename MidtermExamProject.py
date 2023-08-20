import datetime

# EmployeeSystem class to manage employees
class EmployeeSystem:
    def __init__(self, filename):
        self.filename = filename
        self.employees = {}  # Dictionary to store employee data (employee ID as key)
        self.load_employees_from_file()  # Load employees from file
        self.auto_increment_id = len(self.employees) + 1  # To generate new employee IDs

    # Load employees from a file
    def load_employees_from_file(self):
        try:
            with open(self.filename, 'r') as file:
                lines = file.readlines()
                for line in lines:
                    emp_id, username, date_joined, gender, salary = line.strip().split(', ')
                    self.employees[emp_id] = {
                        "Username": username,
                        "DateJoined": date_joined,
                        "Gender": gender,
                        "Salary": int(salary)
                    }
        except FileNotFoundError:
            print("File not found.")

    # Save employee data to a file
    def save_employees_to_file(self):
        try:
            with open(self.filename, 'w') as file:
                for emp_id, emp_data in self.employees.items():
                    line = f"{emp_id}, {emp_data['Username']}, {emp_data['DateJoined']}, {emp_data['Gender']}, {emp_data['Salary']}\n"
                    file.write(line)
            print("Employee data saved successfully.")
        except IOError:
            print("Error saving employee data.")

    # Display information for a specific employee
    def display_employee(self, emp_id):
        emp_data = self.employees.get(emp_id)
        if emp_data:
            print("Employee ID:", emp_id)
            print("Username:", emp_data["Username"])
            print("Date Joined:", emp_data["DateJoined"])
            print("Gender:", emp_data["Gender"])
            print("Salary:", emp_data["Salary"])
        else:
            print("Employee not found.")

    # Display information for all employees, sorted by join date
    def display_all_employees(self):
        sorted_employees = sorted(self.employees.items(), key=lambda x: x[1]["DateJoined"], reverse=True)

        today = datetime.datetime.now().strftime("%Y%m%d")
        yesterday = (datetime.datetime.now() - datetime.timedelta(days=1)).strftime("%Y%m%d")

        print("Employee List:")
        for emp_id, emp_data in sorted_employees:
            date_joined = datetime.datetime.strptime(emp_data["DateJoined"], "%Y%m%d")
            if date_joined.strftime("%Y%m%d") == today:
                date_category = "Today"
            elif date_joined.strftime("%Y%m%d") == yesterday:
                date_category = "Yesterday"
            else:
                date_category = date_joined.strftime("%Y-%m-%d")

            print(f"Employee ID: {emp_id}")
            print(f"Username: {emp_data['Username']}")
            print(f"Date Joined: {emp_data['DateJoined']} ({date_category})")
            print(f"Gender: {emp_data['Gender']}")
            print(f"Salary: {emp_data['Salary']}")
            print("-" * 20)