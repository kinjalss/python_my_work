a=input("Enter num 1:")
b=input("Enter num 2:")
c=input("Enter num 3:")
num1=int(a)
num2=int(b)
num3=int(c)
if num1>num2:
    if num1>num3:
        print(f"{num1} is largest")
    else:
        print(f"{num3} is largest")
elif num2>num3:
    print(f"{num2} is largest")
else:
    print(f"{num3} is largest")

    