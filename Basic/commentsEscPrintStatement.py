# comments are used to explain code and are ignored by the python interpreter.
# single-line comments start with # .
# muti-line comments are enclosed in  ''' or """
'''
this are multiline comments in python  
'''

# What are the escape sequence character 
# let say i want to print string in a new line in terminal so we cant maek a string like this
'''
str = "this is the top 
                                                                    here we leave space 
        and this is the bottom 
        "
'''
# we cant do like this
# because the python rules will not allow it 
# we can do this using escapesequence characters 
print("I want this string in \nnext line")      # \n is used as enter key for next line 
print("I want to leave a tab space \t here")    # \t is used as a tab key leave tab space
print("I want to add a backSlash n here \\n")   # \\ it is used to print backslash
print("\"I want to be inside double quotes\"")  # \" it is used to print double quote
print("\'I want to be inside single quotes\'")  # \' it is used to print single quote
# there are some arguments that we can pass in the print function for ex sep or end 
# sep means space what do you want instead of space do you want , or do you wnat any character
# end means end what do you want in the end you want a new line or a space 
# ex 
print("hello world" ,"myself : garvit" ,"age:22");
# here you can notice we seprate them with , but we havent add space between them but they automatically add space because of sep 
print("now we use sep=\",\" in the 1st print and end=\" \" in the 2nd print")
print("I am 1st print part 1" , "I am 1st print part 2" , sep=",")
print("I am 2nd print", end=" ")
print("I am 3rd print")