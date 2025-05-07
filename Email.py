def is_valid_email(email):
    try:
        if "@" not in email or "." not in email:
            return False

        user, domain = email.split("@", 1)
        if not user or not domain:
            return False

        domain_parts = domain.split(".")
        if len(domain_parts) != 2:
            return False

        x, y = domain_parts
        if not x or not y or "." in y:
            return False

        return True
    except Exception as e:
        print("Validation error:", e)
        return False

def get_valid_email(max_attempts=3):
    for attempt in range(max_attempts):
        email = input("Enter a valid email: ")
        if is_valid_email(email):
            print("Valid email entered:", email)
            return email
        else:
            remaining = max_attempts - attempt - 1
            print(f"Invalid email. You have {remaining} tries left.")

    print("Sorry, try again later.")
    return None