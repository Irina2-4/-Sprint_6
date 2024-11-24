from helpers.data import Order
import random

def generate_name():
    return random.choice(Order.name)

def generate_last_name():
    return random.choice(Order.lastname)

def generate_address():
    return random.choice(Order.address)

def generate_metro():
    return random.choice(Order.metro)

def generate_days():

    return random.choice(Order.days)

def generate_phone():
    return random.choice(Order.phone)

def generate_rent_date():
    return random.choice(Order.rent_date)

def generate_color():
    return random.choice(Order.color)

def generate_comment():
    return random.choice(Order.comment)
