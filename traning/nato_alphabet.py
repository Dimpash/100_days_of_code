import pandas

# student_dict = {
#     "student": ["Angela", "James", "Lily"],
#     "score": [56, 76, 98]
# }
#
# #Looping through dictionaries:
# for (key, value) in student_dict.items():
#     #Access key and value
#     pass
#
# student_data_frame = pandas.DataFrame(student_dict)
#
# #Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
#     #Access index and row
#     #Access row.student or row.score
#     pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}
data = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_dict = {row.letter: row.code for (index, row) in data.iterrows()}
print(nato_dict)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
def generate_nato_list():
    word = input("Input word: ").upper()
    try:
        word_by_nato = [nato_dict[liter] for liter in word]
    except KeyError:
        print("Sorry, only letters please!")
        generate_nato_list()
    else:
        print(word_by_nato)

generate_nato_list()