# :: complex datatype ::
# complex datatypes are thoes datatypes which represents to parts one is real and another one is binary
# representation in python 10+2j  here 10 is real part and 2j is imaginary part.

a = 10+2j

print(type(a))

# getting the imaginary and real part of a complex number

print("real part of a is = ",a.real)
print("imaginary part of a is = ",a.imag)

# we can represent real part of complex number in any form but the imaginary part must be in decimal form 

a = 0b111+2j
print('type of a = 0b111+2j  is = ',type(a) ) 

a= 0o456+2j
print('type of a = 0o456+2j  is = ',type(a) ) 

a= 0xface+2j
print('type of a = 0bface+2j  is = ',type(a) ) 

# we can also perform the arithmatic operation between 2 complex no.
a = 52+2j
b = 82+3j

print(a+b)
print(a-b)
print(a/b)
print(a*b)
