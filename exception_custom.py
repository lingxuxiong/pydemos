# define Python user-defined exceptions
class Error(Exception):
    '''Base class for other exceptions'''
    pass


class ValueTooSmallError(Error):
    '''Raised when the input value is too small'''
    pass


class ValueTooLargeError(Error):
    '''Raised when the input value is too large'''
    pass


# Our main program
# User guesses a number untill he/she gets it right.

# You need to guess this number
number = 10

while True:
    try:
        iNum = int(input('Enter a number:'))
        if iNum < number:
            raise ValueTooSmallError
        elif iNum > number:
            raise ValueTooLargeError
        break
    except ValueTooSmallError:
        print('This value is too small, try again!')
        # traceback.print_exc()
    except ValueTooLargeError:
        print('This value is too large, try again!')
        # traceback.print_exc()
print('Congratuations! You guessed it correctly.')
