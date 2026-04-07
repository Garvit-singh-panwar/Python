print(''' Dunder methods are short form of double underscore methods like __init__ , __str__ , __add__ and many more
      All these methods allow you to define how your object interact with built in python operators functions and language constructs 
      

      class Employee:
        def __init(self,name,salary):
            self.name = name
            self.salary = salary
        def __str__(self):
            return f\"the name is {self.name\} and the salary is { self.salary \}\"
        def __repr__ (self):
            return f\" name : {self.name} \\n salary: {self.salary} \"
        def __len__(self):
            return len(self.name)

      e = Employee("garvit" , 100000)
      print(e.name , e.salary) :-  garvit 100000
      print(str(e)) :-  the name is garvit and the salary is 100000
      print(repr(e)) :- name : garvit  
                        salary: 100000  
      print(len(e) ) :- len(self.name) :- 6
    ''')
