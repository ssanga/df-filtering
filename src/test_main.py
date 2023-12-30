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

    def test_process_employee_1(self):
        employee = self.processor.process_employee(self.df, 1)
        self.assertEqual(employee.employee_id, 1)
        self.assertEqual(employee.name, 'Alice')
        self.assertEqual(employee.salary, 50000)

    def test_process_employee_2(self):
        employee = self.processor.process_employee(self.df, 2)
        self.assertEqual(employee.employee_id, 2)
        self.assertEqual(employee.name, 'Bob')
        self.assertEqual(employee.salary, 60000)

    def test_process_employee_3(self):
        employee = self.processor.process_employee(self.df, 3)
        self.assertEqual(employee.employee_id, 3)
        self.assertEqual(employee.name, 'Charlie')
        self.assertEqual(employee.salary, 70000)

    def test_filter_employees_by_salary(self):
        employees = self.processor.filter_employees_by_salary(self.df, 65000)
        
        self.assertEqual(len(employees), 1)
        self.assertEqual(employees[0].employee_id, 3)
        self.assertEqual(employees[0].name, 'Charlie')
        self.assertEqual(employees[0].salary, 70000)

if __name__ == '__main__':
    unittest.main()

