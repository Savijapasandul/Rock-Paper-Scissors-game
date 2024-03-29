# Rock Paper Scissors game
This Python code implements a Rock, Paper, Scissors game using the Tkinter library for the graphical user interface (GUI). Here's a brief description of its functionality:

GUI Setup: The code creates a main window with options for Rock, Paper, and Scissors displayed as buttons with corresponding images.

Game Logic: When a player selects an option, the code generates a random choice for the computer and determines the winner based on the classic rules of the game (Rock beats Scissors, Scissors beats Paper, Paper beats Rock).

Result Display: After the player's choice is made, the result (win, loss, or tie) is displayed in a label on the GUI.

Game History: The code keeps track of game records, including the player's choice, computer's choice, and the result of each game. There's a button to view the game history, which opens a new window displaying a table with the game records.

User Interaction: The GUI allows users to play the game by clicking on buttons, view the result of each game, and access the game history.


To run this code, follow these steps:

Install Python: Make sure you have Python installed on your system. You can download Python from the official website: https://www.python.org/downloads/

Install Required Libraries: You need to have the tkinter library, which is usually included with Python, and Pillow, which is used for working with images. You can install Pillow using pip, the Python package installer. Open your command line interface (CLI) and run:

pip install Pillow

Prepare Images: Ensure you have image files named rock.png, paper.png, and scissors.png in a folder named src in the same directory as your Python script. Alternatively, you can modify the file paths in the code to match the location of your image files.

Run the Script: Save the provided Python script to a file, for example, rock_paper_scissors.py. Then, open your CLI, navigate to the directory containing the script, and run the script using Python:

python rock_paper_scissors.py

Play the Game: After running the script, a window should appear displaying the Rock, Paper, Scissors game. Click on one of the options to make your choice and see the result. You can also click on the "History" button to view the game history.

Close the Game: You can close the game window by clicking the close button (X) on the window or by terminating the Python process in your CLI.