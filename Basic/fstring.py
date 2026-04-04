# string formating   
template = "this is a string we are placing two string from variables first is this {} and 2nd is this "
print("do you want to place thing in a string");
a = input("give me 1st string that you want to add in my string ")
b = input("give me 2nd string that you want to add in my string " ,end="\n\n")

s1 = template.format(a,b)
print(s1);
print(
        "as you can see that your string is placed in the string ",
        "we are doing this using stringName.format(s1,s2) method",
        "here we made a varable or template where we write our string with curly braces inside it ",
        "them we call format function with that template and give strings which we want inside it as arguments" ,
        "we can do this with another method we call that f string  ",
        "when we want to use print we place a f inside it them use double quotes then give curly braces with string inside it  ",
        "ex  print(f \" write what you want and them \{ s1 \} then \{ s2\} here s1 and s2 are variables which contain some data   ) like this",
        "other functions are ort(\"A\" ) it returns the ascii value of that char in this case 65 you can not give string  ",
        "chr(65) gives us the character of the given ascii value in this case it returns A ",
        sep="\n"
        
     )


