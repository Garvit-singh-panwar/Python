print(
        "Loops are used to repeatedly do a task based on some condition " ,
        "If the condition is true do it again ",
        "if the condition is false stop ",
        sep="\n", end="\n\n"
    ) 

print("Enter number from where to where you want to print numbers ")
x = int(input("give the starting number "))
y = int(input("give the ending number "))

for i in range(x , y):
    print(i)

print("range function excludes the second parameter thats why it is printing from " ,x , " to ", y ,"-1 ")

print()
print("Now we are printing 1 to 5 using while loop")
i =1
while i < 6:
    print(i)
    i += 1 