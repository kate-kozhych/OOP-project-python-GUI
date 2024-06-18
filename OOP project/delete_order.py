import tkinter as tk
from tkinter import messagebox

from style import font_title, numb, my_font
from sql import remove_pr, get_status_by_id

def delete_stat():
    second_window = tk.Tk()
    #tk.Toplevel(root)

    def on_closing(): # Funkcja on_closing() wywoływana przy próbie zamknięcia okna.
        if tk.messagebox.askokcancel("Quit", "Do you want to quit?"):
            second_window.quit()
    
    def get_id_delete():  #Funkcja get_id_delete() pobiera ID projektu, który ma zostać usunięty z bazy danych.
        id_got=number_s.get()
        if id_got.isdigit():
            result = get_status_by_id(id_got)
            remove_pr(id_got)
            if str(result) == ("[]"): # Jeśli nie znaleziono projektu, wyświetla komunikat
                result_e.delete(0, tk.END)
                result_e.insert(0, "No project under id")
            else:  # Jeśli znaleziono projekt, wyświetla komunikat potwierdzający usunięcie.
                result_e.delete(0, tk.END)
                result_e.insert(0, f"Project {id_got} was removed") 
        else:
            result_e.delete(0, tk.END)
            result_e.insert(0, "Please enter number")
    

    second_window.title("Delete")
    second_window.configure(bg="#5F9EA0")
    second_window.geometry("800x600")
    second_window.resizable(width=False, height=False)
    label_w=tk.Label(second_window, text="Enter the id of the project to remove it brom database", font=numb, bg="#5F9EA0")
    label_w.grid(row=0, column=1, columnspan=3, pady=(70, 70))
    number_s = tk.Entry(second_window, width=20,  font=my_font, bg="#FFFFFF")
    number_s.grid(row=3, column=1, columnspan=3)

    button_enter=tk.Button(second_window, text="Delete", font=my_font, padx=5, bg="#FFFFFF", command=get_id_delete)
    button_enter.grid(row=3, column=3)

    result_e = tk.Entry(second_window, width=20, text="hi", font=my_font, bg="#FFFFFF")
    result_e.grid(row=4, column=1, columnspan=3)

    second_window.protocol("WM_DELETE_WINDOW", on_closing) # Ustawienie reakcji na próbę zamknięcia okna.


    second_window.grid_columnconfigure(0, weight=1)
    second_window.grid_columnconfigure(4, weight=1)

