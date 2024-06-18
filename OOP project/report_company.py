import tkinter as tk
from tkinter import messagebox
from style import font_title, numb, my_font
from sql import get_info_by_name

def report():

    # Funkcja obsługująca zamykanie okna
    def on_closing():
        if tk.messagebox.askokcancel("Quit", "Do you want to quit?"):
            second_window.quit()
   
    
    def get_name(): # Funkcja pobierająca dane o firmie na podstawie jej nazwy
        name = number_s.get()
        result = get_info_by_name(name)
        if str(result) == "[]":
            text = "No company under this name"
            listbox.delete(0, tk.END)
            listbox.insert(tk.END, text)
        else:
            header = "ID: Price: Manager:    Description:            Status:  "
            listbox.delete(0, tk.END)
            listbox.insert(tk.END, header)
            listbox.insert(tk.END, "")
            for row in result:
                listbox.insert(tk.END, row)

    # Utworzenie nowego okna
    second_window = tk.Tk()
    second_window.title("Report")
    second_window.configure(bg="#5F9EA0")
    second_window.geometry("800x600")
    second_window.resizable(width=False, height=False)

    # Etykieta informująca o wprowadzeniu nazwy firmy
    label_w = tk.Label(second_window, text="Enter the name of the company to create report:", font=numb, bg="#5F9EA0")
    label_w.grid(row=0, column=1, columnspan=3, pady=(70, 70))
    
    # Pole do wprowadzenia nazwy firmy
    number_s = tk.Entry(second_window, width=20,  font=my_font, bg="#FFFFFF")
    number_s.grid(row=3, column=1, columnspan=3)
    
    # Przycisk wyszukiwania
    button_enter = tk.Button(second_window, text="Search", font=my_font, padx=5, bg="#FFFFFF", command=get_name)
    button_enter.grid(row=3, column=3)

    # Listbox do wyświetlania wyników
    listbox = tk.Listbox(second_window, width=70, height=10, font=my_font)
    listbox.grid(row=4, column=1, columnspan=3, pady=(20, 70))

    # Tworzenie Scrollbara
    vertical_scrollbar = tk.Scrollbar(second_window, orient='vertical')
    listbox.config(yscrollcommand=vertical_scrollbar.set)
    vertical_scrollbar.config(command=listbox.yview)
    vertical_scrollbar.grid(row=4, column=4, sticky='ns')

    # Obsługa zamykania okna
    second_window.protocol("WM_DELETE_WINDOW", on_closing)

    second_window.grid_columnconfigure(0, weight=1)
    second_window.grid_columnconfigure(4, weight=1)


