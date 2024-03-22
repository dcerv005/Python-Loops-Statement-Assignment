#Question 6 Task 1
genres = ['Jazz', 'Rock', 'Hip-hop', 'Classical']
for genre in genres:
    print(genre)

subset_list= genres[1:4]
print(subset_list)

#Question 6 Task 2
new_list = [genre + ' Music' for genre in genres]
print(new_list)

#Question 6 Task 3
for x in range(10,0,-1):
    print(x)
print("The beat drops now!")