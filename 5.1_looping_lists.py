#Task 1: The for Loop DJ Set
#Using the provided genres list, write a for loop that prints out each genre with a custom message. 
#Extend this task by adding a counter that displays the number of the track before the genre.

# Our playlist of genres
genres = ['Jazz', 'Rock', 'Hip-hop', 'Classical']
messages = [ 'smooth and relaxing ', 'hard-hitting and energizing ', 'urban-flavored ', 'elegant and refined ']

for i in range(len(genres)):
    track = i + 1
    genre = genres[i]
    message = messages[i]

    print(f"Track " + str(track) + " is from the " + message + "genre " + genre)
