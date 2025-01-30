import tkinter as tk
import subprocess
import os
from PIL import Image, ImageTk

def launch_shortcut():
    shortcut_path = os.path.abspath("../__Launch_NoSteam.lnk")
    if os.path.exists(shortcut_path):
        try:
            subprocess.run(["cmd", "/c", shortcut_path], shell=True)
        except subprocess.CalledProcessError as e:
            print(f"Failed to launch the shortcut: {e}")
    else:
        print("Shortcut not found!")

def launch_config():
    config_path = os.path.abspath("../Config.exe")
    if os.path.exists(config_path):
        try:
            subprocess.run(["cmd", "/c", config_path], shell=True)
        except subprocess.CalledProcessError as e:
            print(f"Failed to launch Config: {e}")
    else:
        print("Config.exe not found!")

# Create main window
root = tk.Tk()
root.title("Reloaded")
root.geometry("400x300")  # Medium-sized window
root.configure(bg="#2C2C2C")  # Dark grey background

# Load and display image above button
image_path = "menu1.png"  # Change to your image file path
if os.path.exists(image_path):
    image = Image.open(image_path)
    max_size = (250, 100)
    image.thumbnail(max_size, Image.Resampling.LANCZOS)  # Keep aspect ratio
    img = ImageTk.PhotoImage(image)
    image_label = tk.Label(root, image=img, bg="#2C2C2C")
    image_label.pack(pady=(20, 10), anchor="w")

# Add a launch button with Bootstrap-like styling
launch_button = tk.Button(root, text="Launch Game", command=launch_shortcut, font=("Arial", 14, "bold"), bg="#007BFF", fg="white", padx=20, pady=10, borderwidth=0, relief="flat")
launch_button.pack(pady=10, anchor="w", padx=20)

# Add a config button with Bootstrap-like styling
config_button = tk.Button(root, text="Video Config", command=launch_config, font=("Arial", 14, "bold"), bg="#28A745", fg="white", padx=20, pady=10, borderwidth=0, relief="flat")
config_button.pack(pady=10, anchor="w", padx=20)

# Add small text at bottom right
footer_label = tk.Label(root, text="Lewis Jones - gigabitmouse@gmail.com\nCameron Hughes - crhughes.robotics@gmail.com", font=("Arial", 8), fg="white", bg="#2C2C2C", anchor="se", justify="right")
footer_label.place(relx=1.0, rely=1.0, anchor="se", x=-10, y=-10)

# Run the GUI
root.mainloop()
