"""Type Hints son una nueva sintáxis, desde Python 3.6+, que permite declarar el tipo de una variable.
Usando las declaraciones de tipos para tus variables, los editores y otras herramientas pueden proveerte un soporte
mejor.
"""
my_string_variable = "My String variable"
print(my_string_variable)
print(type(my_string_variable))

my_string_variable = 5
print(my_string_variable)
print(type(my_string_variable))

my_typed_variable: str = "My typed String variable"
print(my_typed_variable)
print(type(my_typed_variable))

my_typed_variable = 5
print(my_typed_variable)
print(type(my_typed_variable))
