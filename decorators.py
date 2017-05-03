def decorator_for_all(func):
    def inner(*args, **kwargs):
        print('Decorate here.')
        return func(*args, **kwargs)

    return inner


def inc(x):
    return x + 1


def dec(x):
    return x - 1


def operate(fun, x):
    return fun(x)


result = operate(dec, 1)
print(result)


# -------------------------------------------------

def smart_divide(func):
    def inner(a, b):
        print("I am going to divide", a, "and", b)
        if b == 0:
            print("Whoops! cannot divide")
            return

        return func(a, b)

    return inner


@smart_divide
def divide(a, b):
    return a / b


print(divide(2, 5))


# -------------------------------------------------

def ordinary():
    print('I am ordinary')


def make_pretty(func):
    def inner():
        print('I am decorated')
        func()

    return inner


pretty = make_pretty(ordinary)
pretty()


def make_pretty2(func):
    def inner(msg):
        print(msg, 'was decorated')
        func(msg)

    return inner


@decorator_for_all
def ordinary2(msg):
    print(msg)


ordinary2('Hello Python')


# --------------------------------------------------
def star(func):
    def inner(*args, **kwargs):
        print("*" * 30)
        func(*args, **kwargs)
        print("*" * 30)

    return inner


def percent(func):
    def inner(*args, **kwargs):
        print("%" * 30)
        func(*args, **kwargs)
        print("%" * 30)

    return inner


@star
@percent
def printer(msg):
    print(msg)


printer("Hello")
