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
                    line = (f"{emp_id}, {emp_data['Username']}, {emp_data['DateJoined']}, {emp_data['Gender']}, {emp_data['Salary']}\n")
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

    # Get title based on employee's gender
    # Time Complexity: O(1)
    def get_title(self, emp_id):
        gender = self.employees[emp_id]["Gender"]
        return "Mr." if gender == "male" else "Ms."

    # Admin menu for managing employees
    # Time Complexity: O(1) 
    def admin_menu(self):
        while True:
            print("\nAdmin Menu")
            print("1. Display Statistics")
            print("2. Add an Employee")
            print("3. Display all Employees")
            print("4. Change Employee Salary")
            print("5. Remove Employee")
            print("6. Raise Employee Salary")
            print("7. Exit")

            choice = input("Enter your choice: ")

            if choice == '1':
                self.display_statistics()
            elif choice == '2':
                self.add_employee()
            elif choice == '3':
                self.display_all_employees()
            elif choice == '4':
                emp_id = input("Enter Employee ID: ")
                new_salary = int(input("Enter New Salary: "))
                self.change_salary(emp_id, new_salary)
            elif choice == '5':
                emp_id = input("Enter Employee ID: ")
                self.remove_employee(emp_id)
            elif choice == '6':
                emp_id = input("Enter Employee ID: ")
                raise_percentage = float(input("Enter Raise Percentage (e.g., 1.05 for 5% raise): "))
                self.raise_salary(emp_id, raise_percentage)
            elif choice == '7':
              
                print("Exiting the program.")
                self.save_employees_to_file()  # Save employee data before exiting
                break
            else:
                print("Invalid choice. Please choose again.")

    # User menu for normal employees
    # Time Complexity: O(1) 
    def user_menu(self, username):
        while True:
            print("\nUser Menu")
            print("1. Check My Salary")
            print("2. Exit")

            choice = input("Enter your choice: ")

            if choice == '1':
                self.display_employee(username)
            elif choice == '2':
                self.save_login_timestamp(username)  # Save login timestamp before exiting
                print("Exiting the program.")
                break
            else:
                print("Invalid choice. Please choose again.")

    # Display statistics about employees
    # Time Complexity: O(n), 
    def display_statistics(self):
        total_employees = len(self.employees)
        male_count = sum(1 for emp_data in self.employees.values() if emp_data["Gender"] == "male")
        female_count = total_employees - male_count

        print("Statistics:")
        print("Total Employees:", total_employees)
        print("Male Employees:", male_count)
        print("Female Employees:", female_count)

    # Add a new employee to the system 
    # Time Complexity: O(1)
    def add_employee(self):
        username = input("Enter Username: ")
        gender = input("Enter Gender male or female : ")
        salary = int(input("Enter Salary: "))

        # Generate a formatted employee ID 
        emp_id = f"emp{self.auto_increment_id:03d}"
        self.auto_increment_id += 1

        date_joined = datetime.datetime.now().strftime("%Y%m%d")
        self.employees[emp_id] = {
            "Username": username,
            "DateJoined": date_joined,
            "Gender": gender,
            "Salary": salary
        }
        print("Employee added successfully.")

    # Save login timestamp for users
    # Time Complexity: O(1)
    def save_login_timestamp(self, username):
        try:
            with open("login_timestamps.txt", 'a') as file:
                timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                file.write(f"{username}: {timestamp}\n")
                print("Login timestamp saved successfully.")
        except IOError:
            print("Error saving login timestamp.")

# Entry point of the program
if __name__ == "__main__":
    filename = "employee_data.txt"  # file name
    employee_system = EmployeeSystem(filename)  # EmployeeSystem class
    employee_system.run()  # Start the program
