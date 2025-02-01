from tkinter import *
import time


# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 4
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0

# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(count_down)
    canvas.itemconfig(timer_text, text="00:00")
    text.config(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50, "bold"))
    check_marks.config(text="")
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps 
    reps +=1
    if reps % 8 == 0:
        count_down(LONG_BREAK_MIN * 60)
        text.config(text="Break", fg=RED, bg=YELLOW, font=(FONT_NAME, 50, "bold"))
    elif reps % 2 == 0:
        count_down(SHORT_BREAK_MIN * 60)
        text.config(text="Break", fg=PINK, bg=YELLOW, font=(FONT_NAME, 50, "bold"))
    else:
        count_down(WORK_MIN)
        text.config(text="Work", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50, "bold"))

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
	
    minutes = count // 60
    seconds = count % 60
    if seconds < 10:
        seconds = f"0{seconds}"

    if minutes < 10:
        minutes = f"0{minutes}"

    canvas.itemconfig(timer_text, text=f"{minutes}:{seconds}")

    if count > 0:
        window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        work_sessions = reps // 2
        for _ in range(work_sessions):
            marks += "✔"
        check_marks.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()

window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

text = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50, "bold"))
text.grid(column=1, row=0)

canvas = Canvas(width=200, height=224)
tom_img = PhotoImage(file=r"logos\tomato.png")
canvas.create_image(103, 112, image=tom_img)
timer_text= canvas.create_text(103, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1) 
start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

restart_button = Button(text="Restart", highlightthickness=0, command=reset_timer)
restart_button.grid(column=2, row=2)

check_marks = Label(fg=GREEN, bg=YELLOW)
check_marks.grid(column=1, row=3)

window.mainloop()