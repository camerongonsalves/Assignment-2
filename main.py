round = "yes"
round = "Yes"
hello = input("Welcome to Circle Bot, please press Enter to start") 
print()
while round == "yes" or round == "Yes":
  print ("Please type Radius or Diameter depending on which you wish to input")
  pi = 3.14159265359
  print("")
  choice = input()
  if (choice) == "Radius" or (choice) == "radius":
    print("")
    radius = int(input("Please enter the radius of the circle: "))
    area = pi*radius**2
    circumference = 2*pi*radius
  if (choice) == "Diameter" or (choice) == "diameter":
    print("")
    diameter = int(input("Please enter the diameter of the circle: "))
    radius = diameter/2
    area = pi*radius**2
  circumference = 2*pi*radius
  print ("")
  print ("Area:")
  print ("")
  print (area)
  print ("")
  print ("")
  print ("Circumference:")
  print ("")
  print (circumference)
  print ("")
  print ("")
  print ("Would you like to enter a new Radius or Diameter?")
  print ("")
  round = input()
  if (round) == "yes" or (round) == "Yes":
    print ("")
    print ("")
if (round) == "no" or (round) == "No":
  print ("")
  print ("Have a nice day!")