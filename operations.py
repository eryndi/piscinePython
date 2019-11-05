import sys


def math_operations(one, two):
    """
    Elementary math operations.

    Prints results of the four elementary mathematical operations of arithmetic
    (addition, subtraction, multiplication, division) and the modulo operation.
    Takes 2 numbers as parameters and returns 5 values.
    """
    print("Sum         {}".format(sum([one, two])))
    print("Difference  {}".format(one - two))
    print("Product     {}".format(one * two))
    if two == 0:
        print("Reminder    ERROR (div by zero)")
        print("Quotient    ERROR (modulo by zero)")
    else:
        print("Reminder    {}".format(one % two))
        print("Quotient    {}".format(one / two))


if __name__ == "__main__":

    if len(sys.argv[1:]) != 2:
        raise Exception("InputError: wrong number of arguments. \
Usage: python operations.py Example: python operations.py 10 3")
    if sum(each.isdigit() for each in sys.argv[1:]) != 2:
        raise Exception("InputError: arguments are not numbers or are not positive or whole numbers. \
Usage: python operations.py Example: python operations.py 10 3")

    one, two = sys.argv[1:3]
    math_operations(int(one), int(two))
