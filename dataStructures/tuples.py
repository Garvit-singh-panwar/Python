print(''' Tuples are ordered but immutable collections in python means we cannot change them 
      some times we want our collection to never change
      at times we can  Accidentally change our collections leading to disaster 
      to avoid this problem we use tuples 

      me can make tuples just like lists just changing the bracket in which we initalize value we use ( ) brackets
      tupleName = (value1 , value2 , value3 , value 4);
      we can also say they are immutable list  we can access them same as we access list using index given inside square brackets 
      tupleName[0] = value1
      we use tuples we we dont want our collection to be accidentally change
      to make tuple with single element youhave to add , in the bracket in the end  tupleName = (value1,) 

      Tuple Unpacking 
      let say we have a tuple tu = (3,2,45);
      if i do a,b,c = tu this will simply assign 3 to a , 2 to b and 45 to c  . its like destructuring in javascript

      count method in tuple 
      using count we can find multiple occurence of a value in tuple for eg tu = (1,2,3,4,1,2,3,1,2,1,1,1)
      tu.count(1) it will return  6

      index method in tuple 
      using index method we can find first occurence of a value in tuple 
      ex tu.index(1) it will return 0

      why we use tuples ?
        they are faster than list 
        used as a dictionary keys like a maping of hash keys 
        safe from unintended modification 

    '''
    )