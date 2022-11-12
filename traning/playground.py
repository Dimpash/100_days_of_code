from tkinter import *

# def add(*args):
#     result = 0
#     for num in args:
#         result += num
#     return result
#
# print(add(1,2,6,4,5))


def btn_click():
    label_for_result["text"] = f"{float(my_input.get()) * 1.609}"


window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)

# new_button = Button(text="New Button", command=btn_click)
# new_button.grid(column=2, row=0)


# Entry
my_input = Entry(width=10)
my_input.grid(column=1, row=0)

label_for_input = Label(text="Miles", font=("Arial", 16, "bold"))
# label_for_input["text"] = "New text 1"
# label_for_input.config(text="New text 2")
label_for_input.grid(column=2, row=0)

label_for_result_1 = Label(text="Is equal to", font=("Arial", 16, "bold"))
label_for_result_1.grid(column=0, row=1)

label_for_result = Label(text="", font=("Arial", 16, "bold"))
label_for_result.grid(column=1, row=1)

label_for_result_1 = Label(text="km", font=("Arial", 16, "bold"))
label_for_result_1.grid(column=2, row=1)

button = Button(text="Calculate", command=btn_click)
button.grid(column=1, row=2)

mainloop()