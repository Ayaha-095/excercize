beforeChar: str = ''

while True:
    beforeChar = input('Please input :')

    if beforeChar.islower():
        print(beforeChar.upper())
    elif beforeChar.isupper():
        print(beforeChar.lower())
