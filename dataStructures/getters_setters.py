class Employee:
    def __init__(self , name , salary):
        self.name = name
        self.salary = salary

    @property # here we put a property decorator which makes this function as a property  eg  object.first_name 
    def first_name(self):
        f_name = self.name.split(" ")[0]
        return f_name
    
    @first_name.setter # here we put a @first_name.setter decorator  using this i can call this function like assigning a value eg  object.first_name = name
    def first_name(self , name) : 
        fullname = self.name.split(" ")
        lastname = " ".join(fullname[1:])
        name = f"{name} {lastname}"
        self.name = name.strip()
         


garvit = Employee("garvit singh panwar" , 120000)

# using decorator instead of calling function like this 
# garvit.Set_first_name("lucky")
# print(garvit.name)

# we can call them like this 
print(garvit.first_name)
garvit.first_name = "lucky"
print(garvit.name)

# bassically getters and setters are used to write cleaner syntax in python 
# we use @property decorator to get a property 
# we use @ function_name.setter to set a property 
# we name the function just like in the property but with different decorator so thats how it look like a property 

        

    