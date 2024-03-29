import tkinter as tk
from tkinter import ttk  # Import ttk for Treeview
from PIL import Image, ImageTk
import random

class RockPaperScissorsApp:
    def __init__(self, master):
        self.master = master
        master.title("Rock, Paper, Scissors")
        master.geometry("300x500")  # Set window size

        # Load images
        self.rock_img = ImageTk.PhotoImage(Image.open("src/rock.png").resize((100, 100)))
        self.paper_img = ImageTk.PhotoImage(Image.open("src/paper.png").resize((100, 100)))
        self.scissors_img = ImageTk.PhotoImage(Image.open("src/scissors.png").resize((100, 100)))

        # Frame for Rock
        self.create_option_frame("Rock", self.rock_img)

        # Frame for Paper
        self.create_option_frame("Paper", self.paper_img)

        # Frame for Scissors
        self.create_option_frame("Scissors", self.scissors_img)

        # Result label
        self.result_label = tk.Label(master, text="")
        self.result_label.pack()

        # Game history
        self.game_history = []

        # History button
        self.history_button = tk.Button(master, text="History", command=self.show_history)
        self.history_button.pack()

    def create_option_frame(self, option_name, image):
        frame = tk.Frame(self.master)
        frame.pack(anchor=tk.N, pady=10)

        button = tk.Button(frame, image=image, command=lambda option=option_name: self.play(option))
        button.pack()

        label = tk.Label(frame, text=option_name)
        label.pack()

    def play(self, player_choice):
        self.result_label.config(text=f"You chose {player_choice}.")

        for widget in self.master.winfo_children():
            if isinstance(widget, tk.Frame):
                widget.winfo_children()[0].config(state="disabled")  # Disable button

        choices = ["Rock", "Paper", "Scissors"]
        computer_choice = random.choice(choices)

        # Record the game
        self.game_history.append({"player_choice": player_choice, "computer_choice": computer_choice})

        self.master.after(2000, self.show_result, player_choice, computer_choice)

    def show_result(self, player_choice, computer_choice):
        if player_choice == computer_choice:
            result = "It's a tie!"
        elif (player_choice == "Rock" and computer_choice == "Scissors") or \
             (player_choice == "Paper" and computer_choice == "Rock") or \
             (player_choice == "Scissors" and computer_choice == "Paper"):
            result = "You win!"
        else:
            result = "Computer wins!"

        self.result_label.config(text=f"Computer chose {computer_choice}. {result}")

        for widget in self.master.winfo_children():
            if isinstance(widget, tk.Frame):
                widget.winfo_children()[0].config(state="normal")  # Enable button

    def show_history(self):
        history_window = tk.Toplevel(self.master)
        history_window.title("Game History")
        history_window.geometry("100x100")  # Set window size to 100x100

        # Create a table to display game history
        tree = ttk.Treeview(history_window, columns=("Player Choice", "Computer Choice", "Result"))
        tree.heading("#0", text="Game #")
        tree.heading("Player Choice", text="Player Choice")
        tree.heading("Computer Choice", text="Computer Choice")
        tree.heading("Result", text="Result")
        
        # Insert game records into the table
        for i, record in enumerate(self.game_history, start=1):
            tree.insert("", "end", text=str(i), values=(record["player_choice"], record["computer_choice"], self.calculate_result(record["player_choice"], record["computer_choice"])))
        
        tree.pack(expand=True, fill=tk.BOTH)

    def calculate_result(self, player_choice, computer_choice):
        if player_choice == computer_choice:
            return "Tie"
        elif (player_choice == "Rock" and computer_choice == "Scissors") or \
             (player_choice == "Paper" and computer_choice == "Rock") or \
             (player_choice == "Scissors" and computer_choice == "Paper"):
            return "Win"
        else:
            return "Loss"

def main():
    root = tk.Tk()
    app = RockPaperScissorsApp(root)
    root.geometry("+50+50")  # Set window position to top-left corner
    root.mainloop()

if __name__ == "__main__":
    main()
