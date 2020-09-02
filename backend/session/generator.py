from uuid import uuid4
import itertools

from backend.session.model import User

from backend.generator_utils import fake

def generate_user(ids, first_username, password, role):
    for i, current_id in enumerate(ids):
        if i == 0:
            yield (current_id, first_username, password, role)
        else:
            yield (current_id, fake.user_name(), password, role)

admin_ids = [str(uuid4()) for i in range(1)]
customer_ids = [str(uuid4()) for i in range(20)]
employee_ids = [str(uuid4()) for i in range(10)]


users = itertools.chain(
    generate_user(admin_ids, "admin", "pass", "admin"),
    generate_user(customer_ids, "customer", "pass", "customer"),
    generate_user(employee_ids, "employee", "pass", "employee"),
)

UsersGenerator = (User.new_user_with_id(id, name, pwd, role) for id, name, pwd, role in users)