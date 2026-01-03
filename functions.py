def add(a, b):
    return a + b

def subtract(a, b):
    return a - b  # <--- fix this in step 7

def multiply(a, b):
    return a * b

def convert_fahrenheit_to_celsius(f):
    # Absolute zero in Fahrenheit is -459.67
    assert f >= -459.67, "Temperature below absolute zero"
    return (f - 32) * 5 / 9 # <-- Fix this in step 7