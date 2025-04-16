# a = 1
# b = 0.1
# c = "c"
# # == checks equality
#
# print(a)
# print(type(a))
# print(b)
# print(type(b))
# print(c)
# print(type(c))
#
# #variables have specific types and this is enforced strictly. php is weakly typed
# #a = "error" + 1
#
# #a variable's type is defined as the program runs, and can change. c# is statically typed
# a = "a was an integer, now is a string"
#
# print(id(a))
# a = 1
# print(id(a))
# #a variable's id is the memory address of the variable. when it changes it points to a different value
#
# x = 10
# y = x
# print(id(x))
# print(id(y))
# #they are pointing to the same value
# x = 1
# print(id(x))
# print(id(y))

name = input("What is your name? ")
age = int(input("What is your age? "))
month = input("What month were you born? ")
year = input("What year were you born? ")
print(f"Hi {name}, {age}")
print(f"You were born in {month} of the year {year}.")