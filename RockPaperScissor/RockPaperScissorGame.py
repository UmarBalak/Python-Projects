import tkinter as tk
import random

computer_choices = ["Rock", "Paper", "Scissor"]

def reset_game():
    b1.config(state="active")
    b2.config(state="active")
    b3.config(state="active")
    player_label.config(text="You              ")
    computer_label.config(text="Computer")
    result_label.config(text="")

def disable_buttons():
    b1.config(state="disable")
    b2.config(state="disable")
    b3.config(state="disable")

def play(player_choice):
    computer_choice = random.choice(computer_choices)
    if computer_choice == player_choice:
        match_result = "Match Draw"
    elif (computer_choice == "Rock" and player_choice == "Scissor") or (computer_choice == "Paper" and player_choice == "Rock") or (computer_choice == "Scissor" and player_choice == "Paper"):
        match_result = "Computer Win"
    else:
        match_result = "You Win"
    result_label.config(text=match_result)
    player_label.config(text=f"{player_choice: <16}")
    computer_label.config(text=computer_choice)
    disable_buttons()

root = tk.Tk()
root.geometry("400x400")
root.title("Rock Paper Scissor Game")

tk.Label(root, text="Rock Paper Scissor", font="normal 20 bold", fg="blue").pack(pady=20)

frame = tk.Frame(root)
frame.pack()

player_label = tk.Label(frame, text="  You            ", font=10)
vs_label = tk.Label(frame, text="     VS                ", font="normal 10 bold")
computer_label = tk.Label(frame, text="Computer", font=10)

player_label.pack(side=tk.LEFT)
vs_label.pack(side=tk.LEFT)
computer_label.pack()

result_label = tk.Label(root, text="", font="normal 20 bold", bg="white", width=15, borderwidth=2, relief="solid")
result_label.pack(pady=20)

frame1 = tk.Frame(root)
frame1.pack()

b1 = tk.Button(frame1, text="Rock", font=10, width=7, command=lambda: play("Rock"))
b2 = tk.Button(frame1, text="Paper", font=10, width=7, command=lambda: play("Paper"))
b3 = tk.Button(frame1, text="Scissor", font=10, width=7, command=lambda: play("Scissor"))

b1.pack(side=tk.LEFT, padx=10)
b2.pack(side=tk.LEFT, padx=10)
b3.pack(padx=10)

tk.Button(root, text="Reset Game", font=10, fg="red", bg="black", command=reset_game).pack(pady=20)

root.mainloop()
