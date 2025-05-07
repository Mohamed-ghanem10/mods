def listed(x):
    x = int(x)
    if x <= 0:
        print("Please enter a positive number.")
        return False

    table = [[i * j for j in range(1, i + 1)] for i in range(1, x + 1)]
    print(table)
    return True


def triangle(x):
    x = int(x)
    if x <= 0:
        print("Please enter a positive number.")

    for i in range(1, x + 1):
        row = [f"{i}x{j}={i * j}" for j in range(1, i + 1)]
        print(" ".join(row))
    return True
