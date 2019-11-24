# data types in python
#-----------------------

# 1). in python type concept isn't available 
# 2). in python we don't required to declare type of variable explicitly ( due to this python is called dynamically typed language )

#  available data types in python
#----------------------------------

# in python 14 types of datatypes are available 
#  1. int 
#  2. float
#  3. complex
#  4. bool
#  5. str
#  6. list
#  7. tuple
#  8. set
#  9. forzenset
#  10. dict
#  11. bytes
#  12. bytearray
#  13. range
#  14. none

# every thing in python is concidered as object

# a = 10 ( a is the object of 10 )

# type() is use for getting the type of a varibale 

a = 10
b = 'vaibhav'
c = True
d = 10.0+7j
e = 5.0e2

print(":: Type of variables ::")
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))

# for gettig memory address of a variable we use id()
print(":: Address of variables ::")
print(id(a))
print(id(b))
print(id(c))
print(id(d))
print(id(e))

# in python 2 long data type is available but in python 3 long values are represented by int it self
# we can represent intigral values via 4 ways
# 1. decimal (base-3  range {0-9} ) -> default
# 2. binary (base-2  range {0-1})  prefix = 0b
# 3. octal (base-8 range {0-7})  prefix = 0O
# 4. hexadecimal ( base-16 range {0-15}) prefix = 0X

print (":: Integral datatype ::")
print (":: Representations ::")

a = 0b111
print ("binary to decimal 0b111 = ", a)

a = 0O123
print ("octal to decimal 0O123 = ", a)

a = 0xface
print ("hexadecimal to decimal 0xface = ", a)

# Base conversion
print(':: base conversion in python ::')

a = 10

print("decimal to binary of 10 = ",bin(a))
print("decimal to octal of 10 = ",oct(a))
print("decimal to hexadeciaml of 10 = ",hex(a))



