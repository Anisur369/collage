def quadric():
  import math
  a=int(input("Enter the value of a: "))
  b=int(input("Enter the value of b: "))
  c=int(input("Enter the value of c: "))
  if(a+b>c) and (b+c>a) and (c+a>b):
    s=(a+b+c)/2
    area=math.sqrt(s*(s-a)*(s-b)*(s-c))
    print("The area of the triangle is:",area)
  else:
    print("The triangle is not valid")

quadric()


# Output:
# Enter the value of a: 20
# Enter the value of b: 30
# Enter the value of c: 25
# The area of the triangle is: 248.03918541230536