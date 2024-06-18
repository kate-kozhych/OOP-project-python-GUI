import tkinter as tk
from tkinter import ttk, messagebox
from style import font_title, numb, my_font
from sql import update_status, get_status_by_id

def edit_status():
    second_window = tk.Tk()

    # Funkcja obsługująca zamykanie okna
    def on_closing():
        if tk.messagebox.askokcancel("Quit", "Do you want to quit?"):
            second_window.quit()

    # Funkcja aktualizująca status projektu
    def update():
        status_n = combobox.get()
        id = number_s.get()
        if id.isdigit():
            result = get_status_by_id(id)
            if str(result) == "[]":
                label_w.config(text="No project under this id")
            else:
                update_status(id, status_n)  # Jeśli wprowadzone dane nie są liczbą, wyświetla komunikat.
                label_w.config(text="The status was successfully updated!")

    second_window.title("Edit")  # Konfiguracja okna.
    second_window.configure(bg="#5F9EA0")
    second_window.geometry("800x600")
    second_window.resizable(width=False, height=False)
    
    # Etykieta informująca o wprowadzeniu ID projektu i wybraniu statusu
    label_w = tk.Label(second_window, text="Enter the ID of the project and select status:", font=my_font, bg="#5F9EA0")
    label_w.grid(row=0, column=1, columnspan=3, pady=(70, 20))

    number_s = tk.Entry(second_window, width=19,  font=my_font, bg="#FFFFFF")
    number_s.grid(row=2, column=1, columnspan=2)

    button_enter = tk.Button(second_window, text="Update", font=my_font, padx=10, bg="#FFFFFF", command=update)
    button_enter.grid(row=2, column=3, pady=(0, 0))

    # Pusta etykieta jako odstęp
    l = tk.Label(second_window, text="                    ", bg="#5F9EA0").grid(row=3, column=0)

    # Funkcja wywoływana po wyborze wartości w comboboxie
    def on_combobox_select(event):
        selected_item = combobox.get()
        return selected_item

    # Tworzenie comboboxa z dostępnymi statusami
    combobox = ttk.Combobox(second_window, values=["Processing", "Accepted", "In progress", "Finished", "Canceled"], font=my_font)
    combobox.set("Select a status")  # Ustawienie początkowej wartości
    combobox.bind("<<ComboboxSelected>>", on_combobox_select)  # Przypisanie funkcji do zdarzenia wyboru
    combobox.grid(row=4, column=2)  # Umieszczenie Combobox w oknie

    second_window.protocol("WM_DELETE_WINDOW", on_closing)

    second_window.grid_columnconfigure(0, weight=1)
    second_window.grid_columnconfigure(4, weight=1)

    second_window.mainloop()

