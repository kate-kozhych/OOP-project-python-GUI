import tkinter as tk
from tkinter import messagebox

from style import font_title, numb, my_font
from sql import count_status

def stat():


    def on_closing(): # Funkcja zamknięcia okna
        if tk.messagebox.askokcancel("Quit", "Do you want to quit?"):
            second_window.quit()
   
    def search(): # Funkcja wyszukiwania i wyświetlania statystyk
        result=count_status()
        listbox.delete(0, tk.END)
        for row in result:
            listbox.insert(tk.END, row) # Wstawienie wyników do listy

    second_window = tk.Tk()  # Utworzenie drugiego okna
    second_window.title("Statistics")
    second_window.configure(bg="#5F9EA0")
    second_window.geometry("800x600")
    second_window.resizable(width=False, height=False)
    label_w=tk.Label(second_window, text="Current statistics:", font=numb, bg="#5F9EA0")
    label_w.grid(row=0, column=1, columnspan=3, pady=(70, 30))


    button_enter=tk.Button(second_window, text="See", font=my_font, padx=5, bg="#FFFFFF", command=search)
    button_enter.grid(row=1, column=2)

    listbox = tk.Listbox(second_window, width=70, height=10, font=my_font) # Lista do wyświetlania wyników
    listbox.grid(row=4, column=1, columnspan=3, pady=(20, 70))

 
    vertical_scrollbar = tk.Scrollbar(second_window, orient='vertical') # Utworzenie paska przewijania

    listbox.config(yscrollcommand=vertical_scrollbar.set)
    vertical_scrollbar.config(command=listbox.yview)
    vertical_scrollbar.grid(row=4, column=4, sticky='ns')


    second_window.protocol("WM_DELETE_WINDOW", on_closing)


    second_window.grid_columnconfigure(0, weight=1)
    second_window.grid_columnconfigure(4, weight=1)