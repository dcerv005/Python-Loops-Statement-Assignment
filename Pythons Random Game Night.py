import random
#Question 4 Task 1
item_list= ['ball', 'pencil', 'eraser', 'dice', 'board']


for _ in range(5):
    picked_item = random.choice(item_list)
    user_input = input("Guess what item you got?")
    if picked_item == user_input.lower():
        print("You won!")
        break
    else:
        print("Try again!")
print("Thank you for playing!")