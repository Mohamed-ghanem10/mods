def vowels_count(x):
    vowels = "AEIOUaeiou"
    counter = 0 

    for char in x:
        if char in vowels:
            counter += 1  

    print(f"Vowels count is {counter}")
    return True


def i_count(x):
    print("Positions of 'i':")
    for i in range(len(x)):
        if x[i] == 'i'or x[i] == "I":
            print(i)
    return
