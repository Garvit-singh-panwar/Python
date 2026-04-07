print('''# while True: 
#     try:
#         a = int(input("Enter number 1 : "))
#         b = int(input("Enter number 2 : "))
#         print(f"the  sum is { a / b }")

#     except ValueError: # this error occur ehwn datatypes is changed  
#         print("please dont perform bad typecasts")
    
#     except ZeroDivisionError:   # when a digit is divided by 0 this error occur
#         print("hey dont divide by 0")

#     except Exception as e: 
#         print("Some error occured!" , e)

#     finally : # finally is always called 
#         print("this is always executed ")

# raise is used to throw an error 

# a = int(input("Enter number 1 : "))
# b = int(input("Enter number 2 : "))

# if(b==0):
#     raise ZeroDivisionError("please dont divide it by 0")

# print(f"the  sum is { a / b }")

try: 
    a = 345/0

except Exception as e:
    print(f"this error occured due because of : -  {e}")

# else gets executed when there is no error in the try block 
else: 
    print("hey i am good")


a = int (input("Enter number 1: ))
b = int (input("Enter number 2: ))

try: 
    c = a/b
    print(c)
    
except Exception as e:
    print(e)

# this is always executed no matter if try completly execute or not
finally:
    print("this is always executed ")


    
''')