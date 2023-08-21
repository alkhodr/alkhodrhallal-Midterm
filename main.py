from datetime import datetime
# The Function below is to import the text file that contains employee data and
# add them to a local dictionay called employee_dict.
def read_employee_database(file_name):
    employee_dict = {}

    with open(file_name, 'r') as file:
        for line in file:
            employee_data = line.strip().split(', ')
            employee_id, username, join_date, gender, salary = employee_data
            
            # Store employee details in the dictionary
            employee_dict[employee_id] = {
                'username': username,
                'join_date': join_date,
                'gender': gender,
                'salary': int(salary)
            }

    return employee_dict
# This function to read and populate the employee dictionary
employee_dict = read_employee_database('employeedatabase.txt')

def login():
    max_attempts = 5
    admin_username = "admin"
    admin_password = "admin123123"
    failed_attempts = 0  # Keep track of failed attempts
    print("(if employee please your ID as username)\n")

    for _ in range(max_attempts):
        username = input("Username: ")
        password = input("Password: ")

        if username == admin_username and password == admin_password:
            print("Welcome, Admin!")
            admin_menu()
            break
        elif password == "":
            if username in employee_dict:  # Check if username exists in employee_dict
                #print(f"Welcome, Mr. {employee_dict[username]['username']}!")
                employee_menu(username)
                break
            else:
                print("Invalid username. Please try again.")
        else:
            failed_attempts += 1
            print(f"Invalid username or password. Attempts remaining: {max_attempts - failed_attempts}")
            
            if failed_attempts == max_attempts:
                print("Login failed. Please contact your administrator.")
# The Admin Menu
def admin_menu():
    while True:
        print("\nAdmin Menu:")
        print("1. Display Statistics")
        print("2. Add an Employee")
        print("3. Display all Employees")
        print("4. Change Employee’s Salary")
        print("5. Remove Employee")
        print("6. Raise Employee’s Salary")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            display_statistics()
        elif choice == "2":
            add_employee()
        elif choice == "3":
            display_all_employees()
        elif choice == "4":
            change_salary()
        elif choice == "5":
            remove_employee()
        elif choice == "6":
            raise_salary()
        elif choice == "7":
            save_to_file()
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please select a valid option.")
#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# Admin menu Features number 1
def display_statistics():
    male_count = sum(1 for emp in employee_dict.values() if emp['gender'] == 'male')
    female_count = len(employee_dict) - male_count
    print(f"Number of male employees: {male_count}")
    print(f"Number of female employees: {female_count}")
# This function adds employees and add them to dictionary while adding time
def add_employee():
    employee_id = f"emp{str(len(employee_dict) + 1).zfill(3)}"
    username = input("Enter employee's username: ")
    gender = input("Enter employee's gender (male/female): ")
    salary = int(input("Enter employee's salary: "))
    join_date = datetime.today().strftime('%Y%m%d')

    employee_dict[employee_id] = {
        'username': username,
        'join_date': join_date,
        'gender': gender,
        'salary': salary
    }
    print("Employee added successfully!")
# Display all number 3
def display_all_employees():
    sorted_employees = sorted(employee_dict.items(), key=lambda x: x[1]['join_date'], reverse=True)
    for emp_id, emp_data in sorted_employees:
        print(f"{emp_id}: {emp_data['username']} - {emp_data['gender']} - {emp_data['salary']}")
# Change salary function
def change_salary():
    employee_id = input("Enter employee's ID: ")
    if employee_id in employee_dict:
        new_salary = int(input("Enter new salary: "))
        employee_dict[employee_id]['salary'] = new_salary
        print("Salary changed successfully!")
    else:
        print("Employee not found.")
# Remove Employee from dictionary
def remove_employee():
    employee_id = input("Enter employee's ID: ")
    if employee_id in employee_dict:
        del employee_dict[employee_id]
        print("Employee removed successfully!")
    else:
        print("Employee not found.")
# Raise Employee Salary
def raise_salary():
    employee_id = input("Enter employee's ID: ")
    if employee_id in employee_dict:
        raise_percentage = float(input("Enter raise percentage (e.g., 1.05 for 5%): "))
        employee_dict[employee_id]['salary'] *= raise_percentage
        print("Salary raised successfully!")
    else:
        print("Employee not found.")
# Save the Dictionay to the text file employeedatabase.txt 
# after exiting the system
def save_to_file():
    with open('employeedatabase.txt', 'w') as file:
        for emp_id, emp_data in employee_dict.items():
            file.write(f"{emp_id}, {emp_data['username']}, {emp_data['join_date']}, {emp_data['gender']}, {emp_data['salary']}\n")

#employee Menu
def employee_menu(username):
    while True:
        gender_prefix = "Mr." if employee_dict[username]['gender'] == "male" else "Ms."
        print(f"\nHi {gender_prefix} {employee_dict[username]['username']}!")
        print("Employee Menu:")
        print("1. Check my Salary")
        print("2. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            print(f"Your salary is {employee_dict[username]['salary']}")
        elif choice == "2":
            save_login_timestamp(username)
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please select a valid option.")
#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# To save last time the employee logged in
def save_login_timestamp(username):
    timestamp = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
    with open('employee_logins.txt', 'a') as file:
        file.write(f"{timestamp} - {username}\n")
# Call the login function to start the program
login()