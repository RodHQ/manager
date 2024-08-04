import tkinter as tk
from gui import SalesApp

def main():
    root = tk.Tk()
    app = SalesApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
