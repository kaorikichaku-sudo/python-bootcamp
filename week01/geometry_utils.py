import math

# Define math functions

def area_circle(radius=1):
    return math.pi * (radius ** 2)

def area_rectangle(length, width):
    return length * width

def area_triangle(base, height):
    return (base * height) / 2

# Define logic functions

def normalize(value):
    return value.replace(",", ".").strip()

def is_float(value):
    try:
        float(value)
        return True
    except ValueError:
        return False
    
def to_float(value):
    try:
        return float(value.strip())
    except ValueError:
        return None
