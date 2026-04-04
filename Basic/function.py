print("In python we can define a function using def keyword  def functionName(parameters): " ,
      "return  is a keyword used to return the value of function",
      "we made a function to add 2 numbers ",
      sep="\n"
    )

a = ("enter a num num1 ")
b = ("enter another number num2")

def add(a,b):
    return a+b

print(add(a,b) , "this is the result what we got after the addition")
print("function is reusable block of code ",
      "we have to define a function once and we can use it again and again in our code",
      "the agruments which we pass in function the function creates the cope of that agrument and store it in its variable",
      "then do some operation on them and return the result ",
      "the result doesn't affect the original variable value",
      "in function there are different types of arguments it depends on the way of writing parameters of a function ",
      "1 : positional arguments  def funName(a , b ): ",
      "2 : default argument def funName(a,b,plus=0)  here in function call passing this agrument is not necessary",
      "because we gave a default agrument to it and if we pass that argument in the function call it replaces the default agrument with it ",
      "eg: funName(1,2,3)  plus becomes 3 now",
      "3 : keyword argument means defining the argument in the function call what you are passing ",
      "like funName(a=4,b=7) ",
      "Lambda function in python ",
      "lambda functions are the one liner functions here we use lambda as keyword  sum = lambda x: x+y ",
      "we can call it like this sum(x,y)"  ,
      "they are simply use for convinence "


      )