from employee import Employee


class EmployeeProcessor:
    def get_employee_by_id(self, df, employee_id):
        if employee_id not in df['employee_id'].values:
            return None
        
        employee_data = df[df['employee_id'] == employee_id].iloc[0]
        return Employee(employee_data)

    def filter_employees_by_salary(self, df, min_salary):
        filtered_data = df[df['salary'] > min_salary]
        return [Employee(row) for _, row in filtered_data.iterrows()]
    
    def query_data(self, df, condition):
        queried_data = df.query(condition)
        return [Employee(row) for _, row in queried_data.iterrows()]