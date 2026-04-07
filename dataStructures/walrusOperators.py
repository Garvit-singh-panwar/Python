print(
'''
walrus operator is an assignment expression operator 
it allows you to assign a value to a variable within a expression
this will make your code more concise and in some case more efficient by avoiding repeated calculation or function calls

this is like usememo in react 
if it knows the value it store it inside it and dont call this function again and again to fetch same value

def heavyOperation():
    for i in range(1,1000):
        print("hello')
    return 70
if(heavyOperation() > 10 ):
    print(heavyOperation())
else:
    print("heavyOperation is less than 10)

    
what it does it print 1 to 1000 value 2 time 1st time in if condition and 2nd time inside if to print 70
we just want 70 but for that we are print 1 to 1000 two times there is no need to do that 
there we can use walrus operator it stores the value returned by function so it would not have to call it again and again for the same operation

if((a:=heavyOperation()) > 10):
    print(a)
else:
    print("Heavy opertion is < 10 ")

here a store the value 70 and dont call it again for the same value 
when we call it 2nd time it just gie us the value what it stored 

its like we prev did 

a =  heavyOperation() so the value stored inside it 
then we check the condition

like 
if(a > 10):
    print(a)
else:
    print(....)
    
''')