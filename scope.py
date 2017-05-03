def outer_function():
    b = 20

    def inner_func():
        c = 30
        b = 21
        print(b)

    inner_func()
    print(b)


a = 10
print(a)

outer_function()
