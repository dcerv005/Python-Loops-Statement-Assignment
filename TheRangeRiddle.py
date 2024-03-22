import random
#Question 1 Task 1
moods = ["Happy", "Sad", "Energetic", "Calm"]
days_of_the_week= ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
for day in range(7):
    day_of_the_week = days_of_the_week[day]
    mood = random.choice(moods)
    print(f"Today is {day_of_the_week} and my mood is {mood}")


