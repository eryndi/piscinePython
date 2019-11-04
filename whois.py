import sys


def what_number(num):
    if num == 0:
        return "I'm zero"
    if num % 2 == 0:
        return "I'm Even"
    else:
        return "I'm Ood"


if __name__ == "__main__":
    if str(sys.argv[1]).isnumeric():
        print(what_number(int(sys.argv[1])))
    else:
        print("ERROR")
