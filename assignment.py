print("Input the diameter!")
Diameter = input()
Diameterint = int(Diameter)
if Diameterint <= 0:
  print("Error Diameter is not a positive number!")
elif Diameterint > 0:
    Pi = 3.14
    Radius = Diameterint / 2
    Circumference = 2*Pi*Radius
    Area = Pi*Radius*Radius
    print("Results")
    print(Circumference)
    print(Area)