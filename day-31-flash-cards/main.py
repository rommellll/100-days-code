from tkinter import *
import pandas as pd
import random


to_learn = {}
BACKGROUND_COLOR = "#B1DDC6"
try:
    data_word = pd.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pd.read_csv("data/filipino_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data_word.to_dict(orient="records")

current_card = {}


def next_card():
    global current_card, flip
    window.after_cancel(flip)
    current_card = random.choice(to_learn)
    if current_card["Filipino"] in shown_cards:
        current_card = random.choice(to_learn)
    canvas.itemconfig(bg_img, image=card_front_img)
    canvas.itemconfig(lang_text, text="Filipino", fill="black")
    canvas.itemconfig(word_text, text=current_card["Filipino"], fill="black")
    flip = window.after(3000, flip_card)


def flip_card():
    canvas.itemconfig(bg_img, image=card_back_img)
    canvas.itemconfig(lang_text, text="English", fill="white")
    canvas.itemconfig(word_text, text=current_card["English"], fill="white")


def correct_guess():
    to_learn.remove(current_card)
    print(len(to_learn))
    data = pd.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv")
    # new_data = [item for item in new_data if item.get('Filipino') != current_card["Filipino"]]
    # words_to_learn = pd.DataFrame(new_data)
    # words_to_learn.to_csv("data/words_to_learn.csv", index=False)
    next_card()


window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip = window.after(3000, flip_card)

# images
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
wrong_img = PhotoImage(file="images/wrong.png")
right_img = PhotoImage(file="images/right.png")

# Front card
canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
bg_img = canvas.create_image(400, 263, image=card_front_img)
canvas.grid(column=1, row=1, columnspan=2)
lang_text = canvas.create_text(400, 150, text="",font=("Arial", 40, "italic"))
word_text = canvas.create_text(400, 263, text="",font=("Arial", 60, "bold"))

# Buttons
wrong_button = Button(image=wrong_img, highlightthickness=0, command=next_card)
wrong_button.grid(column=2, row=2)
correct_button = Button(image=right_img, highlightthickness=0, command=correct_guess)
correct_button.grid(column=1, row=2)


next_card()
window.mainloop()