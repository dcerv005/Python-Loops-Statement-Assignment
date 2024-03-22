import random
#Question 2 Task 1
time_of_the_day = ["morning", "afternoon", "evening"]
days_of_the_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
moods = ["Happy", "Sad", "Energetic", "Calm"]

for day in days_of_the_week:
    for time in time_of_the_day:
        mood = random.choice(moods)
        print(f"It is {day} {time} and I am feeling {mood.lower()}")