from http.client import responses
import requests
import json
from tkinter import *
from tkinter import messagebox as mb
from tkinter import ttk

    # Функция exchange
def exchange():
    code = combobox.get()

    if code:
        try:
            response = requests.get('http://open.er-api.com/v6/latest/USD')
            response.raise_for_status()
            data = response.json()
            if code in data['rates']:
                exchange_rate = data['rates'][code]
                mb.showinfo("Курс обмена", f"Курс: {exchange_rate:.2f}{code} за 1 доллар")
            else:
                mb.showerror("Ошибка", f"Валюта {code} не найдена!")
        except Exception as e:
            mb.showerror("Ошибка", f"Произошла ошибка: {e}.")
    else:
        mb.showwarning("Внимание!", "Введите код валюты!")

    # Рисуем главное окно
window = Tk()
window.title("Курсы валют")
window.geometry("360x180")

Label(text="Выберите код валюты").pack(padx=10, pady=10)

cur = ['RUB','EUR','JPY','CNY','CHF','UZS','CAD','AED','KZT']
combobox = ttk.Combobox(value=cur)
combobox.pack(padx=10, pady=10)

# entry = Entry()
# entry.pack(padx=10, pady=10)

Button(text="Получить курс обмена к доллару", command=exchange).pack(padx=10, pady=10)

window.mainloop()