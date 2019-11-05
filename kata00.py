def kata00():
    """Formats strings."""

    t = (19, 42, 21)
    # kata = "The {} numbers are: {}".format(len(t), ', '.join([str(each) for each in t]))
    kata = "The {} numbers are: {}".format(len(t), ', '.join(map(str, t)))
    # print(str(t)[1:-1])
    print(kata)


if __name__ == "__main__":
    kata00()
