from tkinter import *

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


def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text= "00:00")
    title_label.config(text= "Timer", fg= GREEN)
    check_mark.config(text= "")
    global reps
    reps = 0


def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60    
    long_break_sec = LONG_BREAK_MIN * 60
    
    if reps % 8 == 0:
        count_down(long_break_sec)
        title_label.config(text= "Break", fg= RED)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        title_label.config(text= "Break", fg= PINK)
    else:
        count_down(work_sec)
        title_label.config(text= "Work", fg= GREEN)


def count_down(count):
    count_min = count // 60
    count_secs = count % 60
    if count_secs < 10:
        count_secs = f"0{count_secs}"
    canvas.itemconfig(timer_text, text= f"{count_min}:{count_secs}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        mark = ""
        for _ in range(reps // 2):
            mark += "✔︎"
        check_mark.config(text= mark)


window = Tk()
window.title("Pomodoro")
window.config(padx= 100,  pady=50, bg= YELLOW)


title_label = Label(text= "Timer", fg= GREEN, font= (FONT_NAME, 50), bg= YELLOW)
title_label.grid(column=1, row=0)


canvas = Canvas(width=200, height= 224, bg= YELLOW, highlightthickness=0)
photo_image = PhotoImage(file="/Users/muhammadhamdazam/Documents/Python Programs/Day 28/pomodoro-start/tomato.png")
canvas.create_image(100, 112, image= photo_image)
timer_text = canvas.create_text(100, 130, text= "00:00", fill= "white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

start_button = Button(text="Start", highlightthickness=0, highlightbackground=YELLOW, command= start_timer)
reset_button = Button(text="Reset", highlightthickness=0, highlightbackground=YELLOW, command= reset_timer)

start_button.grid(column=0, row=2)
reset_button.grid(column=2, row=2)

check_mark = Label(fg= GREEN, bg= YELLOW)
check_mark.grid(column=1, row=3)

window.mainloop()