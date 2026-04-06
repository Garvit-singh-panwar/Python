print(
    '''sets are ordered unique collections (no duplication)
    here values are not repeated every value is unique

    syntax :
    setName = /{ "apple" , "mango" , "orange" /}

    print(setName , type(setName))
    we can not access them using square brackets
    when ever we add elements in sets are are stored them in random order there order are not maintain 
    means that element can be in 2nd position or in 3rd position or in last position or in first position

    to add element in the set we use .add method
    setName.add(value)
    it can be add anywhere 
    if we want to remove element from the set we use .remove method
    setName.remove(value) 

    discard method :-
    if i try to remove a element which is not present in the set it will give me error 
    but using discard method it will not if the value is present it removes the value if not it simply do nothing or say return

    pop method 
    pop method removes the random element from the set


    Set Operations:-
    Union , intersection 
    let say we have a set a  and a set b 
    if we want to store all the elements of and and b in a set we use unioun method 
    c = a.union(b) it returns set of unique elements of both set

    intersection method let say we have a set a  and a set b 
    if we want a set which contain element which is present in both a and b we use intersection 
    d = a.intersection(b)

    let say a = {1,2,3,4,5,6,7}
            b = {5,6,7,8,9,10} 

            a.union(b) = {1,2,3,4,5,6,7,8,9,10}
            a.intersection(b) = {5,6,7} 
    
    this is same as sets in mathematics 
    '''
)