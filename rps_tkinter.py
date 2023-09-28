import tkinter as tk
import random

def player_choice(user):
    computer = computer_choice()
    determine_winner(user, computer)

def computer_choice():
    choices = ["Rock", "Paper", "Scissor"]
    return random.choice(choices)

def determine_winner(player_choice, computer_choice):
    global player_score, computer_score
    choice_label.config(text=f"{player_choice} vs {computer_choice}")
    if player_choice == computer_choice:
        result_label.config(text="It's a draw!")
    elif ((player_choice == "Rock" and computer_choice == "Paper") or
          (player_choice == "Paper" and computer_choice == "Scissor") or
          (player_choice == "Scissor" and computer_choice == "Rock")):
        result_label.config(text="Computer wins!")
        computer_score += 1
        computer_score_label.config(text=f"Computer Score: {computer_score}")
    else:
        result_label.config(text="Player wins!")
        player_score += 1
        player_score_label.config(text=f"Player Score: {player_score}")
        
player_score = 0
computer_score = 0

window = tk.Tk()
window.geometry("600x400")
window.configure(background="skyblue")

## Create labels
title_label = tk.Label(text="Rock Paper Scissor Game", font=("Century", 20), bg="skyblue")
title_label.pack(padx=10, pady=30)
tk.Label(text="Player vs Computer", font=("Century", 18), bg="skyblue").pack()
choice_label = tk.Label(text="",font=("Century", 18), bg="skyblue")
choice_label.pack()
player_score_label = tk.Label(text=f"Player Score: {player_score}", bg ="skyblue")
player_score_label.pack()
computer_score_label = tk.Label(text=f"Computer Score: {computer_score}", bg ="skyblue")
computer_score_label.pack()
result_label = tk.Label(text="", bg ="skyblue")
result_label.pack()

## Create Buttons
rock_button = tk.Button(text="Rock", command=lambda: player_choice("Rock"))
rock_button.pack(side="left", padx=80)
paper_button = tk.Button(text="Paper", command=lambda: player_choice("Paper"))
paper_button.pack(side="left", padx=80)
scissor_button = tk.Button(text="Scissor", command=lambda: player_choice("Scissor"))
scissor_button.pack(side="left", padx=80)

window.mainloop()
