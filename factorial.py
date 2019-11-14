'''
    WAP to find the factorial of given number
'''


def factorial(n):
    i=1
    fact = 1
    while i < n+1:
        fact = fact*i
        i= i+1
    print(fact)

n = int(input('enter no to find factorial : '))
factorial(n)


