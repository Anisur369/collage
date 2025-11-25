a=int(input("Enter the value of a: "))
b=int(input("Enter the value of b: "))
c=int(input("Enter the value of c: "))

if(a>b) and (a>c):
    print("Largest number is: ",a)
elif(b>a) and (b>c):
    print("Largest number is: ",b)
else:
    print("Largest number is: ",c)


# output:
# Enter the value of a: 200
# Enter the value of b: 500
# Enter the value of c: 100
# Largest number is:  500