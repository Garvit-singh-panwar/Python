print('''
        map filter and reduce they all are higher order functions 
        they operate on iterables 
      
      numbers = [1,2,3,4,5,6,7]
      def square(a):
          return a*a
      
      new = list(map(square,numbers))
      print(new)
      ''')
numbers = [1,2,3,4,5,6,7]
def square(a):
    return a*a
      
new = list(map(square,numbers))
print(new)

print('''
    def is_greater_than_9(x):
        return True if x > 9 else False

    a =[1,2,5,235,34,32,6543,23,2,5,6,7,43]
    new = list(filter(is_greater_than_9,a))
    ''')

def is_greater_than_9(x):
    return True if x > 9 else False

a =[1,2,5,235,34,32,6543,23,2,5,6,7,43]
new = list(filter(is_greater_than_9,a))

print(new)

print('''

    def sum(a,b):
      return a+b

      c = reduce(sum ,a)

      print(c)     

''')
from functools import reduce

def sum(a,b):
    return a+b

c = reduce(sum , a)
print(c)  