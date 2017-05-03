import sys
import traceback

args = ['a', 0, 2.0]

for a in args:

    try:
        print('entry value:', a)
        r = 1 / int(a)
        break
    except:
        print('encountered exception:', sys.exc_info()[0])
        print('Next entry')
        print()
print('reciprocal of ', a, ' is ', r)

try:
    a = int(input('Enter a positive value here:'))
    if a <= 0:
        raise ValueError('value should be positive!')
    print(a)
except ValueError as ve:
    print(ve)
    traceback.print_exc()
