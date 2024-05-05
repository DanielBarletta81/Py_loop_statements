#Task 1: Loop Condition Exploration
# Write a while loop with a condition that will never be false (an infinite loop).
 # Inside the loop, print a statement. 
#Then, use a break statement to exit the loop after 5 iterations.

party_balloons = 200
iterations = 5

while party_balloons > 1:
   party_balloons += 1
   iterations -= 1
   print("The party continues!")
   if iterations == 0:
      break
