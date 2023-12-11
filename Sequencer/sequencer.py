import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

def word_break(s, word_dict):
    n = len(s)
    breakable = [False] * (n + 1)
    breakable[0] = True

    for i in range(1, n + 1):
        for j in range(i):
            if breakable[j] and s[j:i] in word_dict:
                breakable[i] = True
                break

    return breakable[n]

class WordBreakApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Sequencer")

        self.image = Image.open("./UnB.png")
        self.image.thumbnail((100, 100))
        self.photo = ImageTk.PhotoImage(self.image)
        self.image_label = tk.Label(root, image=self.photo)
        self.image_label.pack(pady=10)

        self.label = tk.Label(root, text="Digite uma palavra:", font=("Arial", 12))
        self.label.pack(pady=10)

        self.entry = tk.Entry(root, font=("Arial", 12), bd=2, relief="solid")
        self.entry.pack(pady=10)

        self.button = ttk.Button(root, text="Verificar", command=self.check_word, style="TButton")
        self.button.pack(pady=10)

        self.result_label = tk.Label(root, text="", font=("Arial", 12), fg="green")
        self.result_label.pack(pady=10)

        self.word_listbox = tk.Listbox(root, selectmode=tk.SINGLE, font=("Arial", 12), height=5)
        self.word_listbox.pack(pady=10)
        self.populate_word_listbox()

        self.add_word_button = ttk.Button(root, text="Adicionar Palavra", command=self.add_word, style="TButton")
        self.add_word_button.pack(pady=10)

    def check_word(self):
        user_input = self.entry.get().lower()
        result = word_break(user_input, word_dict)

        if result:
            self.result_label.config(text="A palavra pode ser quebrada!", fg="green")
        else:
            self.result_label.config(text="A palavra não pode ser quebrada!", fg="red")

    def populate_word_listbox(self):
        self.word_listbox.delete(0, tk.END)
        for word in word_dict:
            self.word_listbox.insert(tk.END, word)

    def add_word(self):
        new_word = self.entry.get().lower()
        if new_word not in word_dict:
            word_dict.append(new_word)
            self.populate_word_listbox()

if __name__ == "__main__":
    word_dict = ["leet", "code", "python", "program", "dynamic", "programming"]

    root = tk.Tk()
    app = WordBreakApp(root)
    root.geometry("600x500") 
    root.mainloop()
