
import tkinter as tk
from tkinter import messagebox
from style import numb, my_font
from sql import get_status_by_id

def check_status():
    second_window = tk.Tk()

    def on_closing(): # Funkcja obsługi zamknięcia okna
        if tk.messagebox.askokcancel("Quit", "Do you want to quit?"):
            second_window.quit()

    def get_id():
        id_got=number_s.get() # Pobranie wartości ID z pola wprowadzania tekstu
        if id_got.isdigit():
            result = get_status_by_id(id_got) # Pobranie statusu projektu na podstawie ID
            if str(result) == ("[]"):  # Sprawdzenie, czy brak wyników wyszukiwania
                result_e.delete(0, tk.END)
                result_e.insert(0, "No project under id")
            else:
                text = str(result).strip("''()[]'',") # Przetworzenie wyniku na czytelny tekst
                result_e.delete(0, tk.END)
                result_e.insert(0, f"Status: {text}") 
        else:
            result_e.delete(0, tk.END)
            result_e.insert(0, "Please enter number")
    

    second_window.title("Second Page")
    second_window.configure(bg="#5F9EA0")
    second_window.geometry("800x600")
    second_window.resizable(width=False, height=False)
    label_w=tk.Label(second_window, text="Enter the number of the project to see the current status:", font=numb, bg="#5F9EA0")
    label_w.grid(row=0, column=1, columnspan=3, pady=(70, 70))
    number_s = tk.Entry(second_window, width=20,  font=my_font, bg="#FFFFFF")
    number_s.grid(row=3, column=1, columnspan=3)

    button_enter=tk.Button(second_window, text="Search", font=my_font, padx=5, bg="#FFFFFF", command=get_id)
    button_enter.grid(row=3, column=3)

    result_e = tk.Entry(second_window, width=20, text="hi", font=my_font, bg="#FFFFFF")
    result_e.insert(0, "Status:")
    result_e.grid(row=4, column=1, columnspan=3)

    second_window.protocol("WM_DELETE_WINDOW", on_closing) # Ustawienie reakcji na zamknięcie okna


    second_window.grid_columnconfigure(0, weight=1)
    second_window.grid_columnconfigure(4, weight=1)

