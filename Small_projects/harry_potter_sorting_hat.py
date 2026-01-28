gryffindor = 0
ravenclaw = 0
hufflepuff = 0
slytherin = 0

#--------------------------------Q1--------------------------------#
print("Q1) Do you like Dawn or Dusk?")
print("    1) Dawn")
print("    2) Dusk")

q1 = int(input("Enter your answer(1-2): "))

if q1 == 1:
  gryffindor = gryffindor + 1
  ravenclaw = ravenclaw + 1
elif q1 == 2:
  hufflepuff = hufflepuff + 1
  slytherin = slytherin + 1
else:
  print("Wrong input.")

#--------------------------------Q2--------------------------------#
print("Q2) When I’m dead, I want people to remember me as:")
print("    1) The Good")
print("    2) The Great")
print("    3) The Wise")
print("    4) The Bold")

q2 = int(input("Enter your answer(1-4): "))

if q2 == 1:
  hufflepuff = hufflepuff + 2
elif q2 == 2:
  slytherin = slytherin + 2
elif q2 == 3:
  ravenclaw = ravenclaw + 2
elif q2 == 4:
  gryffindor = gryffindor + 2
else:
  print("Wrong input.")

#--------------------------------Q3--------------------------------#
print("Q3) Which kind of instrument most pleases your ear?")
print("    1) The violin")
print("    2) The trumpet")
print("    3) The piano")
print("    4) The drum")

q3 = int(input("Enter your answer(1-4): "))

if q3 == 1:
  slytherin = slytherin + 4
elif q3 == 2:
  hufflepuff = hufflepuff + 4
elif q3 == 3:
  ravenclaw = ravenclaw + 4
elif q3 == 4:
  gryffindor = gryffindor + 4
else:
  print("Wrong input.")

#------------------------------ANSWER------------------------------#
if gryffindor > ravenclaw and gryffindor > hufflepuff and gryffindor > slytherin:
  print("You are a Gryffindor!")
elif ravenclaw > gryffindor and ravenclaw > hufflepuff and ravenclaw > slytherin:
  print("You are a Ravenclaw!")
elif hufflepuff > gryffindor and hufflepuff > ravenclaw and hufflepuff > slytherin:
  print("You are a Hufflepuff!")
elif slytherin > gryffindor and slytherin > ravenclaw and slytherin > hufflepuff:
  print("You are a Slytherin!")
else:
  print("Something went wrong!")

#print(gryffindor)
#print(ravenclaw)
#print(hufflepuff)
#print(slytherin)
