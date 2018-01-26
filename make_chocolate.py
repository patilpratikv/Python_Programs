'''
We want make a package of goal kilos of chocolate. We have small bars (1 kilo each) and big bars (5 kilos each).
Return the number of small bars to use, assuming we always use big bars before small bars.
Return -1 if it can't be done.
INPUT:make_chocolate(4, 1, 9) OUTPUT:4
INPUT:make_chocolate(4, 1, 10) OUTPUT:-1
INPUT:make_chocolate(4, 1, 7) OUTPUT:2
'''


def make_chocolate(small, big, goal):
    big_kilo_range = range(1, big + 1)
    for i in big_kilo_range:
        big_kilos = big_kilo_range[i-1] * 5
        if (big_kilos + small) >= goal:
            return goal - big_kilos
    return -1


count = make_chocolate(4, 4, 15)
print(count)

