a=20
b=30
if a>b:
    print("a is greater than b")
elif b>a:
    print("b is greater than a")    
else:
    print("a is equal to b")


a = input("Enter a number:")
num = int(a)
if num>0:
    print("num is positive")
elif num<0:
    print("num is negative")
else:
    print("num is zero")


#if statements cannot be empty, but if you for some reason have an if statement with no content, put in the pass statement to avoid getting an error.
a=10
b=20
if a>b:
    pass  


b=input("Enter a number:")
c=int(b)
if c>10:
    print("number is greater than 10")
elif c<10:
    print("number is less than 10")
else:
    print("Number is exactly 10")







