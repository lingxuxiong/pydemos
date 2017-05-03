def myGenerator():
    n = 1
    print('yield with n=', n)
    yield n

    n += 1
    print('yield with n=', n)
    yield n

    n += 1
    print('yield with n=', n)
    yield n


def reverseString(str):
    length = len(str)
    for i in range(length - 1, -1, -1):
        print(str[i])


def powerOfTwoGenerator(max=0):
    n = 0
    while n <= max:
        yield 2 ** n
        n += 1
