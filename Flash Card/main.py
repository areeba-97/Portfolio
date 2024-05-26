from tkinter import *
import pandas
from random import choice

# ------------------------------------   CONSTANTS   ---------------------------------------------#
BACKGROUND_COLOR = "#B1DDC6"
FONT1 = ("Ariel", 40, "italic")
FONT2 = ("Ariel", 40, "bold")
current_card = {}
to_learn = {}

# ----------------------------------   NEW FLASH CARDS -------------------------------------------#
try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/synonyms_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")


# ------------------------------------   FLIP THE CARD  ---------------------------------------------#
def next_card():
    """Generate new Flash Card."""
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = choice(to_learn)

    # Front Card
    canvas.itemconfig(card_title, text="Word", fill="black")
    canvas.itemconfig(card_text, text=current_card['Word'], fill="black")
    canvas.itemconfig(canvas_image, image=card_front_img)

    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    """Flips the Flash Card from front to back"""
    # Back Card
    canvas.itemconfig(card_title, text="Synonyms", fill="white")
    canvas.itemconfig(card_text, text=current_card['Synonyms'], fill="white")
    canvas.itemconfig(canvas_image, image=card_back_img)


# ------------------------------------   SAVE PROGRESS  ---------------------------------------------#
def is_known():
    to_learn.remove(current_card)
    new_file = pandas.DataFrame(to_learn)
    new_file.to_csv("data/words_to_learn.csv", index=False)
    next_card()


# --------------------------------------   UI SETUP   -----------------------------------------------#

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, func=flip_card)

# Canvas
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
# Card Front Image
card_front_img = PhotoImage(file="images/card_front.png")
# Card Back Image
card_back_img = PhotoImage(file="images/card_back.png")
canvas_image = canvas.create_image(400, 263, image=card_front_img)
# Card Title
card_title = canvas.create_text(400, 140, text="", font=FONT1)
# Card Text
card_text = canvas.create_text(400, 280, width=380, text="", font=FONT2)
canvas.grid(row=0, column=0, columnspan=2)

# Right Button
right_img = PhotoImage(file="images/right.png")
right_button = Button(image=right_img, highlightthickness=0, bd=0, command=is_known)
right_button.grid(row=1, column=1)

# Wrong Button
wrong_img = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_img, highlightthickness=0, bd=0, command=next_card)
wrong_button.grid(row=1, column=0)
next_card()

window.mainloop()
