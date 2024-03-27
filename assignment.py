import time
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
  time.sleep(1)
  print("Beep...")
  time.sleep(1)
  print("Boop..")
  time.sleep(1)
  print("Bap.")
  time.sleep(1)
  print("Ding!")
  time.sleep(0.75)
  print("Results")
  print("Circumference =", Circumference)
  print("Area =", Area)