import random
import pandas as pd

names = ['Alex','Beth','Caroline','Dave','Eleanor','Freddie']

student_scores = {student:random.randint(1,100) for student in names}
#print(student_scores)

passed_students = {key:student_scores[key] for key in student_scores.keys() if student_scores[key]>60}
#print(passed_students)

passed_students_1 = {student:score for (student,score) in student_scores.items() if score>=60}
#print(passed_students_1)


#Exercise 1
sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# 🚨 Don't change code above 👆
# Write your code below 👇

words_list = sentence.split(' ')
result = {word:len(word) for word in words_list}

#print(result)


#Exercise 2
weather_c = {"Monday": 12, "Tuesday": 14, "Wednesday": 15, "Thursday": 14, "Friday": 21, "Saturday": 22, "Sunday": 24}
# 🚨 Don't change code above 👆
# Write your code 👇 below:

weather_f = {day:(degrees*9/5) +32 for (day,degrees) in weather_c.items()}

#print(weather_f)

student_dict = {
    "student":["Angela","James","Lily"],
    "score": [56,76,98]
}

#Looping through a dictionary
for (key,value) in student_dict.items():
    print(f"{key}:{value}")

print("\n")

student_df = pd.DataFrame(student_dict)
print(student_df)

#Loop through a DF
for (index, row) in student_df.iterrows():
    print(row)