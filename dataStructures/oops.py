print(
    ''' 
    Object-Oriented Programming is a way of writing programs in the form of classes and objects.
    A class is like a template. For example, an unfilled form is a class — it shows what properties
    and behaviors an object should have. Objects are instances of a class, like a filled form,
    containing the data of a real-world entity.
 
    for ex we made a class of car that should have some variables or attributes like  model , company , speend , type_of_breakes , average ,
    fuel_capacity , and many more 
    and some functions or methods like start , stop , accelarate , slow_down and many more 
    now we make a object using that class
    real world object using this template like maruti800 and defines all the veriables for it and calls the functions for it 

    OOP offers saveral advantages :
    -> Organization: your code become more structures and easier to navigate .
        large projects become much more managable.
    -> reusability: you can use the same object "blueprints" classes multiple times saving you from writing the same code again and again 
    -> Easier Debugging: when something goes wrong . its often easier to pinpoint the problem witha specific self=contained object 
    -> read-world modeling : oop allows you to represent real-world things and there relationship in a natural way 

    four pillers of oops 
    oops is built on four fundamental principle :

    1.Abstraction: means hiding complex data from the user and just siw them the information
    2. Encapsulation: means binding the variables and methods together and put inside a class this protects the data form being accidently changed or misused form outside 
    3. Inheritance: Imagine creating a SportsCar class instead of starting form scratch you can builf it upon an existing \"car\" class
    the Sportscar inherits all the features of car and add its own special feature in it .
    4. Polymorphism: \"poly\" means many and morph means forms . this means object of different classes can respond to the same "message(method call) in their own specific way for example , both a \"dog\" and a cat might have a make_sound() method. the dog will bark ,and the cat will meow - same method name different behaviour 

    classes and objects 

    class is a blueprint or a template eg: form for an exam that contain name , age ,electives , fathername , etc it defiines what a object would be like what data it will hold and what action it can perform . it doesn't create the object itself  , just the instruction off creating it 
    object: specific instance created  from the template (class.). eg. form which contain the data for jhon Doe each object has its own unique set of data , its like a actual house built from an architectural plan 

    
    '''
    )   

class Employee:
    company= "Hp"
    def get_salary(self): # self is the reference of the object of class being created self is like this in cpp or java
        return 30000
    
jhon = Employee() # an object of a class Employee created here 
print(jhon.get_salary()) # Employee jhon's get salaary method is called

ram = Employee() # an object of class Employee created 
print(ram.get_salary()) # employee Ram's get salary method is called 

# whenever i say jhon  = Employee() self is jhon 
# whenever i say ran = Employee() self is ram 

# Constructor 
# A constructor is a special method in a class that runs automatically when you create an object.
# In Python, the constructor method is always named __init__ (double underscores before and after).
# Its job is to initialize (set up) the object with default or custom values.

class Employee:
    company="Asus"

    def __init__(self, name, salary, bond , company):
        # constructor initializes values
        self.name = name
        self.salary = salary
        self.bond = bond
        self.company = company

    def get_info(self):
        return f"{self.name} earns {self.salary} and his bond is for {self.bond} years"

# When you create an object, constructor runs automatically
jhon = Employee("Jhon", 30000, 5 , "tesla")
ram = Employee("Ram", 40000 , 6 , "google")

print(jhon.get_info())  # Jhon earns 30000 and his bond is for 5 years
print(ram.get_info() , end="\n\n")   # Ram earns 40000 and his bond is for 6 years


# instance in class Attribute 

# if we print( jhon.company) what whill print class variable or a instance 
# in that case if a instance is passed object.company always print the instance variable 
# the instance variable is self.company = company this
# object always print a instance attribute 
# if we want to print the class attribute company we can print it using classname.company

# Inheritance :- 
# Inheritance means one class can borrow things from another class.
# The parent class has common features (like name, age).
# The child class automatically gets those features, and can also add its own.

# Think of it like a family:
# A child inherits traits from parents (like eye color, surname).
# But the child can also have unique traits (like hobbies).

class Animal:
    def __init__(self , name):
        self.name = name
    def speak(self):
        print("Generic animal sound")


class dog(Animal): # this is how inheritance is done in python 
    def speak(self):
        super().speak() # super() is used to call the parent’s version of a method inside the child.
        print("woof!") 


bruno = dog("bruno")
print(bruno.name)
bruno.speak()


# Operator overloading 

class Point:

    def __init__(self,x,y):
        self.x = x
        self.y = y

    def sum(self , p):
        # here we are returning a new point object which comes from the sum of cordinates of two object
        return Point((self.x+p.x),(self.y+p.y)) 
    
    def Print_point(self):
        return f"X is {self.x} and  y is {self.y}"
    
    def __add__(self,p):
        # this is same as function but using this we can call this function like p1+p2 this is called operator oveloading
        return Point((self.x+p.x),(self.y+p.y)) 

p1 = Point(3,2)
p2 = Point(6,3)

p = p1.sum(p2)
print(p1.Print_point()) # here we are creating new object with the sum of two objects value 

p3 = p1+p2 # we overloaded teh + operatoe by writing __add__ function
print(p3.Print_point()) 

# there are some other functions that are used to overload the other operators 
# __sub__(-)
# __mul__ (*)
# __truediv__(/)
# __eq__(==)
# __ne__(!=)
# __lt__(<)
# __gt__(>)