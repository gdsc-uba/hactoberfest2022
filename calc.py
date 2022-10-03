import math
print("WELCOME! TO THE ADVANCED CALCULATOR!!!\t + - / *")
print("I am CALCI, an immitation of modern day online calculators(in comparison to the functioning)")
print("The functions I can perform are----->")
print("""               [1]Round off a given number to the next number.                                           
               [2]Round off a given number to the previous number.
               [3]To Find th Factorial of a given number.
               [4]To Find the modulus of a given +ve  or -ve number.
               [5]To Find the remainer of 1 number when divided by the other number.
               [6]To Find the Greatest Common Divisor of 2 given numbers.
               [7]To Find 1 number to the power another number.
               [8]To Find the squre root of a given number.
               [9]To Find the sine of a given number in radians.
               [10]To Find the cosine of a given number in radians.
               [11]To Find the tangent of a given number in radians.""")
a=int(input("Enter choice of mathematical function(from 1 to 11):"))
while True:
    if(a==1):
        n=float(input("Enter number which is to be rounded off to its next number:"))
        print("After rounding off, the number is:",math.ceil(n))
    if(a==2):
        m=float(input("Enter number which is to be rounded off to its previous number:"))
        print("After rounding off, the number is:",math.floor(m))
    if(a==3):
        p=int(input("Enter number whose factorial is to be found (number should be +ve):"))
        print("Therefore, the factorial of",p,'is',math.factorial(p))
    if(a==4):
        q=int(input("Enter number whose modulus is to be found is to be rounded off to its next number:"))
        print("Therefore, modulus of:",q,'is',math.fabs(q))
    if(a==5):
        Q=float(input("Enter first number (which will be in the numerator):"))
        s=float(input("Enter second number (which will be in the denominator):"))
        print("So, the remainder on dividing",Q,'by',s,'is',math.fmod(Q,s))
    if(a==6):
        S=float(input("Enter first number:"))
        t=float(input("Enter second number:"))
        print("The greatest common divisor of",S,"and",t,"is:",math.fmod(S,t))
    if(a==7):
       S=float(input("Enter first number:"))
       t=float(input("Enter second number:"))
       print(S,"to the power",t,"is:",math.pow(S,t))
    if(a==8):
        N=int(input("Enter number whose square root is to be found:"))
        print("Therefore, the square root of the number is:",math.sqrt(N))
    if(a==9):
         x=float(input("Enter number whose sine is to be found:"))
         print("So, Sine of the number is:",math.sin(x))
    if(a==10):
        x=float(input("Enter number whose cosine is to be found:"))
        print("So, Cosine of the number is:",math.cos(x))
    if(a==11):
       x=float(input("Enter number whose tangent is to be found:"))
       print("So, Tangent of the number is:",math.tan(x))
    
    ch=input("Do you want to continue?[Yes or No]")
    if(ch=='No' or ch=='no' or ch=='NO'):
        print("IT WAS FUN CALCULATING FOR YOU!!!!\nBYE!!!  + - / *")
        break
