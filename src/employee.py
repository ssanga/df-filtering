class Employee:
    def __init__(self, data):
        self.employee_id = data['employee_id']
        self.name = data['name']
        self.salary = data['salary']
        # Agrega más campos según tu dataset