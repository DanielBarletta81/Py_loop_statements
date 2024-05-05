# Task 2: The One-Liner Band with List Comprehensions
#Use a list comprehension to create a new list that
#contains each genre with the word "Music" appended to it. Print this new list.

genres = ['Jazz', 'Rock', 'Hip-hop', 'Classical']

new_genre_list = [x + " Music" for x in genres]


print(new_genre_list)