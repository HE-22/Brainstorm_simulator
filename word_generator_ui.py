import tkinter as tk
from main import generate_random_word
from images import PexelsAPI
from PIL import Image, ImageTk
import requests
from io import BytesIO


class WordGeneratorUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Random Word Generator")
        self.pexels_api = PexelsAPI()
        self.setup_ui()

    def setup_ui(self):
        # Position the window in the center of the screen
        window_width = 1000
        window_height = 500
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        position_top = int(screen_height / 2 - window_height / 2)
        position_right = int(screen_width / 2 - window_width / 2)
        self.root.geometry(
            f"{window_width}x{window_height}+{position_right}+{position_top}"
        )

        # Create a label to display the image
        self.image_label = tk.Label(self.root)
        self.image_label.pack(side="left", padx=10)

        # Create a label to display the word
        self.word_label = tk.Label(
            self.root, text="", font=("Helvetica", 50), justify="center"
        )
        self.word_label.pack(pady=20)

        # bind space bar to update_word_label function
        self.root.bind("<space>", lambda event: self.update_word_label())

        # Center the text both ways vertical and horizontal
        self.word_label.place(relx=0.5, rely=0.5, anchor="center")

    def update_word_label(self):
        """
        - Updates the word label with a new random word

        Args: None

        Returns: None
        """
        new_word = generate_random_word()
        self.word_label.config(text=new_word)
        self.image_label.config(image="")
        self.root.after(100, self.update_image_label, new_word)

    def update_image_label(self, word):
        """
        - Updates the image label with a new image from Pexels

        Args: word (str): The word to search for an image

        Returns: None
        """
        image_url = self.pexels_api.get_image_url(word)
        if image_url != "No image found for that query.":
            response = requests.get(image_url)
            img_data = response.content
            img = Image.open(BytesIO(img_data))
            img.thumbnail((200, 200), Image.Resampling.LANCZOS)
            img = ImageTk.PhotoImage(img)
            self.image_label.config(image=img)
            self.image_label.image = img

    def run(self):
        # Start the Tkinter event loop
        self.update_word_label()  # Generate a word immediately when the application is opened
        self.root.mainloop()


if __name__ == "__main__":
    app = WordGeneratorUI()
    app.run()
