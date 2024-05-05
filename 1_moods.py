#Task 1: Your Mood Today

#Write a program that prints off different moods for each day of the week. 
#Create a list of moods such as "Happy", "Sad", "Energetic", and "Calm". 
#Using the range() function, loop through the days of the week and for each day, randomly select a mood from the list and print it.
 #Ensure that your program includes the use of the random module to select the mood.

import random

days_of_week = ['Sunday', 'Monday','Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
moods = ['Happy', 'Sad', 'Lively', 'Grumpy', 'Inquisitive', 'Playful', 'Excited']

for i in range(len(days_of_week)):
    for mood in moods:
        random_mood = random.choice(moods)
   
    print(f"Today is "  + days_of_week[i]  + " ,and your mood is: " + random_mood)
