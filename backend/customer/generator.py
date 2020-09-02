from backend.customer.model import Customer
from backend.session.model import User

from backend.generator_utils import fake, rand_gender
from backend.session.generator import customer_ids

customers = (
    (i, fake.name(), rand_gender(), fake.phone_number(), fake.address()) for i in customer_ids
)

CustomersGenerator = (
    Customer.new_customer(id, name, gender, tel, address) 
    for id, name, gender, tel, address in customers
)
