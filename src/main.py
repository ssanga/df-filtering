# pip install pandas pytest

import pandas as pd
from employee import Employee
from employee_processor import EmployeeProcessor

# Prueba
if __name__ == "__main__":
    data = {'employee_id': [1, 2, 3],
            'name': ['Alice', 'Bob', 'Charlie'],
            'salary': [50000, 60000, 70000],
            'department_id': [101, 102, 103]}
    df_employees = pd.DataFrame(data)

    processor = EmployeeProcessor()
    employee = processor.get_employee_by_id(df_employees, 2)

    print(f"Employee ID: {employee.employee_id}")
    print(f"Name: {employee.name}")
    print(f"Salary: {employee.salary}")

    department_data = {'department_id': [101, 102, 103],
                   'department_name': ['HR', 'Engineering', 'Finance']}
    
    df_departments = pd.DataFrame(department_data)

    # Unir los DataFrames utilizando merge
    df_merged = pd.merge(df_employees, df_departments, on='department_id')

    # Mostrar el DataFrame resultante
    print(df_merged)


    