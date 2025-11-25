import math
a=float(input("Enter the value of a: "))
b=float(input("Enter the value of b: "))
c=float(input("Enter the value of c: "))

D=b*b-4*a*c
if(D>0):
  r1=(-b+math.sqrt(D))/(2*a)
  r2=(-b-math.sqrt(D))/(2*a)
  print("The values of roots are: r1=",r1,"and r2=",r2)
else:
  print("The roots are imaginary")


# output:
# Enter the value of a: 5
# Enter the value of b: 10
# Enter the value of c: 3
# The values of roots are: r1= -0.3675444679663241 and r2= -1.632455532033676