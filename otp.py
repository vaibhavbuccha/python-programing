#----------------------------------
# WAP to generate otp of 6 digit
#----------------------------------


from random import randint
print (randint(0,9),randint(0,9),randint(0,9),randint(0,9),randint(0,9),randint(0,9))

# for remove spaces between digits we use sep=''
print (randint(0,9),randint(0,9),randint(0,9),randint(0,9),randint(0,9),randint(0,9),sep='')


#---------------------------------------------------
# WAP to generate no of otp's based on user input 
#---------------------------------------------------

def optGenerator(n):

    while n>0:
        # NOTE : - in while loop we have to use print function for instead of return because the return in a terminater statement that terminate the execution.
        print ("OTP No.",n," : " ,randint(0,9),randint(0,9),randint(0,9),randint(0,9),randint(0,9),randint(0,9),sep='')
        n=n-1;

n = int(input("enter the no of otp's you want : "))
optGenerator(n)

#-----------------------------------------------------
# WAP to generate digits of otp's based on user input 
#-----------------------------------------------------

def otpDigitGenerater(i):
    otp = ''
    while i>0:
        otp = otp + str(randint(0,9))
        i = i-1
    print (otp)
    
i = int(input("enter the digits of otp tou want : "))
otpDigitGenerater(i)

#--------------------------------------------------------------------------------
# WAP that follows following instructions .
# 1 .  generate no of otp's based on user input
# 2 . generate digits of otp's based on user input 
#--------------------------------------------------------------------------------


# n => n specifies the no of otps that user want.
# m => m specifies the digits user want
def otpCustomGenerater(n,m):
    while n > 0:
        i = m
        otp = ''
        while i > 0:
            otp = otp + str(randint(0,9))
            i = i-1
        print ("OTP No. ",n," : ",otp)
        n = n-1

n = int(input("Enter the No of otps you want : "))
m = int(input("Enter the No of digits of otp you want : "))

otpCustomGenerater(n,m)

