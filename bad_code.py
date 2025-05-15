# bad_code.py

# === Reliability Issue: Using a risky function (eval) ===
def run_code(code_str):
    return eval(code_str)

# === Duplications: Repeated code ===
def get_discount(price):
    discounted_price = price - (price * 0.1)
    print("Discounted price is", discounted_price)
    return discounted_price

def apply_discount(price):
    discounted_price = price - (price * 0.1)
    print("Discounted price is", discounted_price)
    return discounted_price

# === Maintainability Issue: Long method with code smells ===
def process_user(user):
    if user == "admin":
        print("Admin logged in")
        # do admin stuff
    elif user == "guest":
        print("Guest logged in")
        # do guest stuff
    elif user == "member":
        print("Member logged in")
        # do member stuff
    elif user == "member":  # Duplicate condition (bug-prone)
        print("Duplicate check")
    else:
        print("Unknown user")

    # Deeply nested if block
    if user:
        if user.startswith("a"):
            if len(user) > 5:
                print("Name starts with A and is long")

    temp = []  # Unused variable
