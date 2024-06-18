import tkinter as tk
from tkinter import messagebox

from style import font_title, numb, my_font
from delete_order import delete_stat
from add_project import add_new



def choose_order(root):
    def delete(): # Funkcja przechodzenia do usuwania zamówienia
        second_window.withdraw()
        delete_stat()

    def add():  # Funkcja przechodzenia do dodawania nowego zamówienia
        second_window.withdraw()
        add_new()

    def on_closing(): # Funkcja obsługi zamknięcia okna
        if tk.messagebox.askokcancel("Quit", "Do you want to quit?"):
            second_window.quit()

    def back(): # Funkcja powrotu do głównego okna
        second_window.withdraw()
        root.deiconify()
   

    second_window = tk.Tk() # Inicjalizacja drugiego okna
    second_window.title("Choose order")
    second_window.configure(bg="#5F9EA0")
    second_window.geometry("800x600")
    second_window.resizable(width=False, height=False)
    label_chs=tk.Label(second_window, text="Choose your option", font=font_title, bg="#5F9EA0")
    label_chs.grid(row=0, column=1, columnspan=3, pady=(70, 70))


    l=tk.Label(second_window, text ="                                   ", bg="#5F9EA0").grid(row=2, column=1 )
    button_check=tk.Button(second_window, text="Add new order", font=my_font, padx=55, bg="#B0E0E6", command=add)
    button_check.grid(row=3, column=1, columnspan=3)


    l=tk.Label(second_window, text ="                                   ", bg="#5F9EA0").grid(row=4, column=1 )
    button_add=tk.Button(second_window, text="Delete order", font=my_font, padx=65, bg="#FFFFFF", command=delete)
    button_add.grid(row=5, column=1, columnspan=3)

    second_window.protocol("WM_DELETE_WINDOW", on_closing)  # Ustawienie reakcji na zamknięcie okna

    pasek_menu = tk.Menu(second_window)
    second_window.config(menu=pasek_menu)
    # Dodawanie opcji do menu
    menu_plik = tk.Menu(pasek_menu, tearoff=0)
    pasek_menu.add_cascade(label="Comand", menu=menu_plik)
    menu_plik.add_command(label="Go Back", command=back)

    second_window.grid_columnconfigure(0, weight=1)
    second_window.grid_columnconfigure(4, weight=1)
