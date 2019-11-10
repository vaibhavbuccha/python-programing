# hello world in python

print(" hello world ")

# WAP to perform arithmatic operation based on user input

def calc(a,b,opr):
    if(opr == 'sum'):
        return "sum of ",a," and ",b," is ",a+b;
    elif(opr == "sub"):
        return "subtraction of ",a," and ",b," is ",a-b;
    elif(opr == "multi"):
        return "multiplication of ",a," and ",b," is ",a*b;
    elif(opr == "div"):
        return "division of ",a," and ",b," is ",a/b;
        

    
a= int(input("enter value of a : "))
b = int(input("enter value of b : "))
opr = str(input("enter the opr which you want to perform : "))

print (calc(a,b,opr))
