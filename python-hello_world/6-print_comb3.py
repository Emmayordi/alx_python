for tens_digit in range(10):
    for ones_digit in range(tens_digit + 1, 10):
        combination = "{:02d}".format(tens_digit * 10 + ones_digit)
        print(combination, end=", " if ones_digit < 9 else "\n", flush=True)
