#Task 2: Conditional Exit
#Modify the infinite loop from Task 1 to include a condition that will 
#eventually be true and remove the break statement.
#The loop should terminate naturally once the condition is met.

# From Task 1

party_balloons = 200
iterations = 5

while party_balloons > 1:
   party_balloons += 1
   iterations -= 1
   print("The party continues!")
   if iterations == 0:
      break
   
# Modify for Task 2

party_balloons = 0


while party_balloons < 10:
   party_balloons += 1
  
   print("We have all the balloons we need for the party!")
  

