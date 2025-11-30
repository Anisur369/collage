def quadric_equation():
  a=int(input("Enter the value of a: "))
  b=int(input("Enter the value of b: "))
  c=int(input("Enter the value of c: "))
  D=(b*b-4*a*c)
  if(D>0):
    r1=(-b+D**0.5)/(2*a)
    r2=(-b-D**0.5)/(2*a)
    print("The values of roots are: r1=",r1,"and r2=",r2)
  elif(D==0):
    r1=-b/(2*a)
    print("The value of root is: r1=",r1)
  else:
    print("The roots are imaginary")

quadric_equation()


# Output:
# Enter the value of a: 5
# Enter the value of b: 10
# Enter the value of c: 3
# The values of roots are: r1= -0.3675444679663241 and r2= -1.632455532033676