import requests
import auth_data

def get_question_data():
    proxies = {
            'http': auth_data.http_proxy,
            'https': auth_data.https_proxy,
        }

    parameters = {
        "amount": 10,
        "type": "boolean"
    }

    response = requests.get(url="https://opentdb.com/api.php", proxies=proxies, params=parameters)
    response.raise_for_status()
    data = response.json()
    data_list = data['results']
    # for item in data_list:
    #     item['question'] = item['question'].replace("&#039;", "'").replace("&quot;", '"')
    # print(data)
    return data['results']


question_data = get_question_data()

# question_data = [
#     {
#         "category": "Science: Computers",
#         "type": "boolean",
#         "difficulty": "medium",
#         "question": "The HTML5 standard was published in 2014.",
#         "correct_answer": "True",
#         "incorrect_answers": [
#             "False"
#         ]
#     },
#     {
#         "category": "Science: Computers",
#         "type": "boolean",
#         "difficulty": "medium",
#         "question": "The first computer bug was formed by faulty wires.",
#         "correct_answer": "False",
#         "incorrect_answers": [
#             "True"
#         ]
#     },
#     {
#         "category": "Science: Computers",
#         "type": "boolean",
#         "difficulty": "medium",
#         "question": "FLAC stands for 'Free Lossless Audio Condenser'.",
#         "correct_answer": "False",
#         "incorrect_answers": [
#             "True"
#         ]
#     },
#     {
#         "category": "Science: Computers",
#         "type": "boolean",
#         "difficulty": "medium",
#         "question": "All program codes have to be compiled into an executable file in order to be run. This file can then be executed on any machine.",
#         "correct_answer": "False",
#         "incorrect_answers": [
#             "True"
#         ]
#     },
#     {
#         "category": "Science: Computers",
#         "type": "boolean",
#         "difficulty": "easy",
#         "question": "Linus Torvalds created Linux and Git.",
#         "correct_answer": "True",
#         "incorrect_answers": [
#             "False"
#         ]
#     },
#     {
#         "category": "Science: Computers",
#         "type": "boolean",
#         "difficulty": "easy",
#         "question": "The programming language 'Python' is based off a modified version of 'JavaScript'",
#         "correct_answer": "False",
#         "incorrect_answers": [
#             "True"
#         ]
#     },
#     {
#         "category": "Science: Computers",
#         "type": "boolean",
#         "difficulty": "medium",
#         "question": "AMD created the first consumer 64-bit processor.",
#         "correct_answer": "True",
#         "incorrect_answers": [
#             "False"
#         ]
#     },
#     {
#         "category": "Science: Computers",
#         "type": "boolean",
#         "difficulty": "easy",
#         "question": "'HTML' stands for Hypertext Markup Language.",
#         "correct_answer": "True",
#         "incorrect_answers": [
#             "False"
#         ]
#     },
#     {
#         "category": "Science: Computers",
#         "type": "boolean",
#         "difficulty": "easy",
#         "question": "In most programming languages, the operator ++ is equivalent to the statement '+= 1'.",
#         "correct_answer": "True",
#         "incorrect_answers": [
#             "False"
#         ]
#     },
#     {
#         "category": "Science: Computers",
#         "type": "boolean",
#         "difficulty": "hard",
#         "question": "The IBM PC used an Intel 8008 microprocessor clocked at 4.77 MHz and 8 kilobytes of memory.",
#         "correct_answer": "False",
#         "incorrect_answers": [
#             "True"
#         ]
#     }
# ]
