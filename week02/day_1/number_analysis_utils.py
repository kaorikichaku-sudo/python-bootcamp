


def number_count(numbers):
    counter = 0
    for n in numbers:
        counter += 1
    return counter


def number_addition(numbers):
    numbers_to_add = 0
    for n in numbers:
        numbers_to_add = numbers_to_add + n
    return numbers_to_add


def number_average(numbers_count, result):
    if numbers_count == 0:
        return None
    return result / numbers_count



def number_max_min(numbers):
    largest, smallest = max(numbers), min(numbers)
    return largest, smallest
    

def convert_to_float(user_input):
    try:
        return float(user_input.replace(",", "."))
    except ValueError:
        print(" This ist not a number. Please try it again.\n")
        return None
