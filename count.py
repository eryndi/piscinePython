import string


def text_analyzer(text=""):
    """This function counts the number of upper characters, lower characters, punctuation and spaces in a given text."""
    if not text:
        text = input("What is the text to analyse?")

    print("The text contains {} characters".format(len(text)))

    upper = sum(letter.isupper() for letter in text)
    print("- {} upper letters".format(upper))

    lower = sum(letter.islower() for letter in text)
    print("- {} lower letters".format(lower))

    space = sum(letter.isspace() for letter in text)
    print("- {} spaces".format(space))

    punctuation = len([letter for letter in text if letter in string.punctuation])
    print("- {} punctuation marks".format(punctuation))


if __name__ == "__main__":
        text = "Python is an interpreted, high-level, general-purpose programming language. Created by Guido van Rossum and first released in 1991, Python's design philosophy emphasizes code readability with its notable use of significant whitespace."
        text_analyzer(text)
