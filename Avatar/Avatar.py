# Import the tkinter module and alias it as tk
import tkinter as tk

# From the tkinter module, import the filedialog submodule
from tkinter import filedialog

# Import the pyttsx3 module for text-to-speech conversion
import pyttsx3  

# Import the PIL module, specifically the Image and ImageTk modules
from PIL import Image, ImageTk



# Define a class named SpeakingAvatar
class SpeakingAvatar:
    # Define the __init__ method which initializes instances of the class
    def __init__(self, root):
        # Initialize the root window attribute
        self.root = root
        # Set the title of the root window to "Speaking Avatar"
        self.root.title("Speaking Avatar")


        # Initialize text-to-speech engine
        self.engine = pyttsx3.init()

        # Create and configure GUI
        self.create_gui()

    def create_gui(self):
        # Text Entry
        # Create a text entry widget within the root window with a width of 40 characters
        self.text_entry = tk.Entry(self.root, width=40)
        self.text_entry.pack(pady=10)
        # Pack the text entry widget with a vertical padding of 10 units

        # Speak Button
        speak_button = tk.Button(self.root, text="Speak", command=self.speak_text)
        speak_button.pack(pady=5)

        # Image Display
        self.avatar_image = Image.open("C:\\Users\\Lenovo\\Desktop\\man.gif")
        # Replace "avatar.png" with your avatar image
        self.avatar_photo = ImageTk.PhotoImage(self.avatar_image)
        # Create a label within the root window and set its image to the avatar PhotoImage
        self.avatar_label = tk.Label(self.root, image=self.avatar_photo)
        # Pack the avatar label with a vertical padding of 10 units
        self.avatar_label.pack(pady=10)

        # Load Image Button
        load_image_button = tk.Button(self.root, text="Load Image", command=self.load_image)
        load_image_button.pack(pady=5)

    # Define a method to speak the text entered by the user
def speak_text(self):
    # Get the text entered by the user from the text entry widget
    text = self.text_entry.get()
    
    # Check if the text is not empty
    if text:
        # Speak the text using the text-to-speech engine
        self.engine.say(text)
        
        # Wait for the speech to finish
        self.engine.runAndWait()

    # Define a method to load an image from the user's file system
def load_image(self):
    # Open a file dialog window to select an image file
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg;*.gif")])
    
    # Check if a file was selected
    if file_path:
        # Open the selected image file using PIL (Pillow) library
        self.avatar_image = Image.open(file_path)
        
        # Convert the image to a format compatible with Tkinter
        self.avatar_photo = ImageTk.PhotoImage(self.avatar_image)
        
        # Configure the avatar label widget to display the newly loaded image
        self.avatar_label.config(image=self.avatar_photo)


# Check if the script is being run directly as the main program
if __name__ == "__main__":
    # Create a Tkinter root window instance
    root = tk.Tk()
    
    # Create an instance of the SpeakingAvatar class with the root window as an argument
    app = SpeakingAvatar(root)
    
    # Enter the Tkinter event loop to display the GUI and handle user events
    root.mainloop()


