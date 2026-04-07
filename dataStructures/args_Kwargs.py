def sum(*args):
    # here args will be the tuple of all the values passed to sum 
    total = 0 
    for items in args:
        total+=items
    return total


def marks(**kwargs):
    total = 0
    # here kwargs is a dictionary with all the key value pairs passed to the marks
    for keys in kwargs.keys():
        total += kwargs[keys]
    return total

print(sum(342,2,7,9))
print( marks( c=75 , cpp = 85 , java = 75 , javascript = 95 , react = 95 )) 

def func1(*args,**kwargs):
    print(args)
    print(kwargs)

func1(1,2,3,4,5,6,7 ,c=75 , cpp = 85 , java = 75 , javascript = 95 , react = 95)