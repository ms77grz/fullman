def capsy(words):
    if ' ' in words:
        return words.upper()
    else:
        return words.lower()


print(capsy('Hello world'))
print(capsy('Congratulations!'))
