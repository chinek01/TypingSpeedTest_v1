"""

Portfolio: Typing Speed Test
#100DaysOfCode with Python
Day: 85
Date: 2023-07-05
Author: MC

Another version of this project. Previous wos so bad :)

"""


from word_worker.word_worker import word_worker
from tkinter import *
from time import strftime, gmtime


# ---------------------------- constance ------------------------------------ #
FONT_48 = ("NewYork", 48)
FONT_36 = ("NewYork", 36)
FONT_32 = ("NewYork", 32)
FONT_24 = ("NewYork", 24)
FONT_16 = ("NewYork", 16)

is_start_typing = False
timer = None

# ---------------------------- words mechanizm ---------------------------- #
my_words = word_worker()
my_words.get_words_list('word_db.txt')

# ---------------------------- timer mechanizm ------------------------------------ #


def start_timer():
    global is_start_typing

    if not is_start_typing:
        is_start_typing = True

        count_down(60)


def count_down(count):
    global timer

    time_format = "%M:%S"

    timer_canvas.itemconfig(
        timer_text,
        text=strftime(time_format,
                      gmtime(count))
    )

    if count > 0:
        timer = window.after(
            1000,
            count_down,
            count - 1
        )


# ---------------------------- UI ------------------------------------ #

window = Tk()
window.title("Typing speed test by MC")
window.config(
    padx=100,
    pady=50,
    # bg= # todo: do zastanowienia się
)
window.minsize(
    width=800,
    height=600,
)

# title label
title_label = Label(
    text="Typing speed test",
    font=FONT_48,
    fg='white',
    pady=15,
)
title_label.grid(
    row=0,
    column=0,
)

# canvas property
timer_canvas = Canvas(
    width=550,
    height=100,
    bg='gray',
    highlightthickness=0
)

timer_text = timer_canvas.create_text(
    550/2,
    50,
    text="01:00",
    fill='white',
    font=FONT_32
)

timer_canvas.grid(
    row=1,
    column=0)

word_canvas = Canvas(
    width=550,
    height=500,
    bg='#a6a6a6',
    highlightthickness=0
)

word_canvas_text = word_canvas.create_text(
    550/2,
    25,
    text='Type max words you can.',
    fill='white',
    font=FONT_24,
)

word_canvas.grid(
    row=2,
    column=0
)

start_timer()


window.mainloop()

