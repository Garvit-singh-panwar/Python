# A decorator is just a special function that can add extra features to another function without changing its actual code.

# Think of it like wrapping a gift: the gift (original function) stays the same, but the wrapping (decorator) adds something extra (like a ribbon or message).

def say_hello_w():
    print("hello")

say_hello_w()

# let say i want to add something before calling this function and also do something after its been called so what should i do here we use decorators 

# decorator is a function that takes a function as a argument 
# create a new function inside its body (wrapper)
# then it returns that new function 
def decorator(func):
    def wrapper():
        print("I am about to execute a function.... ")
        func()
        print("I have executed this function......")
    return wrapper

@decorator
def say_hello():
    print("Hello!")


say_hello()

# instead of doing this we can add @decorator at the top of sayhello function
# f = decorator(say_hello)
# f()


# How decorators work with arguments 

def repeat(n):
    def decorator(func):
        def wrapper(a):
            for i in range(n):
                func(a)
        return wrapper
    return decorator


# repeat(n) → This is a decorator factory. It takes a number n and returns a decorator.

# decorator(func) → This is the real decorator. It takes a function and wraps it.

# wrapper(a) → This is the wrapper function. It replaces the original function, but inside it, the original function is still called.

# superpower here → The wrapper adds extra behavior (calling the function multiple times).


@repeat(7)
def sayhello(a):
    print(f"Hello! {a}")

sayhello("garvit")