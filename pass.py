import tkinter as tk
from tkinter import messagebox, Listbox
import random
import json
import string

class PasswordGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Random Password Generator")

        # Ползунок длины пароля
        self.length_label = tk.Label(root, text="Длина пароля:")
        self.length_label.pack(pady=5)

        self.length_slider = tk.Scale(root, from_=6, to_=20, orient='horizontal')
        self.length_slider.set(12)  # Устанавливаем значение по умолчанию
        self.length_slider.pack(pady=5)

        # Чекбоксы для выбора символов
        self.include_uppercase = tk.BooleanVar()
        self.uppercase_checkbox = tk.Checkbutton(root, text="Включить заглавные буквы", variable=self.include_uppercase)
        self.uppercase_checkbox.pack(pady=5)

        self.include_numbers = tk.BooleanVar()
        self.numbers_checkbox = tk.Checkbutton(root, text="Включить цифры", variable=self.include_numbers)
        self.numbers_checkbox.pack(pady=5)

        self.include_special = tk.BooleanVar()
        self.special_checkbox = tk.Checkbutton(root, text="Включить спецсимволы", variable=self.include_special)
        self.special_checkbox.pack(pady=5)

        # Кнопка генерации
        self.generate_button = tk.Button(root, text="Сгенерировать пароль", command=self.generate_password)
        self.generate_button.pack(pady=10)

        # Таблица истории
        self.history_label = tk.Label(root, text="История паролей:")
        self.history_label.pack(pady=5)

        self.history_list = Listbox(root, width=50)
        self.history_list.pack(pady=5)

        # Загрузка истории из файла
        self.history = []
        self.load_history()

    def generate_password(self):
        length = self.length_slider.get()
        
        if length < 6 or length > 20:
            messagebox.showerror("Ошибка", "Длина пароля должна быть от 6 до 20 символов.")
            return
        
        characters = string.ascii_lowercase  # Всегда добавляем строчные буквы
        
        if self.include_uppercase.get():
            characters += string.ascii_uppercase
        if self.include_numbers.get():
            characters += string.digits
        if self.include_special.get():
            characters += string.punctuation
            password = ''.join(random.choice(characters) for _ in range(length))
        
        self.history.append(password)
        self.update_history_display()
        
    def update_history_display(self):
        self.history_list.delete(0, tk.END)
        for password in self.history:
            self.history_list.insert(tk.END, password)
            
    def load_history(self, filename='history.json'):
        try:
            with open(filename, 'r') as f:
                self.history = json.load(f)
                self.update_history_display()
        except FileNotFoundError:
            pass

    def save_history(self, filename='history.json'):
        with open(filename, 'w') as f:
            json.dump(self.history, f)

    def on_closing(self):
        self.save_history()
        self.root.destroy()

# Запуск приложения
if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordGeneratorApp(root)
    root.protocol("WM_DELETE_WINDOW", app.on_closing)
    root.mainloop()
