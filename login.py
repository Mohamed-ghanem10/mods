def valid(DB, user, password):

    user_found = None
    for u in DB:
        if u["name"] == user:
            user_found = u
            break

    if not user_found:
        print("Username not found!")
        return False

    if user_found["password"] == password:
        print("Login successful!")
        return True
    else:
        print("Incorrect password!")
        return False