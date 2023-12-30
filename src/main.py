# pip install pandas pytest

import pandas as pd

class EmployeeProcessor:
    def process_employee(self, df, employee_id):
        employee_data = df[df['employeeid'] == employee_id].iloc[0]
        return Employee(employee_data)

    def filter_employees_by_salary(self, df, min_salary):
        filtered_data = df[df['salary'] > min_salary]
        return [Employee(row) for _, row in filtered_data.iterrows()]

class Employee:
    def __init__(self, data):
        self.employee_id = data['employeeid']
        self.name = data['name']
        self.salary = data['salary']
        # Agrega más campos según tu dataset

# Prueba
if __name__ == "__main__":
    data = {'employeeid': [1, 2, 3],
            'name': ['Alice', 'Bob', 'Charlie'],
            'salary': [50000, 60000, 70000]}
    df = pd.DataFrame(data)

    processor = EmployeeProcessor()
    employee = processor.process_employee(df, 2)

    print(f"Employee ID: {employee.employee_id}")
    print(f"Name: {employee.name}")
    print(f"Salary: {employee.salary}")
