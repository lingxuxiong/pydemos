# Examples from python programming tutorial, for more details check
# https://www.programiz.com/python-programming#learn-python-tutorial

def greets(*names, message='How are you'):
    '''Greet each one in the variable args with the passed in message.'''
    # print(type(names)) -> tuple

    for name in names:
        print('Hello {name}, {msg}'.format(name=name, msg=message))
    return


def greet(name='someone', message='how are you'):
    '''
    Greet someone with the provided message. 
    If no argument provided, the default one will be used instead.
    '''
    print('Hello {0}, {1}'.format(name, message))


def greeting(name):
    '''Greet someone'''
    print('Hello {}'.format(name))


def helloPython():
    '''docString'''
    print('Hello Python!')
    return


def testForFlow():
    '''docString'''
    colors = ['red', 'blue', 'yellow']
    print(colors)
    for color in colors:
        if color == 'red':
            print('I am red')
        print(color)
    return


def double(num):
    '''This is the doc string of function double'''
    print(double.__doc__)
    return 2 * num


def printDic():
    '''docString'''
    dic = {1: 'a', 2: 'b'}
    for t in dic:
        print('dic[{}]={}'.format(t, dic[t]))
    return


def sum():
    '''docString'''
    numbers = [6, 5, 3, 8, 4, 2, 5, 4, 11];
    sum = 0
    for val in numbers:
        sum += val
    print('sum=', sum)
    return sum


def testRange():
    '''docString'''
    r = range(1, 12, 2)
    print(r, type(r), len(r))
    return


def conditionForFlow():
    '''docString'''
    genre = ['pop', 'rock', 'jazz']
    print(type(genre))

    breakCondition = 'i >= 3'
    for i in range(len(genre)):
        print('genre[{}]={}'.format(i, genre[i]))
        if (eval(breakCondition)):
            print('break when {breakCondition}'.format(breakCondition=breakCondition))
            break
    else:
        print('out of for loop.')

    return


def vowelTest():
    '''docString'''
    vowels = 'aeiouAEIOU'
    ch = ''
    while True:
        ch = str(raw_input('Input a character:'))
        if ch in vowels:
            break
        else:
            print('{} is not a vowel'.format(ch))

    print('Thanks you')
    return


def absolute_value(value):
    '''Get absolute value of the passed in parameter'''

    if (value >= 0):
        return value
    else:
        return -value


def calc_factorial(x):
    '''
    This function calcuate the factorial of an integer in an recursive way.
    '''

    if (x == 1):
        return 1

    return (x * calc_factorial(x - 1))


print('End of file! Python is so cool!')
