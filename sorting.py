def numbers5():
    nums = []

    while len(nums) < 5:
        x = input(f"Enter number {len(nums) + 1}: ")

        if x.isdigit():
            nums.append(int(x))
        else:
            print("Invalid input. Please enter a valid number.")

    asc = sorted(nums)
    desc = sorted(nums, reverse=True)

    print("Ascending Ordered:", asc)
    print("Descending Ordered:", desc)

    return asc, desc