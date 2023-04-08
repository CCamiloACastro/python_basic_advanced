# syntax: module_name.function_name.
import mymodule
import platform

mymodule.greeting("Camilo")

a = mymodule.person1["age"]
print(a)

# The dir() function can be used on all modules, also the ones you create yourself.
diirection = dir(mymodule)
print(diirection)

x = platform.system()
print(x)


