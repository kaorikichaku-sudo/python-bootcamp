from number_analysis_utils import number_count, number_addition, number_average, number_max_min, convert_to_float 

print(" NUMBER ANALYSIS\n\n")

print(f" Enter:\n Number -> Add to the analysis-list\n Stop -> to analyse and finish\n\n")

numbers = []

while True:
    user_input = input(" Number or 'Stop': ")
    
    


    if user_input.lower() == "stop":
        if not numbers:
            print("Please enter minimum one number.\n\n")
            continue

        numbers_count = number_count(numbers)
        result = number_addition(numbers)
        average = number_average(numbers_count, result)
        largest, smallest = number_max_min(numbers)

        print(f"\n\n Count: {numbers_count}\n Result: {result:.2f}\n Average: {average:.2f}\n Smallest: {smallest:.2f}\n Largest: {largest:.2f}\n\n")
        break
    
    else:
        user_float = convert_to_float(user_input)
        if user_float == None:
            continue
        else:
            numbers.append(user_float)

input(" Press Enter to close...")
        



