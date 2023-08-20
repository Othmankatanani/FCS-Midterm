import datetime

class EmployeeSystem:
    def __init__(self, filename):
        self.filename = filename
        self.employees = {}  # Dictionary to store employee data 
        self.load_employees_from_file()  # Load employees from file
        self.auto_increment_id = len(self.employees) + 1  # generate new employee IDs

    # Load employees from a file
    # Time Complexity: O(n), where n is the number of employees in the file
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
    # Time Complexity: O(n), where n is the number of employees
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
    # Time Complexity: O(1)
    def display_employee(self, emp_id):
        emp_data = self.employees.get(emp_id)
        if emp_data:
            print("Employee ID:", emp_id)
            print("Username:", emp_data["Username"])
            print("Date Joined:", emp_data["DateJoined"])
            print("Gender:", emp_data["Gender"])
            print("Salary: ${:,.2f}".format(emp_data["Salary"]))  # Display salary in $
        else:
            print("Employee not found.")

    # Display information for all employees, sorted by join date
    # Time Complexity: O(n log n), where n is the number of employees
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
            print(f"Gender : {emp_data['Gender']}")
            print("Salary: ${:,.2f}".format(emp_data["Salary"]))  # Display salary in $
            print("-" * 20)

    # Change an employee's salary
    # Time Complexity: O(1)
    def change_salary(self, emp_id, new_salary):
        emp_data = self.employees.get(emp_id)
        if emp_data:
            emp_data["Salary"] = new_salary
            print("Employee's salary changed successfully.")
        else:
            print("Employee not found.")

    # Remove an employee from the system
    # Time Complexity: O(1)
    def remove_employee(self, emp_id):
        if emp_id in self.employees:
            del self.employees[emp_id]
            print("Employee removed successfully.")
        else:
            print("Employee not found.")

    # Raise an employee's salary by a percentage
    # Time Complexity: O(1)
    def raise_salary(self, emp_id, raise_percentage):
        emp_data = self.employees.get(emp_id)
        if emp_data:
            current_salary = emp_data["Salary"]
            new_salary = int(current_salary * raise_percentage)
            emp_data["Salary"] = new_salary
            print("Employee's salary raised successfully.")
        else:
            print("Employee not found.")

    # Run the employee system
    # Time Complexity: O(1)
    def run(self):
        print("Welcome to the Employee System!")
        login_choice = input("Enter 'A' for Admin Login, 'U' for User Login: ")

        max_login_attempts = 5
        login_attempts = 0

        while login_attempts < max_login_attempts:
            
            if login_choice.upper() == 'A':
                username = input("Enter your admin username: ")
                password = input("Enter your admin password: ")
                if username == "admin" and password == "admin123123":
                    print("Welcome, Admin!")
                    self.admin_menu()
                    break
                else:
                    print("Incorrect Admin Username or Password.")
            elif login_choice.upper() == 'U':
                user_id = input("Enter your user ID: ")
                if user_id in self.employees:
                    print(f"Welcome, {self.get_title(user_id)} {self.employees[user_id]['Username']}!")
                    self.user_menu(user_id)
                    break
                else:
                    print("User ID not found.")
            else:
                print("Invalid choice. Please choose again.")

            login_attempts += 1

        if login_attempts == max_login_attempts:
            print("Exceeded maximum login attempts. Exiting the program.")