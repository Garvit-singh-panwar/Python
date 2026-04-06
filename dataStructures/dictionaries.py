print(
    '''
    dictionaries are key value pairs and allow fast lookups it stores data like a json file
    we create a dectionary like this 
    Syntax 
    variableName = { \"key1\": \"value1\" , \"key2\": \"value2\"  } 

    whenever we create a dictionary as any data type as key and any datatype as value 
    the only thing is the key that you are using should be hashable 
    A hashable object is one that can be given a unique “ID number” (called a hash) that never changes while the object exists.
    means python should be able to hash that datatype internally so 
    strings , integers and tuples are hashable
     
    
    we can access dictionaries like this  variableName[key] it maps the key in the dictionary and gives you the value 
    a dictionary also have a lot of method 
    we can change value in dictionary like this 
    variableName[key] = newValue  thats how you can change  the content of a dictionary

    Common dictionary methods
    let say we want to print all the keys of a dictionary 
    print(dictionaryName.keys())

    dictionaryName.values() gives all the values of the dictionary

    you can also pop a key from dictionary
    .clear() method remove all the keyvalue pairs from the dictionary 
    .pop("key") remove that key and value from the dictionary 

    Dictionary comprehensions :-

    let say we want table of 5 
    table_of_5 = {i : 5*i for i in range(1,11) }
     
    '''
    )