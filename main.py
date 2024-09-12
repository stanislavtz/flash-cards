from tkinter import *
from tkinter import messagebox

import random as rn
import pandas as pd

BACKGROUND_COLOR = "#B1DDC6"


def get_random_word():
	try:
		data = pd.read_csv("data/french_words.csv")
	except FileNotFoundError:
		messagebox.showinfo(title="ERROR", message="File Not Found")
	else:
		data_dict = data.to_dict(orient="records")
		current_word = rn.choice(data_dict)
		canvas.itemconfig(word_text, text=current_word["French"])



window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas()
card_front_img = PhotoImage(file="images/card_front.png")
canvas.config(width=800, height=600, bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.create_image(400, 300, image=card_front_img)
title_text = canvas.create_text(400, 200, text="French", font=("Ariel", 40, "italic"))
word_text = canvas.create_text(400, 350, text="French Word", font=("Ariel", 50, "normal"))
canvas.grid(row=0, column=0, columnspan=2)

x_image = PhotoImage(file="images/wrong.png")
wrong_btn = Button(image=x_image, highlightthickness=0, command=get_random_word)
wrong_btn.grid(row=1, column=0)

v_image = PhotoImage(file="images/right.png")
wrong_btn = Button(image=v_image, highlightthickness=0, command=get_random_word)
wrong_btn.grid(row=1, column=1)

get_random_word()

window.mainloop()
