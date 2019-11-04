import sys

if __name__ == "__main__":

    ret = []
    for each in sys.argv:
        ret.append(each.swapcase())
    ret.reverse()
    ret = ret[:-1]
    output = " ".join(ret)
    print(''.join(reversed(output)))
