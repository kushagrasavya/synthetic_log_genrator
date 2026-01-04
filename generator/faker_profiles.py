from faker import Faker
from random import choice

fake = Faker()

ATTACKER = {
    "username": fake.user_name(),
    "ip": fake.ipv4_public(),
    "ssh_port": choice(range(20000, 60000))
}

def random_username():
    return fake.user_name()
