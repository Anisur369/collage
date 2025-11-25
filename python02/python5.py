x=int(input("Enter the value of x: "))
y=int(input("Enter the value of y: "))
z=int(input("Enter the value of z: "))

if(x<y) and (x<z):
    print("The smallest number is:",x)
elif(y<x) and (y<z):
    print("The smallest number is:",y)
else:
    print("The smallest number is:",z)


# output:
# Enter the value of x: 120
# Enter the value of y: 50
# Enter the value of z: 80
# The smallest number is: 50