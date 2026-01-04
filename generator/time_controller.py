from random import randint

def generate_kernel_time():
    return f"[   {randint(10,5000)}.{randint(100000,999999)}]"
