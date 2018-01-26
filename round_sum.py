'''
For this problem, we'll round an int value up to the next multiple of 10 if its rightmost digit is 5 or more,
so 15 rounds up to 20. Alternately, round down to the previous multiple of 10 if its rightmost digit is less than 5,
so 12 rounds down to 10. Given 3 ints, a b c, return the sum of their rounded values.
To avoid code repetition, write a separate helper "def round10(num):" and call it 3 times.
Write the helper entirely below and at the same indent level as round_sum()
Examples:
    INPUT: round_sum(16, 17, 18) OUTPUT:60
    INPUT: round_sum(12, 13, 14) OUTPUT:30
    INPUT: round_sum(6, 4, 4) OUTPUT:10
'''


def round_sum(a, b, c):
    round_a = round10(a)
    round_b = round10(b)
    round_c = round10(c)
    addition = round_a + round_b + round_c
    return addition


def round10(num):
    all_digits = []
    for d in str(num):
        all_digits.append(int(d))

    new_number = 0
    # Check for single digit number
    if len(all_digits) == 1:
        if all_digits[0] >= 5:
            new_number = 10
        return new_number
    else:
        if all_digits[1] >= 5:
            new_number = int(str((all_digits[0] + 1)) + '0')
        else:
            new_number = int(str(all_digits[0]) + '0')
        return new_number


sum = round_sum(6, 29, 38)
print(sum)
