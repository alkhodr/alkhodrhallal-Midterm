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