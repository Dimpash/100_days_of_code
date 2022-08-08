from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #


def reset_timer():
    window.after_cancel(timer)
    lbl_header.config(text="Timer", fg=GREEN)
    canvas.itemconfig(timer_text, text="00:00")
    lbl_checkpoint.config(text="")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    global reps

    reps += 1
    if reps % 8 == 0:
        lbl_header.config(text="Break", fg=RED)
        count_down(LONG_BREAK_MIN * 60)
    elif reps % 2 == 0:
        lbl_header.config(text="Break", fg=PINK)
        count_down(SHORT_BREAK_MIN * 60)
    else:
        lbl_header.config(text="Work", fg=GREEN)
        count_down(WORK_MIN * 60)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        if reps % 2 == 0:
            lbl_checkpoint.config(text=lbl_checkpoint["text"] + "✔")
        start_timer()



# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

lbl_header = Label(text="Timer", font=(FONT_NAME, 35, "bold"), bg=YELLOW, fg=GREEN)
lbl_header.grid(column=1, row=0)

canvas = Canvas(width=202, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(102, 112, image=tomato_img)
timer_text = canvas.create_text(102, 130, text="00:00", fill="white", font=(FONT_NAME, 25, "bold"))
canvas.grid(column=1, row=1)


btn_start = Button(text="Start", font=(FONT_NAME, 16, "bold"))
btn_start.grid(column=0, row=2)
btn_start.config(command=start_timer)

btn_reset = Button(text="Reset", font=(FONT_NAME, 16, "bold"), command=reset_timer)
btn_reset.grid(column=2, row=2)

lbl_checkpoint = Label(font=(FONT_NAME, 20, "bold"), bg=YELLOW, fg=GREEN)
lbl_checkpoint.grid(column=1, row=3)


mainloop()