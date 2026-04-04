name = "Garvit"
print(name)
name ='Garvit'
print(name)
name='''Garvit''' # tripple quotes are used for multi line string in python it is like a pre tag in html
print(name)

print(name[0]) # you can print characters by giving a index in []   index start form 0 to length-2 
print(name[1])
print(name[-1], end="\n\n") # index [-1] means last character or last position negative no give us the reverse means -1 means last -2 means second last like taht -3 is  3rd last 
# in positive indev means going straight and -ve index means comming back 

# slicing a string
# its like a range function in for loop  
# we can  give two index no in one index bracked saperate them with colan 
# first index no shows from which index we want string and second  index no shows to which index no we want string we exxcludes 2nd index no means when we reach that index it stops and dont give character of that index
print("now we can talk about slicing method it is used to get substring of your string")
print("[starting index : endingindex ]  it goes from starting index to ending index - 1")
# if I add colon in it and give another num as parameter 
# like this 
print("[starting index : endingindex : skipcharacter ]  it goes from parameter1st-index to parameter2nd-index - 1 ans also skip character according to what is given in third parameter it leaver skipcharacter-1 characters" , end="\n\n")

name = "this is a string and there is multiple character in it "
print(name)
a = int(input("give me the parameter 1 or 1st index from which you want the sub string "))
b = int(input("now give me the parameter 2 or 2nd index from which you want end your substring "));

print(name[a:b] , "now see the result you get this substring" , end="\n\n" ,sep="\n")

print("now we can also add the skip parameter the 3rd parameter")
a = int(input("give me the parameter 1 or 1st index from which you want the sub string "))
b = int(input("now give me the parameter 2 or 2nd index from which you want end your substring "));
c = int(input("now give me the parameter 3 or 3rd index how many character you want to leave everytime "))

print(name[a:b:c])


