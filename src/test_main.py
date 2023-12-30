import unittest
import pandas as pd
from main import EmployeeProcessor

class TestEmployeeProcessor(unittest.TestCase):
    def setUp(self):
        data = {'employeeid': [1, 2, 3],
                'name': ['Alice', 'Bob', 'Charlie'],
                'salary': [50000, 60000, 70000]}
        self.df = pd.DataFrame(data)
        self.processor = EmployeeProcessor()

    def test_get_employee_by_id(self):
        employee = self.processor.get_employee_by_id(self.df, 1)
        self.assertEqual(employee.employee_id, 1)
        self.assertEqual(employee.name, 'Alice')
        self.assertEqual(employee.salary, 50000)

    def test_process_non_existing_employee(self):
        employee = self.processor.get_employee_by_id(self.df, 4)
        self.assertIsNone(employee)  # Espera que sea None para un employee_id que no existe

    def test_filter_employees_by_salary(self):
        employees = self.processor.filter_employees_by_salary(self.df, 65000)
        
        self.assertEqual(len(employees), 1)
        self.assertEqual(employees[0].employee_id, 3)
        self.assertEqual(employees[0].name, 'Charlie')
        self.assertEqual(employees[0].salary, 70000)

    def test_query_data(self):
        condition = 'salary > 60000'
        queried_employees = self.processor.query_data(self.df, condition)

        self.assertEqual(len(queried_employees), 1)
        self.assertEqual(queried_employees[0].employee_id, 3)
        self.assertEqual(queried_employees[0].name, 'Charlie')
        self.assertEqual(queried_employees[0].salary, 70000)

if __name__ == '__main__':
    unittest.main()

