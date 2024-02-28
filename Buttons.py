import tkinter as tk
from genres import genres

class Buttons:
    def __init__(self, root):
        self.root = root
        self.dict = genres
        self.genre = None
        self.key_buttons = []
        self.val_buttons = []  
        self.show_keys()

    def show_keys(self):
        for key in self.dict:
            button = tk.Button(self.root, text=key, command=lambda k=key: self.on_key_click(k))
            button.pack()
            self.key_buttons.append(button)

    def on_key_click(self, key):
        if key == "No Preference":
            self.genre = None
            print("Selected genre:", None)
            self.root.destroy()
        else:
            self.genre = key
            self.clear_buttons(self.key_buttons)
            self.show_values()

    def show_values(self):
        values = self.dict[self.genre]
        for val in values:
            button = tk.Button(self.root, text=val, command=lambda v=val: self.on_val_click(v))
            button.pack()
            self.val_buttons.append(button)
        back_button = tk.Button(self.root, text="Go Back", command=self.go_back)
        back_button.pack()
        self.val_buttons.append(back_button)

    def on_val_click(self, val):
        if val is not "No Preference":
          self.genre = val
        print("Selected genre:", self.genre)
        self.root.destroy()

    def go_back(self):
        self.clear_buttons(self.val_buttons)
        self.show_keys()

    def clear_buttons(self, buttons):
        for b in buttons:
            b.pack_forget()

    def get_genre(self):
        return self.genre
