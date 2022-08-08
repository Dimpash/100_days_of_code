from tkinter import *
from tkinter import messagebox
import pandas

BACKGROUND_COLOR = "#B1DDC6"




# ---------------------------- NEW FLASH CARD MECHANISM ------------------------------- #
def new_flash_card():
    global card, flip_timer
    window.after_cancel(flip_timer)
    try:
        card = data.sample()
    except:
        btn_right.config(state="disabled")
        btn_wrong.config(state="disabled")
        messagebox.showinfo(title="Congratulations!", message="You learned all these words!")
    else:
        # new_word = data.sample().to_dict(orient="records")
        canvas.itemconfig(img, image=card_front_img)
        canvas.itemconfig(title_text, text=language, fill="black")
        # canvas.itemconfig(word_text, text=new_word(language))
        canvas.itemconfig(word_text, text=card[language].values[0], fill="black")
        flip_timer = window.after(3000, func=flip_card)
        # canvas.itemconfig(title_text, text=native_language)
        # canvas.itemconfig(word_text, text=new_word[native_language].values[0])

def flip_card():
    canvas.itemconfig(img, image=card_back_img)
    canvas.itemconfig(title_text, text=native_language, fill="white")
    canvas.itemconfig(word_text, text=card[native_language].values[0], fill="white")

def ok_click():
    data.drop(labels=card.index.values, inplace=True)
    data.to_csv(path_or_buf="data/words_to_learn.csv", index=False)
    new_flash_card()



window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526)
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
img = canvas.create_image(400, 263, image=card_front_img)
title_text = canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"), fill="black")
word_text = canvas.create_text(400, 263, text="word", font=("Ariel", 60, "bold"), fill="black")
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

wrong_img = PhotoImage(file="images/wrong.png")
btn_wrong = Button(image=wrong_img, highlightthickness=0, command=new_flash_card)
btn_wrong.grid(column=0, row=1)

right_img = PhotoImage(file="images/right.png")
btn_right = Button(image=right_img, highlightthickness=0, command=ok_click)
btn_right.grid(column=1, row=1)

try:
    data = pandas.read_csv("data/words_to_learn.csv")
except:
    data = pandas.read_csv("data/en_ru_0.csv")
language = data.columns[0]
native_language = data.columns[1]

flip_timer = window.after(3000, func=flip_card)
# print(data.Russian.sample())

new_flash_card()





window.mainloop()
