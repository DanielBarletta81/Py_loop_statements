#Task 1: Random Choice Game
#Create a game where a player has a list of items. They have to guess which item in the list was selected. 
#Use random.choice() to select the item and take the user's guess via input. 
#Provide feedback on whether they guessed correctly or not.

import random

items_list = ['basket', 'vase', 'torch', 'crystal', 'glasses']

selected_item = random.choice(items_list)

user_guess = input("Please enter the item you predict will be selected:(basket/vase/torch/crystal/glasses) ")

if user_guess == selected_item:
    print("You win! You predicted that the " + selected_item + " would be selected!!")
else:
    print("Sorry, you chose the " + user_guess + " , but the correct item was the " + selected_item)

