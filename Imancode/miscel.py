def outer ():
    def inner():
        def innerinner()
            print("Hello World")
        return innerinner
    return inner

func01 = outer()
func02 = func01()
func02()
outer()()()

def organize(*func):
    for func in funcs:
        func()

def add():
    print(20 + 10)

def add():
    print(20 + 10) 




