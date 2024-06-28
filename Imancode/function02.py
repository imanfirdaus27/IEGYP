# Whenever we say function immediately we think about
# 2 Things 1) parameter 2) return
# We already know how to pass function as an argument
# Now we will learn how to return a function from another function

def authenticate(username, password):
    if (username == "admin" and password == "pwd123"):
        pass

def sum(a,b):
    return a + b

# function without name is also called annonymous function
# however if the function do not have a name how to call/ invoke them