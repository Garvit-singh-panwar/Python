print("conditional statements are control structures which runs based on some condition "," if the condition is met it will show some result ","else it will give another result  " , sep="\n", end="\n\n")

print("the conditional statements in python are :- ")
print("if , else , elif , match " , end="\n\n")

print(  "if" ,
        "● Checks a condition.",
        "● If the condition is true, the code inside the if block runs.",
        "else",
        "● Runs when the if condition is false.",
        "● Provides an alternative block of code.",
        "elif (short for else if)",
        "● Used when you want to test multiple conditions.",
        "● If the first if is false, Python checks the elif conditions one by one.",
        "match",
        "● Introduced in Python 3.10.",
        "● Works like switch-case in other languages.",
        "● Compares a variable against different cases and executes the matching block.",
        sep="\n"
    )

x = int( input("Enter the value of x between 0 and 30"))

if x > 20:
    print("x is greater than 20")
elif x > 10:
    print("x is greater than 10 and lower than 20")
else:
    print("x is 10 or less")

# Using match

x = int(input("Enter the value of x again "))

match x:
    case 5:
        print("x is 5")
    case 15:
        print("x is 15")
    case _:
        print("x has some other value")
