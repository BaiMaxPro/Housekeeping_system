from backend.employee.model import Employee
from backend.session.model import User

from backend.generator_utils import fake, rand_gender
from backend.session.generator import employee_ids

employees = (
    (i, fake.name(), rand_gender(), fake.phone_number()) for i in employee_ids
)

EmployeesGenerator = (
    Employee.new_employee(id, name, gender, tel) 
    for id, name, gender, tel in employees
)
