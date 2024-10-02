import requests
import json
from tkinter import *
from tkinter import messagebox as mb
from tkinter import ttk

# Функция для обновления метки с названием валюты
def update_c_label(event):
    code = t_combobox.get()
    name = cur.get(code)
    c_label.config(text=name)

    # Функция exchange
def exchange():
    t_code = t_combobox.get()
    b_code = b_combobox.get()
    if t_code and b_code:
        try:
            response = requests.get(f'http://open.er-api.com/v6/latest/{b_code}')
            response.raise_for_status()
            data = response.json()
            if t_code in data['rates']:
                exchange_rate = data['rates'][t_code]
                t_name = cur[t_code]
                b_name = cur[b_code]
                mb.showinfo("Курс обмена", f"Курс: {exchange_rate:.2f} {t_name} за 1 {b_name}")
            else:
                mb.showerror("Ошибка", f"Валюта {t_code} не найдена!")
        except Exception as e:
                mb.showerror("Ошибка", f"Произошла ошибка: {e}.")
    else:
            mb.showwarning("Внимание!", "Введите код валюты!")

    # Словарь с кодами валют
cur = {
    'USD': 'Американский доллар',
    'RUB': 'Российский рубль',
    'EUR': 'Евро',
    'JPY': 'Японская йена',
    'CNY': 'Китайский юань',
    'CHF': 'Швейцарский франк',
    'UZS': 'Узбекский сум',
    'CAD': 'Канадский доллар',
    'AED': 'Дирхам ОАЭ',
    'KZT': 'Казахский тенге'
 }

    # Рисуем главное окно
window = Tk()
window.title("Курсы валют")
window.geometry("360x300")

    # список базовой валюты
Label(text="Базовая валюта").pack(padx=10, pady=10)
b_combobox = ttk.Combobox(value=list(cur.keys()))
b_combobox.pack(padx=10, pady=10)


    # Список целевой валюты
Label(text="Целевая валюта").pack(padx=10, pady=10)
t_combobox = ttk.Combobox(value=list(cur.keys()))
t_combobox.pack(padx=10, pady=10)
t_combobox.bind("<<ComboboxSelected>>", update_c_label)

c_label = ttk.Label()
c_label.pack(padx=10, pady=10)

Button(text="Получить курс обмена к доллару", command=exchange).pack(padx=10, pady=10)

window.mainloop()
