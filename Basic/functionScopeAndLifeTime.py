print("In python variable have scope and lifetime variables are created when the function is called and destroyed when it return")
print(''' 
Local Scope

Variables created inside a function.
They exist only while the function runs.
You cannot use them outside.

def add(x, y):
    result = x + y   # local variable
    return result

print(add(3, 4))  # Output: 7
print(result)     # Error: result not defined
      
Global Scope :-

Variables created outside functions.
They can be used anywhere in the file.

a = 10  # global variable

def show():
    print(a)  # works fine

show()       # Output: 10
print(a)     # Output: 10
Block Scope (special in Python)

In many languages, variables inside if or for are local.
In Python, they are still accessible outside.

if True:
    x = 5
print(x)  # Output: 5 (still works!)
      
Lifetime of Variables:-
      
Lifetime means how long a variable stays in memory.
Local variables: Created when the function starts, destroyed when the function ends.
Global variables: Stay alive until the program finishes.

The global Keyword
If you want to change a global variable inside a function, you must use global.

count = 0

def increase():
    global count
    count += 1

increase()
print(count)  # Output: 1
Without global, Python thinks you are creating a new local variable.

    ''')