# Closure is the technique by which some data ("Hello") gets attached 
# to the code, even though the data ran out of its scope or the function 
# itself is removed from the current namespace.
# check https://www.programiz.com/python-programming/closure

def outterPrintMessage(msg):

    def innerPrintMessage():
        print(msg)

    return innerPrintMessage

#closure = outterPrintMessage('Hello closue')
#closure()


def make_multiplier_of(n):
    def multiplier(x):
        return x * n
    return multiplier

# Multiplier of 3
times3 = make_multiplier_of(3)

# Multiplier of 5
times5 = make_multiplier_of(5)

# Output: 27
print(times3(9))

# Output: 15
print(times5(3))

# Output: 30
print(times5(times3(2)))