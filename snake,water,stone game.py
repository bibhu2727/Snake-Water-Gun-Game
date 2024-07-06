import random
import sys
import os
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
from pygame import mixer
from tkinter.font import Font

# Initialize pygame mixer
mixer.init()

# Load audio files
click_sound = mixer.Sound('click.wav')
win_sound = mixer.Sound('win.wav')
lose_sound = mixer.Sound('lose.wav')
draw_sound = mixer.Sound('draw.wav')

# Mapping for user input and computer choices
youDict = {"s": 1, "w": -1, "g": 0}
reverseDict = {1: "Snake", -1: "Water", 0: "Gun"}

# Create the main window
root = tk.Tk()
root.title("Snake Water Gun Game")

# Full paths to the images
base_dir = os.path.dirname(os.path.abspath(__file__))
snake_img_path = os.path.join(base_dir, "snake.png")
water_img_path = os.path.join(base_dir, "water.png")
gun_img_path = os.path.join(base_dir, "gun.png")

# Image dimensions (adjust as necessary)
img_width, img_height = 100, 100

# Load and resize images
try:
    print("Loading and resizing images...")
    snake_img = Image.open(snake_img_path).resize((img_width, img_height), Image.Resampling.LANCZOS)
    water_img = Image.open(water_img_path).resize((img_width, img_height), Image.Resampling.LANCZOS)
    gun_img = Image.open(gun_img_path).resize((img_width, img_height), Image.Resampling.LANCZOS)
    
    snake_img = ImageTk.PhotoImage(snake_img)
    water_img = ImageTk.PhotoImage(water_img)
    gun_img = ImageTk.PhotoImage(gun_img)
    
    print("Images loaded and resized successfully.")
except Exception as e:
    messagebox.showerror("Error", f"Failed to load or resize images: {e}")
    sys.exit(1)

def play(choice):
    mixer.Sound.play(click_sound)
    computer = random.choice([-1, 0, 1])
    you = youDict[choice]

    user_choice_label.config(image=images[choice])
    comp_choice_label.config(image=images[reverseDict[computer]])

    if computer == you:
        result.set("It's a draw!")
        mixer.Sound.play(draw_sound)
    elif (computer == -1 and you == 1) or (computer == 1 and you == 0) or (computer == 0 and you == -1):
        result.set("You win!")
        mixer.Sound.play(win_sound)
    else:
        result.set("You lose!")
        mixer.Sound.play(lose_sound)

# Images dictionary
images = {
    "s": snake_img,
    "w": water_img,
    "g": gun_img,
    "Snake": snake_img,
    "Water": water_img,
    "Gun": gun_img
}

# Create widgets
user_choice_label = tk.Label(root, text="Your Choice", font=("Arial", 14))
comp_choice_label = tk.Label(root, text="Computer's Choice", font=("Arial", 14))
result = tk.StringVar()
result_label = tk.Label(root, textvariable=result, font=("Arial", 20))

snake_button = tk.Button(root, image=snake_img, command=lambda: play("s"))
water_button = tk.Button(root, image=water_img, command=lambda: play("w"))
gun_button = tk.Button(root, image=gun_img, command=lambda: play("g"))

# Load custom font for the signature
try:
    cursive_font = Font(family="Brush Script MT", size=16, slant="italic")
except:
    cursive_font = Font(family="Helvetica", size=16, slant="italic")

signature_label = tk.Label(root, text="Developed by BIBHU", font=cursive_font, fg="blue")

# Layout widgets
user_choice_label.grid(row=0, column=0, padx=20, pady=10)
comp_choice_label.grid(row=0, column=1, padx=20, pady=10)
result_label.grid(row=2, column=0, columnspan=3, pady=10)

snake_button.grid(row=1, column=0, padx=10, pady=10)
water_button.grid(row=1, column=1, padx=10, pady=10)
gun_button.grid(row=1, column=2, padx=10, pady=10)

# Place the signature label at the bottom
signature_label.grid(row=3, column=0, columnspan=3, pady=20)

# Start the main loop
root.mainloop()
