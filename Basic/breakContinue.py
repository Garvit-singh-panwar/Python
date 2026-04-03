print("break and continue are keywords which is used to stop continious flow of loop ")
print("for ex you want to stop loop based on some condition you use break")
print("when you want to skip some iteration based on some condition you use continue")

print()

print("Enter number from where to where you want to print numbers ")
x = int(input("give the starting number "))
y = int(input("give the ending number "))

a = int(input("now  give me a number where you want to stop loop "))
b = int(input("give me a number which you want to skip in this sequence "))


for i in range(x,y):
    if(i == a):
        break
    if(i == b):
        continue
    print(i)

print()
print("now we talk about another keyword pass");
print("when you want somewhere to write code later you will write pass there means do nothing it just skip  that place")
print("for ex you define a function if you write nothing inside it it will throw error,",
       "so you will write pass there so it will no throw error", 
       "because you mentioned there do nothing (pass) ",
       sep="\n"
    )