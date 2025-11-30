def grade():
  Marks=float(input("Enter the marks: "))
  if(Marks>=80):
    print("Grade: A+")
  elif(Marks>=70):
    print("Grade: A")
  elif(Marks>=60):
    print("Grade: A-")
  elif(Marks>=50):
    print("Grade: B")
  elif(Marks>=40):
    print("Grade: C")
  elif(Marks>=33):
    print("Grade: D")
  else:
    print("Grade: F")

grade()


# output:
# Enter the marks: 75
# Grade: A