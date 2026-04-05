print('''python provides powerful built in data structures to store and manipulate collections of data efficiently 
      1. Lists and list methods 
      list are like arrays 
      sometimes you want to store multiple variable inside single variable name 
      lists are ordered mutable collections of items 
      means we can add something in the list we can remove something from the list 

      syntax
      ListName = [23 ,44,True , False , "Hello"]
      and we can access them using there index like are like array in javascript where we can store multiple datatypes in the same array
      index starts from 0 and goes to list length - 1 here the list length is 5 but last index is 4
       ListName[0] = 23 , ListName[1] = 44 , ListName[2] = True , ListName[3] = False , ListName[5] = Hello
      
      we can also do slicing in lists we can get sublists out of list 
      

      Lists method ; - 
      
      ListName.append("newvalue") it creates a new entry in the list means adding new value in the list at last position
      now listName looks like  [23.44.true,False,"hello" ,"NewValue"]
      ListName.pop() it removes the last element from the list and return it 
      ListName.extend(otherList) it add the other list in the list name at the end of the list name
      .reverse() reverse the original list
      .sort() sort the intire list 
      .insert(index,value ) insert the value at the given index 
      .remove(index) removes the value of the given index

      
      List comprehension:- 
      let say we create a list contain table of 5 
      list1 = []

      for i in range( 1 , 11):
        list1.append(5*i)
      
      this is good but let just try list comprehension to do this
      list2 = [5*i for i in range(1 ,11)] it s just a short cut for doing that in single line 


      '''
    )