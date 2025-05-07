def string(x):
    x = int(x)
    for i in range(1, x + 1):
        print(' ' * (x - i) + '*' * i)
    return True

    
def listed(x):
    x = int(x)
    L = [' '] * x
    for _ in range(x):
        L.append('*')
        L.pop(0)
        print(L)
    return True
