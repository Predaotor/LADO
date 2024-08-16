import csv

def read_employees(csv_file_name):
    try:
        csv.register_dialect("empDialect", skipinitialspace=True, strict=True)
        with open(csv_file_name, mode='r') as file:
            employee_file = csv.DictReader(file, dialect="empDialect")
            employee_list = [dict(data) for data in employee_file]
        return employee_list
    except FileNotFoundError:
        print(f"Error: The file '{csv_file_name}' was not found.")
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")
    return []

def process_data(employee_list):
    try:
        department_list = [employee_data['Department'] for employee_data in employee_list]
        department_data = {department_name: department_list.count(department_name) 
                           for department_name in set(department_list)}
        return department_data
    except KeyError as e:
        print(f"Error: Missing key in employee data - {e}")
    except Exception as e:
        print(f"An error occurred while processing the data: {e}")
    return {}

def generate_report(dictionary, report_file):
    try:
        with open(report_file, "w") as f:
            for k in sorted(dictionary):
                f.write(f"{k}: {dictionary[k]}\n")
        print(f"Report successfully generated and saved to '{report_file}'.")
    except Exception as e:
        print(f"An error occurred while writing the report: {e}")

if __name__ == "__main__":
    employee_list = read_employees("employees-with-date.csv")
    if employee_list:
        department_data = process_data(employee_list)
        if department_data:
            generate_report(department_data, "report.txt")
