from geometry_utils import area_circle, area_rectangle, area_triangle, normalize, is_float, to_float 

# Program introduce
print(f"AREA CALCULATOR\n\n")
print(f" This program will calculate the area from circles, rectangles and triangles.\n")
print(f" Needed parameter to calculate:\n\n Circle:      radius\n Rectangle:   length and width\n Triangle:    Base and Height\n")
print(f" Enter what you want to calculate and following enter the parameters. Enter 'exit' to close.\n")

# Logic
while True:

    
    # User input query
    select = input(" Form or exit: ")

    
    # Proof input and print result
    if select.lower() == "exit":
        print("\n\nBye!\n")
        break

    elif select.lower() == "circle":
        radius = normalize(input("\n Radius: "))
        if not is_float(radius):
            print(" Error radius: invalid number!\n")
            continue
        radius = to_float(radius)
        print(f" Circle-area = {area_circle(radius):.2f}\n")
    
    elif select.lower() == "rectangle":
        length = normalize(input("\n Length: "))
        width = normalize(input(" Width: "))
        if not is_float(length):
            print(" Error length: invalid number!\n")
            continue
        elif not is_float(width):
            print(" Error width: invalid number!\n")
            continue
        length = to_float(length)
        width = to_float(width)
        print(f" Rectangle-area = {area_rectangle(width):.2f}\n")
    
    elif select.lower() == "triangle":
        base = normalize(input("\n Base: "))
        height = normalize(input(" height: "))
        if not is_float(base):
            print(" Error base: invalid number!\n")
            continue
        elif not is_float(height):
            print(" Error height: invalid number!\n")
            continue
        base = to_float(base)
        height = to_float(height)
        print(f" Triangle-area = {area_triangle(base, height):.2f}\n")
    
    
    # Error message
    else:
        print(" Pleas write circle, rectangle or triangle, to calculate something!\n")
        continue

input("\nPress Enter to Finish...")