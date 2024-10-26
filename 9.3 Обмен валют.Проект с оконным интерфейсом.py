from tkinter import *
from tkinter import messagebox as mb
import requests
import json



window = Tk()
window.title("КУрсы обмена валют")
window.geometry("360x180")

Label(text="Введите код валюты").pack(padx=10, pady=10)

entry = Entry()
entry.pack(padx=10, pady=10)

Button(text="Получить курс обмена к доллару", comand=exchange).pack(padx=10, pady=10)


window.mainloop()