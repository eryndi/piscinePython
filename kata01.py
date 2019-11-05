def kata01():
    """Formats strings."""

    languages = {
        'Python': 'Guido van Rossum',
        'Ruby': 'Yukihiro Matsumoto',
        'PHP': 'Rasmus Lerdorf',
    }

    for key, value in languages.items():
        kata = "{} was created by {}".format(key, value)
        print(kata)


if __name__ == "__main__":
    kata01()

