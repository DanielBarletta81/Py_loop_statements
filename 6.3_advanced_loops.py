# Task 3: Numerical Beats with range
#Write a loop using range() to print out a countdown from 10 to 1,
#followed by the message "The beat drops now!".

counter = 10

for i in range(10, -1, -1):
    if counter > 0:
        counter -= 1
        print(i)
    else:
        print('The beat drops NOW!')