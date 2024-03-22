#Question 5 Task 1
import random
genres = ['Jazz', 'Rock', 'Hip-hop', 'Classical']
counter = 0
for genre in genres:
    counter +=1
    print(f"You are now listening to track {counter} in genre: {genre}")

#Question 5 task 2
    
genres = ['Jazz', 'Rock', 'Hip-hop', 'Classical']
counter = 0
while counter < len(genres):
    genre = genres[counter]
    counter +=1
    print(f"You are now listening to track {counter} in genre: {genre}")
    if genre == 'Hip-hop':
        break


#Question 5 task 3
genres = ['Jazz', 'Rock', 'Hip-hop', 'Classical']

for index in range(len(genres)):
    if genres[index] == 'Classical':
        continue
    print(f"The light show is ready for track number {index+1}: {genres[index]}")
    
    