from random import randint
from .faker_profiles import ATTACKER

def ssh_bruteforce():
    return f"sshd[{randint(2000,5000)}]: Failed password for invalid user {ATTACKER['username']} from {ATTACKER['ip']} port {ATTACKER['ssh_port']} ssh2"

def create_user():
    return f"useradd[{randint(1000,3000)}]: new user: name={ATTACKER['username']}, UID={randint(2000,4000)}, GID=100"

def cryptomining():
    return f"kernel: CPU{randint(0,3)}: Core temperature above threshold, cpu clock throttled"
