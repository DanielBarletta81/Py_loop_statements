# Task 2: The Remix Artist with while
#Convert the for loop from Task 1 into a while loop. 
#Ensure it performs the same function but also includes a condition to stop the loop 
#if a certain genre is played for instance Hip-hop.
import random
# From Task 1:

""" genres = ['Jazz', 'Rock', 'Hip-hop', 'Classical']
messages = [ 'smooth and relaxing ', 'hard-hitting and energizing ', 'urban-flavored ', 'elegant and refined ']

for i in range(len(genres)):
    track = i + 1
    genre = genres[i]
    message = messages[i]

    print(f"Track " + str(track) + " is from the " + message + "genre " + genre) """

# Converted for Task 2:

genres = ['Jazz', 'Rock', 'Hip-hop', 'Classical']

selected = []

killer_genre = genres[3]
# Classical is the genre that kills the loop
track = 0

while killer_genre not in selected:

  genre_select = random.choice(genres)
  selected.append(genre_select)
  track += 1
  if genre_select == 'Jazz':
    print(f"Track # " + str(track) + " comes from the smooth, relaxing, and timeless genre " + genre_select)
  elif genre_select == 'Hip-hop':
    print(f"Track # " + str(track) + " comes from the genre " + genre_select + " with its hard beats and lyrics!")
  elif genre_select == 'Rock':
   print(f"Track # " + str(track) + " comes from the hard-hitting, hair-banded genre " + genre_select)
  else:
     print(f"Track # " + str(track) + " comes from the genre " + genre_select + " , full of tradition and elegant melodies.")

else:
  print("The genre " + killer_genre + " was chosen for track # " + str(track) + ", which will be our farewell song.")



  
 
 





