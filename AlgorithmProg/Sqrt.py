# Write a static function sqrt to compute the square root of a nonnegative number c
# given in the input using Newton's method:
# -------------------------------------------------------------------------------------
# Function for squareroot


def sqrt(c, e):
    # Newtons method
    t = c
    while abs(t - c / t) > e:
        t = (c / t + t) / 2
    return t


if __name__ == '__main__':
    epsilon = 1 * 10 ** -15
    positive_int = int(input("Enter a positive number"))
    # checks weather given num is positive or not
    if positive_int <= 0:
        print("Number cant be negitive or zero:")
        positive_int = int(input("Enter a positive number"))

    print("Squareroot of number is: ", sqrt(positive_int, epsilon))
