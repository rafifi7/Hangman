# Practice for coding and making guis
# Hangman
# Author: Rafee Adnan
# Date created: 12/21/2023

import tkinter as tk
from tkinter import font as tkFont

#Global strings

g_blanks = ""
g_phrase = ""
g_pic = "0"

g_file_path = "C:\\Users\\rafee\\OneDrive\\Desktop\\Hangman\\Pictures\\"
g_png= ".png"


#GUI functions

def press_play():
    for widget in root.winfo_children():
        widget.destroy()
    title_font = tkFont.Font(family='Helvetica', size=36, weight='bold')
    title_frame=tk.Frame(root)
    title_frame.configure(background='lightblue')
    title_frame.pack(side='top', pady=80)

    enter_label = tk.Label(title_frame, text="Enter a word or phrase:", font=title_font, background='lightblue')
    enter_label.pack()

    submit_font = tkFont.Font(family='Helvetica', size=20, weight='bold')

    entry = tk.Entry(root, font=submit_font)
    entry.pack(pady=(10,50), padx=40)

    submit_button = tk.Button(root, text="   Submit   ", command=lambda: create_board(entry.get()), font=submit_font)
    submit_button.pack(pady=30)

    back_button = tk.Button(root, text="Main Menu", command=show_main_menu, font=submit_font)
    back_button.pack(pady=30)

def create_board(user_input):
    for widget in root.winfo_children():
        widget.destroy()

    title_font = tkFont.Font(family='Helvetica', size=36, weight='bold')
    submit_font = tkFont.Font(family='Helvetica', size=20, weight='bold')

    blanks_arr = []
    for letter in user_input:
        if letter == " ":
            blanks_arr.append("   ")
        else:
            blanks_arr.append("_ ")

    blanks = ''.join(blanks_arr)

    g_blanks = blanks
    g_phrase = user_input.upper()

    letters_used = tk.Label(root, text="Letters Used\n----------------------", font=submit_font, background='lightblue')
    letters_used.pack(side='left', pady=10, padx= (100, 0))
    
    pic = g_file_path + g_pic + g_png

    hangman_image = tk.PhotoImage(file=pic)
    image_label = tk.Label(root, image=hangman_image)
    image_label.pack(side='right', pady = 10, padx =(0,100))


    blanks_label = tk.Label(root, text=blanks, font=title_font, background='lightblue')
    blanks_label.pack(pady=100)

    entry = tk.Entry(root, font=submit_font)
    entry.pack(pady=(10,50))

    guess_button = tk.Button(root, text="  Guess A Letter  ", command=lambda: update_board(entry.get().upper()), font=submit_font)
    guess_button.pack(pady=30)

    


def update_board(guess):
    for widget in root.winfo_children():
        widget.destroy()
    print(guess)

def press_instr():
    for widget in root.winfo_children():
        widget.destroy()
    
    title_font = tkFont.Font(family='Helvetica', size=36, weight='bold')
    title_frame = tk.Frame(root)
    title_frame.configure(background='lightblue')
    title_frame.pack(side='top', pady=(100, 0))

    instr_label = tk.Label(title_frame, text="Instructions", font=title_font, anchor='center', background='lightblue')
    instr_label.pack()

    button_font = tkFont.Font(family='Helvetica', size=20, weight='bold')
    
    text_frame = tk.Frame(root)
    text_frame.configure(background='lightblue')
    text_frame.pack(pady=(50, 10))
    text_font = tkFont.Font(family='Helvetica', size=15)
    text = """
            2 Players Needed
            \nPlayer 1 will enter a custom phrase for the other player to guess.
            \nPlayer 2 will then enter letters to guess the phrase.
            \nCorrect letters will show up in the blanks while incorrect letters will cause the hangman to show up limb by limb.
            \n If the hangman is fully shown (5 incorrect guesses), Player 2 has lost.
            \nIf Player 2 figures out the phrase before the hangman shows up, Player 1 has lost.
            """
    text_label = tk.Label(text_frame, text=text, font=text_font, background='lightblue')
    text_label.pack()

    # Create the frame for the back button
    back_frame = tk.Frame(root)
    back_frame.pack(pady=40)  

    back_button = tk.Button(back_frame, text="Main Menu", command=show_main_menu, font=button_font)
    back_button.pack()

def press_quit():
    root.destroy()

def show_main_menu():
    for widget in root.winfo_children():
        widget.destroy()

    root.configure(background='lightblue')

    title_frame = tk.Frame(root)
    title_frame.configure(background='lightblue')
    title_frame.pack()

    title_font = tkFont.Font(family='Helvetica', size=36, weight='bold')
    title_label = tk.Label(title_frame, text="Hangman", font = title_font, background='lightblue')
    title_label.pack(pady= (100, 60))

    button_font = tkFont.Font(family='Helvetica', size=20, weight='bold')

    play_frame = tk.Frame(root)
    play_frame.pack(pady=25)

    play_button = tk.Button(play_frame, text="       Play       ", command=press_play, font=button_font)
    play_button.pack()  

    instr_frame = tk.Frame(root)
    instr_frame.pack(pady=25)

    instr_button = tk.Button(instr_frame, text=" Instructions ", command=press_instr, font=button_font)
    instr_button.pack()  

    quit_frame = tk.Frame(root)
    quit_frame.pack(pady=25)

    quit_button = tk.Button(quit_frame, text="       Quit       ", command=press_quit, font=button_font)
    quit_button.pack()

#GUI

root = tk.Tk()
root.title("Hangman")
root.resizable(True, True)
root.geometry("1280x720")

# i want the background to have a moving banner of a bunch of random letters


show_main_menu()

root.mainloop()










