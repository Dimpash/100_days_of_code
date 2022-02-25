with open('./Input/Letters/starting_letter.txt') as f:
    letter_blank = f.read()

with open('./Input/Names/invited_names.txt') as f:
    names = f.readlines()

for name in names:
    with open(f'./Output/letter_{name.strip()}.txt', mode='w') as result_f:
        result_f.write(letter_blank.replace('[name]', name.strip()))
