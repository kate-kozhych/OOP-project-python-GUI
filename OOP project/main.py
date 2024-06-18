# Autor: Katsiaryna Kozhych
# Nazwa przedmiotu: Paradygmat programowania obiektowego
# Numer grupy: 3
# Czas zajęć: wtorek godz. 10:00


from style import my_font, font_title  # Importowanie modułów i funkcji
from choose_status import choose_status
from choose_order import choose_order
from create_report import create_report
from delete_order import delete_stat
from check import check_status
from edit_status import edit_status
from add_project import add_new
from report_company import report
from statistica import stat

# Importowanie modułu tkinter i messagebox
import tkinter as tk
from tkinter import messagebox

# Funkcje przypisane do przycisków
def status():
    root.withdraw()
    choose_status(root)

def ordrer():
    root.withdraw()
    choose_order(root)

def report_m():
    root.withdraw()
    create_report(root)

def zamknij_aplikacje():
    root.destroy()

def del_proj():
    root.withdraw()
    delete_stat()

def check():
    root.withdraw()
    check_status()

def edit():
    root.withdraw()
    edit_status()

def add():
    root.withdraw()
    add_new()

def report_c():
    root.withdraw()
    report()

def stats():
    root.withdraw()
    stat()

def on_closing():  # Funkcja obsługująca zamykanie okna
    if tk.messagebox.askokcancel("Quit", "Do you want to quit?"):
        root.quit()



root=tk.Tk() # Utworzenie głównego okna tkinter
root.configure(bg="#5F9EA0")
root.geometry("800x600")
root.resizable(width=False, height=False)
root.title("KPMG")


label_welcome=tk.Label(root, text="Welcome Back!", font=font_title, bg="#5F9EA0") # Ustawienie etykiety powitalnej
label_welcome.grid(row=0, column=1, columnspan=3, pady=(70, 70))


l=tk.Label(root, text ="                                   ", bg="#5F9EA0").grid(row=2, column=1 )
button_check=tk.Button(root, text="Status", font=my_font, padx=72, bg="#B0E0E6", command=status) # Utworzenie przycisków
button_check.grid(row=3, column=1, columnspan=3)


l=tk.Label(root, text ="                                   ", bg="#5F9EA0").grid(row=4, column=1 )
button_add=tk.Button(root, text="Order administration", font=my_font, padx=10, bg="#FFFFFF", command=ordrer)
button_add.grid(row=5, column=1, columnspan=3)

l=tk.Label(root, text ="                                   ", bg="#5F9EA0").grid(row=6, column=1 )
button_search=tk.Button(root, text="Report", font=my_font, padx=67, bg="#FFFFFF", command=report_m)
button_search.grid(row=7, column=1, columnspan=3)


pasek_menu = tk.Menu(root) # Tworzenie paska menu
root.config(menu=pasek_menu)
# Dodawanie opcji do menu
menu_plik = tk.Menu(pasek_menu, tearoff=0)
pasek_menu.add_cascade(label="Comand", menu=menu_plik)
menu_plik.add_command(label="Check Status", command=check)
menu_plik.add_command(label="Edit Status", command=edit)
menu_plik.add_command(label="Add New Project", command=add)
menu_plik.add_command(label="Delete Project", command=del_proj)
menu_plik.add_command(label="Create Report", command=report_c)
menu_plik.add_command(label="See Statistics", command=stats)
menu_plik.add_separator()
menu_plik.add_command(label="Close", command=zamknij_aplikacje)

root.protocol("WM_DELETE_WINDOW", on_closing) # Zamykanie okna po kliknięciu krzyżyka


root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(4, weight=1)

root.mainloop()