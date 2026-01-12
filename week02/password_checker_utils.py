# # Functions

def check_stenght(password):
    # Error messages
    error_to_short = "\n Please use at least 8 Charackters.\n"
    error_min_required = "\n Please meet the minimum required criteria. Enter 'rules' to review them again.\n\n"
    error_rules = (
    "\n"
    " Min. 1 Number\n"
    " Min. 1 Capital letter\n"
    " Min. 1 lowercase letter\n"
    " Min. 1 special character\n\n"
    )
    
    # Variables
    strength = 0
    length = 0
    num_count = 0
    cap_count = 0
    low_count = 0
    special_count = 0

    # Check User Password Chars
    for i in password:
        length += 1

        if i.isdigit():
            num_count += 1
        elif i.isupper():
            cap_count += 1
        elif i.islower():
            low_count += 1
        elif i in "!@#$%^&*()-_=+?":
            special_count += 1
        else:
            continue
    
    # Check minimum reguired criteria
    if length < 8:
        return error_to_short
    elif not all((num_count, cap_count, low_count, special_count)):
        return error_min_required
    
    # Check Strength
    if length >= 8:
        strength = 1
    if length >=10:
        strength = 2
    if length >= 14:
        strength = 3

    # Return results
    if strength == 1:
        return "\n Weak\n"
    elif strength == 2:
        return "\n Medium\n"
    elif strength == 3:
        return "\n Strong\n"
    else:
        return error_rules
    
def rules():
    print(
        f"\n"
        f" Min. 1 Number\n"
        f" Min. 1 Cap\n"
        f" Min. lower\n" 
        f" Min. 1 Special Charackter\n"
        f"\n"
        f" WEAK   = Min. Criteria\n"
        f" MEDIUM = Min. Criteria and at least 10 chars\n"
        f" STRONG = Min. Criteria and at least 14 Chars\n\n"
    )