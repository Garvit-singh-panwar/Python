print("when a function call it again and again wsing it self or with the help of another function in a function call we call that recursion ")

print("""
    for ex this function is calling itself again and again by changing its value inside it  
    def fibonachi(n):
        if(n==0 or n==1):
            return n
        
        val = fibonachi(n-1)+fibonachi(n-2);
        return val
""")

a = int(input("Give me a number whose fibonachi you want to find "))
def fibonachi(n):
    if(n==0 or n==1):
        return n
        
    val = fibonachi(n-1)+fibonachi(n-2)
    return val

print( "\n",fibonachi(a), f" : this is the fibonachi of {a}" )