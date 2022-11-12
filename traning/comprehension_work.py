numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

squared_numbers = [num ** 2 for num in numbers]
print("squared_numbers: ", squared_numbers)

even_numbers = [num for num in numbers if num % 2 == 0]
print("even_numbers: ", even_numbers)

with open("file1.txt") as file1:
    list1 = file1.read().splitlines()

with open("file2.txt") as file2:
    list2 = file2.read().splitlines()

common_numbers = [int(num) for num in list1 if num in list2]
print("common_numbers: ", common_numbers)

####################################################################################

names = ['Alex', 'Beth', 'Dima', 'Olya', 'Egor']

from random import randint

student_scores = {name: randint(1, 100) for name in names}
print("student_scores: ", student_scores)
passed_students = {student: score for (student, score) in student_scores.items() if score >= 60}
print("passed_students: ", passed_students)

#####################################################################################

sentence = "What is the Airspeed Velocity of an Unladen Swallow"

sentence_list = sentence.split(" ")
words_length = {word: len(word)  for word in sentence_list}
print("words_length: ", words_length)

#####################################################################################

weather_c = {'Monday': 12, 'Tuesday': 14, 'Wednesday': 15, 'Thursday': 14, 'Friday': 21, 'Saturday': 22, 'Sunday': 24}
weather_f = {day: (t_c * 9 / 5 + 32) for (day, t_c) in weather_c.items()}
print("weather_f: ", weather_f)
