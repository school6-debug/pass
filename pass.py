import tkinter as tk
from tkinter import ttk
import random
import json
import os
from datetime import datetime

# Основное окно
root = tk.Tk()
root.title("Random Password Generator")

# Ползунок для длины пароля
length_var = tk.IntVar(value=12)
length_scale = tk.Scale(root, from_=4, to=64, orient=tk.HORIZONTAL, label="Длина пароля", variable=length_var)
length_scale.pack()

# Чекбоксы для символов
symbols = {
    "Цифры": tk.BooleanVar(value=True),
    "Буквы": tk.BooleanVar(value=True),
    "Спецсимволы": tk.BooleanVar(value=False)
}

for text, var in symbols.items():
    tk.Checkbutton(root, text=text, variable=var).pack()

# Кнопка генерации
def generate_password():
    # Собрать параметры
    length = length_var.get()
    char_pool = ""
    if symbols["Цифры"].get():
        char_pool += "0123456789"
    if symbols["Буквы"].get():
        char_pool += "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if symbols["Спецсимволы"].get():
        char_pool += "!@#$%^&*()[]{}"

    if not char_pool:
        # Предупреждение
        print("Выберите хотя бы один тип символов.")
        return

    password = ''.join(random.choice(char_pool) for _ in range(length))
    # Добавлять в историю и отображать
    print(password)  # или вставлять в таблицу

generate_btn = tk.Button(root, text="Генерировать", command=generate_password)
generate_btn.pack()

# Таблица истории (используем Treeview)
columns = ("Пароль", "Дата и время", "Параметры")
tree = ttk.Treeview(root, columns=columns, show='headings')
for col in columns:
    tree.heading(col, text=col)
tree.pack()

# Загружать/сохранять историю в json
history_file = "history.json"

def load_history():
    if os.path.exists(history_file):
        with open(history_file, 'r') as f:
            return json.load(f)
    return []

def save_history(entry):
    history = load_history()
    history.append(entry)
    with open(history_file, 'w') as f:
        json.dump(history, f, ensure_ascii=False, indent=4)

# Обновление таблицы и вызов функции генерации...
# (Дальше по необходимости)

root.mainloop()
