# when we say class attribute we can access them from class and we can also access them using objects
# but a instance attribute can only be access by object 
# because instance attribute is created when a object is created

class Employee:
    company = "Asus"
    def __init__(self,name ,salary):
        self.name= name
        self.salary = salary

    # this is called a instance method it is called by a object 
    def info(self):
        print(f"employee name is {self.name} and salary is {self.salary}")

    # static method  
    # to make a static method we have to add a decorator @staticmethod
    # without this decorator our method becomes instance method we have to give self inside the parameter 
    # the self is itself a object it amke the function size bigger 
    # if we dont want to give self in the parameter we have to use @staticmethod
    # static method doesn't use the instance attribute or instance method
    @staticmethod
    def sum(a,b):
        return a+b 
    
    # classmethod 
    # whenever you want to reference the class you have always use the class method 
    @classmethod
    def print_company(cls):
        # here cls is nothing but the class employee
        print(cls.company)
    
    @classmethod
    def change_company(cls,new_company):
        cls.company = new_company



print(Employee.sum(7,9))
Employee.change_company("google")
print(Employee.company)