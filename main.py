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

    for _ in range(max_attempts):
        username = input("Username: ")
        password = input("Password: ")

        if username == admin_username and password == admin_password:
            print("Welcome, Admin!")
            admin_menu()
            break
        elif password == "":
            if username in employee_dict:  # Check if username exists in employee_dict
                print(f"Welcome, Mr. {employee_dict[username]['username']}!")
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