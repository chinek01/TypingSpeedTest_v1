"""

Portfolio: Typing Speed Test
#100DaysOfCode with Python
Day: 85
Date: 2023-07-05
Author: MC

Another version of this project. Previous wos so bad :)

"""


from word_worker.word_worker import word_worker
from scoreboard.scoreboard import scoreboard
from tkinter import *
from time import strftime, gmtime
from tkinter.messagebox import showinfo


# ---------------------------- constance ------------------------------------ #
FONT_48 = ("NewYork", 48)
FONT_36 = ("NewYork", 36)
FONT_32 = ("NewYork", 32)
FONT_24 = ("NewYork", 24)
FONT_16 = ("NewYork", 16)

is_start_typing = False
timer = None
game_on = False
user_word = None
chosen_word = None

# ---------------------------- words mechanism ---------------------------- #
my_words = word_worker()
my_words.get_words_list('word_db.txt')


# ---------------------------- scoreboard mechanism ---------------------------- #

score = scoreboard()
score.reset_results()

# ---------------------------- timer mechanism ------------------------------------ #


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

        entry_word.config(
            state='normal'
        )
    else:
        global is_start_typing
        is_start_typing = False

        global game_on
        game_on = False
        entry_word.config(
            state='disabled'
        )

        global score
        showinfo(
            title="Your scores",
            message=f"You write {score.result()} words per min."
        )
        score.reset_results()


def word_enter(event):
    if event.char == ' ':
        global game_on

        if game_on is True:
            global chosen_word

            if chosen_word is not None:
                global user_word
                user_word = entry_word.get()

                global score
                if user_word.replace(" ", "").lower() == chosen_word:
                    score.add_answer(True)
                else:
                    score.add_answer(False)

        put_another_word()
        # cleaning entry control
        entry_word.delete('0', 'end')


def put_another_word():
    global game_on
    global user_word
    global chosen_word

    if game_on is False:
        game_on = True
        start_timer()

    if game_on is True:
        global chosen_word
        chosen_word = my_words.choice_word()
        word_label.config(
            text=chosen_word
        )

# ---------------------------- UI ------------------------------------ #


window = Tk()
window.title("Typing speed test by MC")
window.config(
    padx=100,
    pady=50,
    bg="#323232"
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

# ---------------------------- game controls ---------------------------- #

word_canvas = Canvas(
    width=550,
    height=100,
    bg='#a6a6a6',
    highlightthickness=0
)

word_canvas_text = word_canvas.create_text(
    550/2,
    50,
    text='Type max words you can.',
    fill='white',
    font=FONT_24,
)

word_canvas.grid(
    row=2,
    column=0
)

# word label
word_label = Label(
    text='word label',
    fg='gray',
    font=FONT_48,
)
word_label.grid(
    row=3,
    column=0,
    pady=40,
)

# entry
entry_word = Entry(
    font=FONT_32,
    width=50,
    justify='center',
)
entry_word.grid(
    row=4,
    column=0,
    pady=30,
)

# some hint
hint_label = Label(
    text="To start press space bar",
    font=FONT_16,
    fg="gray",
    pady=30,
)
hint_label.grid(
    row=5,
    column=0
)

# ---------------------------- timer start ---------------------------- #

entry_word.bind("<Key>", word_enter)

# start_timer()

window.mainloop()
