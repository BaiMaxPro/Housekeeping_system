from faker import Faker
import random

fake = Faker("zh_CN")
def rand_gender():
    return random.choice(("男","女"))
