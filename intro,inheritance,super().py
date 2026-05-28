#oject =A "bundle" of related attribute (variable) and methods (functions)
#     ex. phone, cup, book
#     you need a "class" to create many onjects

#class = (blueprint) used to design the structure and layout of an object 

# class car:
#     def __init__(self, model, year, color, for_sale):
#         self.model=model
#         self.year=year
#         self.color=color
#         self.for_sale=for_sale

#     def drive(self):
#         print(f"You drive the {self.model}")

#     def stop(self):
#         print(f"you stop the {self.model}")

# car1= car("mustang", 2024, "red", False)
# car2 = car("corvette", 2025, "blue", True)
# car3 = car("charger", 2026, "yellow", True)

# print(car1.model)
# print(car1.color)
# print(car3.year)

# car1.stop()



#class variable = shared among all instances of a class
#                 defined outside the constructor
#                 allow you to share date among all onject created from that class 

# class student:

#     class_year = 2024
#     num_students = 0
#     def __init__(self, name, age):
#         self.name= name
#         self.age= age
#         student.num_students +=1

# student1 = student("Spongebob", 30)
# student2 = student("patrick", 35)
# student3 = student("pedri", 24)
# student4 = student("messi", 38)
# # print(student1.name)
# # print(student2.age)
# # print(student1.class_year)
# # print(student.num_students)

# print(f"My graduation class of {student.class_year} has {student.num_students} students ")
# print(student1.name)
# print(student2.name)
# print(student3.name)
# print(student4.name)

##################################################################

#Inheritance = Allows a class to inherit attributes and methods form another class
#              helps with code reusability and extensibility 
#              class child(parent)


# class Animal:
#     def __init__(self,name):
#         self.name = name
#         self.is_alive= True

#     def eat(self):
#         print(f"{self.name} is eating")

#     def sleep(self):
#         print(f"{self.name} is sleeping")

# class Dog(Animal):
#     def speak(self):
#         print("Woof!")


# class Cat(Animal):
#     def speak(self):
#         print("Meow!")


# class Mouse(Animal):
#     def speak(self):
#         print("Squee")

# dog = Dog("Scooby")
# cat = Cat("Gerfield")
# mouse =Mouse("Mickey")

# print(dog.name)
# print(dog.is_alive)
# dog.eat()
# dog.sleep()
# cat.speak()

#######################################################################

#multiple inheritance = inherit from more than one parent class 
#                       C(A,B)

#multilevel inheritance = inherit from a parent which inherit from another parent 
#                         C(B) <- B(A) <- A



# class Animal:
#     def __init__(self,name):
#         self.name = name

#     def eat(self):
#         print(f"{self.name} is eating")

#     def sleep(self):
#         print(f"{self.name} is sleeping")

        

# class Prey(Animal):
#     def flee(self):
#         print(f"{self.name} is fleeing")

# class Predator(Animal):
#     def hunt(self):
#         print(f"{self.name} is hunting")

# class Rabbit(Prey):
#     pass

# class Hawk(Predator):
#     pass

# class Fish(Prey, Predator):
#     pass

# rabbit = Rabbit("bugs")
# hawk = Hawk("tony")
# fish = Fish("nemo")

# hawk.hunt()

# rabbit.eat()
# fish.sleep()

######################################################################################
#super() = Function used in a child class to call method from a parent class(superclass).
#          Allow you to extedn the functionality of the inherited methods.




# class shape:
#     def __init__(self, color, is_filled):
#         self.color = color
#         self.is_filled = is_filled

# class Circle(shape):
#     def __init__(self, color, is_filled, radius):
#         super().__init__(color, is_filled)
#         self.radius= radius

# class Square(shape):
#     def __init__(self, color, is_filled, width):
#         super().__init__(color, is_filled)
#         self.width= width
    

# class Triangle(shape):
#     def __init__(self, color, is_filled, width, height):
#         super().__init__(color, is_filled)
#         self.width= width
#         self.height= height

#     circle = Circle("red",True,5)
#     Square= Square("blue",False, 10)

#     print(circle.color)
#     print(circle.is_filled)
#     print(Square.width)


