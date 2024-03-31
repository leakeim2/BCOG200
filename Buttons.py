import tkinter as tk
from genres import genres

class Buttons:
    def __init__(self, root):
        self.root = root
        self.dict = genres
        self.genre = None
        self.buttons = [] 
        self.show_keys()

    def show_keys(self):
        numCol = 3
        currentCol = 0
        currentRow = 0
        for key in self.dict:
            button = tk.Button(self.root, text=key, command=lambda k=key: self.on_key_click(k))
            button.grid(row=currentRow,column=currentCol,padx=5,pady=5)
            self.buttons.append(button)
            currentCol+=1
            if currentCol >= numCol:
                currentCol = 0
                currentRow+=1

    def on_key_click(self, key):
        self.genre = key
        self.root.destroy()

    def get_genre(self):
        return self.genre

def createButtons():
    root = tk.Tk()
    b = Buttons(root)
    root.mainloop()
    return b.get_genre()
