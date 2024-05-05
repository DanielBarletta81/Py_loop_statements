# Task 1: Your Mood Tracker
#Simulate a mood tracker that records your mood at three different times of the day (morning, afternoon, evening)
#for each day of the week. Use nested loops to implement this: the outer loop should 
#iterate over the days, and the inner loop should iterate over the times of the day. 
#For each time, randomly select a mood from a predefined list and print it.

import random

days_of_week = ['Sunday', 'Monday','Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']

time_of_day = ['Morning', 'Afternoon', 'Evening']

moods = ['Happy', 'Sad', 'Lively', 'Grumpy', 'Inquisitive', 'Playful', 'Excited']



for i in range(len(days_of_week)):
    for time in range(len(time_of_day)):
        current_mood = random.choice(moods)
        print("On " + days_of_week[i] + " in the " + time_of_day[time] + " you were feeling " + current_mood)

