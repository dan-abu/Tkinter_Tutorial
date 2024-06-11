"""Write a Python GUI program to import Tkinter package and create a window and set its title."""
from tkinter import *
import sys
def close_window(root):
    """Closes GUI window"""
    root.destroy()
    sys.exit()

def create_window(title="Tkinter Test"):
    """Creates window with user-defined title or default 'Tkinter Test'."""
    print("Loading window...")
    root = Tk()
    try:
        if len(sys.argv) < 2:
            root.title(title)
            root.after(5000, lambda: close_window(root))
            root.mainloop()
            print("Successfully loaded window.")
        else:
            root.title(sys.argv[1])
            root.after(5000, lambda: close_window(root))
            root.mainloop()
            print("Successfully loaded window.")
    except Exception as e:
        print("Failed to load window. Probably a user input issue.")
        print(e)
        raise e
    finally:
        print("Session ended.")

if __name__ == "__main__":
    create_window()