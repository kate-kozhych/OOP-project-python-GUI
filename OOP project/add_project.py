
#ADD
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from style import font_title, numb, my_font
from sql import insert_pr
from classP import Project

def add_new():
    second_window = tk.Tk()
    def on_closing():  # Funkcja obsługi zamknięcia okna
        if tk.messagebox.askokcancel("Quit", "Do you want to quit?"):
            second_window.quit()
    
    
    def add_project():
        id_got=id.get() # Pobranie wartoścej
        name_got=name.get()
        price_got=price.get()
        manf_got=manf.get()
        manl_got=manl.get()
        desc_got=desc.get()
        status_got = combobox.get()

        
        def addnew():
            second_window.withdraw()
            add_new()

        if id_got.isdigit() and price_got.isdigit() and not manf_got.isdigit() and not manl_got.isdigit(): # Sprawdzenie, czy wprowadzone wartości są poprawne
            project=Project(id_got, name_got, price_got, manf_got, manl_got, desc_got, status_got) #Instancja
            insert_pr(project) # Dodanie projektu do bazy danych
            label_w.config(text="The project as successfully added to the db")
            button_enter.config(text="Add again", command=addnew) # Zmiana tekstu przycisku i jego działania
        else:
            label_w.config(text="There are mistakes in lines. Try again!")

            id.delete(0, tk.END)
            id.insert(0, "ID:")
            id.bind("<FocusIn>", clear_id)  # Przypisanie funkcji do zdarzenia kliknięcia


            name.delete(0, tk.END)
            name.insert(0, "Name:")
            name.bind("<FocusIn>", clear_name)  
            price.delete(0, tk.END)
            price.insert(0, "Price:")
            price.bind("<FocusIn>", clear_price) 

            manf.delete(0, tk.END)
            manf.insert(0, "Managers first name:")
            manf.bind("<FocusIn>", clear_manf) 

            manl.delete(0, tk.END)
            manl.insert(0, "Managers last name:")
            manl.bind("<FocusIn>", clear_manl)  

            desc.delete(0, tk.END)
            desc.insert(0, "Description:")
            desc.bind("<FocusIn>", clear_desc)  
            


    
    def clear_id(event):
        id.delete(0, tk.END)

    def clear_name(event):
        name.delete(0, tk.END)

    def clear_price(event):
        price.delete(0, tk.END)
    
    def clear_manf(event):
        manf.delete(0, tk.END)

    def clear_manl(event):
        manl.delete(0, tk.END)

    def clear_desc(event):
        desc.delete(0, tk.END)


    second_window.title("Add")
    second_window.configure(bg="#5F9EA0")
    second_window.geometry("800x600")
    second_window.resizable(width=False, height=False)
    label_w=tk.Label(second_window, text="Enter the information about the project:", font=numb, bg="#5F9EA0")
    label_w.grid(row=0, column=1, columnspan=3, pady=(70, 70))

    id = tk.Entry(second_window, width=20,  font=my_font, bg="#FFFFFF")
    id.insert(0, "ID:")
    id.bind("<FocusIn>", clear_id)  # Przypisanie funkcji do zdarzenia kliknięcia
    id.grid(row=3, column=1, columnspan=3)

    button_enter=tk.Button(second_window, text="Add", font=my_font, padx=5, bg="#FFFFFF", command=add_project)
    button_enter.grid(row=3, column=3)

    l=tk.Label(second_window, text ="                                   ", bg="#5F9EA0").grid(row=4, column=1 )


    name = tk.Entry(second_window, width=20, font=my_font, bg="#FFFFFF")
    name.insert(0, "Name:")
    name.bind("<FocusIn>", clear_name)  # Przypisanie funkcji do zdarzenia kliknięcia
    name.grid(row=5, column=1, columnspan=3)

    l=tk.Label(second_window, text ="                                   ", bg="#5F9EA0").grid(row=6, column=1 )


    price = tk.Entry(second_window, width=20, font=my_font, bg="#FFFFFF")
    price.insert(0, "Price:")
    price.bind("<FocusIn>", clear_price)  # Przypisanie funkcji do zdarzenia kliknięcia
    price.grid(row=7, column=1, columnspan=3)

    l=tk.Label(second_window, text ="                                   ", bg="#5F9EA0").grid(row=8, column=1 )
     
    manf = tk.Entry(second_window, width=20, font=my_font, bg="#FFFFFF")
    manf.insert(0, "Managers first name:")
    manf.bind("<FocusIn>", clear_manf)  # Przypisanie funkcji do zdarzenia kliknięcia
    manf.grid(row=9, column=1, columnspan=3)

    l=tk.Label(second_window, text ="                                   ", bg="#5F9EA0").grid(row=10, column=1 )
     
    manl = tk.Entry(second_window, width=20, font=my_font, bg="#FFFFFF")
    manl.insert(0, "Managers last name:")
    manl.bind("<FocusIn>", clear_manl)  # Przypisanie funkcji do zdarzenia kliknięcia
    manl.grid(row=11, column=1, columnspan=3)

    l=tk.Label(second_window, text ="                                   ", bg="#5F9EA0").grid(row=12, column=1 )
     
    desc = tk.Entry(second_window, width=20, font=my_font, bg="#FFFFFF")
    desc.insert(0, "Description:")
    desc.bind("<FocusIn>", clear_desc)  # Przypisanie funkcji do zdarzenia kliknięcia
    desc.grid(row=13, column=1, columnspan=3)

    l=tk.Label(second_window, text ="                                   ", bg="#5F9EA0").grid(row=14, column=1 )
     

    def on_combobox_select(event):
        selected_item = combobox.get()
        return selected_item
    # Tworzenie głównego okna

    combobox = ttk.Combobox(second_window, values=["Processing", "Accepted", "In progress", "Finished", "Canceled"], font=my_font)
    # Ustawienie początkowej wartości
    combobox.set("Select a status")
    # Przypisanie funkcji do zdarzenia wyboru
    combobox.bind("<<ComboboxSelected>>", on_combobox_select)
    # Umieszczenie Combobox w oknie
    combobox.grid(row=15, column=1, columnspan=3)

    
    second_window.protocol("WM_DELETE_WINDOW", on_closing)



    second_window.grid_columnconfigure(0, weight=1)
    second_window.grid_columnconfigure(4, weight=1)


    