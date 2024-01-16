import tkinter as tk
from main import generate_random_word


def update_word_label():
    """
    - Updates the word label with a new random word

    Args: None

    Returns: None
    """
    new_word = generate_random_word()
    word_label.config(text=new_word)


# Create the main window
root = tk.Tk()
root.title("Random Word Generator")

# Position the window in the center of the screen
window_width = 300
window_height = 100
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
position_top = int(screen_height / 2 - window_height / 2)
position_right = int(screen_width / 2 - window_width / 2)
root.geometry(f"{window_width}x{window_height}+{position_right}+{position_top}")

# Create a label to display the word
word_label = tk.Label(root, text="", font=("Helvetica", 50), justify="center")
word_label.pack(pady=20)

# bind space bar to update_word_label function
root.bind("<space>", lambda event: update_word_label())

# Center the text both ways vertical and horizontal
word_label.place(relx=0.5, rely=0.5, anchor="center")

if __name__ == "__main__":
    # Start the Tkinter event loop
    update_word_label()  # Generate a word immediately when the application is opened
    root.mainloop()
