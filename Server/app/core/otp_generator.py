import math, random

def generate_otp():
    digits = random.random() * 1000000
    otp = round(digits)
    return otp
