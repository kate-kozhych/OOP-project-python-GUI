import sqlite3
from classP import Project

conn = sqlite3.connect(':memory:') # Połączenie z bazą danych w pamięci
c = conn.cursor() # Utworzenie tabeli projektów
c.execute("""CREATE TABLE project ( 
            id INTEGER,
            name TEXT,
            price INTEGER,
            manager_first TEXT,
            manager_last TEXT,
            description TEXT,
            status TEXT
            )""")


def insert_pr(pr): # Funkcja dodająca projekt do bazy danych
    with conn:
        c.execute("INSERT INTO project VALUES (:id, :name, :price, :manager_first, :manager_last, :description, :status)",
            {'id': pr.id, 'name': pr.name, 'price': pr.price, 'manager_first': pr.manager_first, 'manager_last': pr.manager_last, 'description': pr.description, 'status': pr.status})

def insert_project(id, name, price, manager_first, manager_last, description, status): # Funkcja dodająca projekt do bazy danych przy użyciu pojedynczych wartości
    with conn:
        c.execute("INSERT INTO project VALUES (:id, :name, :price, :manager_first, :manager_last, :description, :status)",
            {'id': id, 'name': name, 'price': price, 'manager_first': manager_first, 'manager_last': manager_last, 'description': description, 'status': status})


def get_by_id(id): # Funkcja pobierająca projekt po jego identyfikatorze
    c.execute("SELECT * FROM project WHERE id=:id", {'id':id})
    return c.fetchall()

def get_status_by_id(id): # Funkcja pobierająca status projektu po jego identyfikatorze
    c.execute("SELECT status FROM project WHERE id=:id", {'id':id})
    return c.fetchall()

def update_status(id, status): # Funkcja aktualizująca status projektu
    with conn:
        c.execute("""UPDATE project SET status=:status 
                WHERE id = :id""", {'status': status,'id':id})


def remove_pr(id): # Funkcja usuwająca projekt z bazy danych
    with conn:
        c.execute("DELETE FROM project WHERE id = :id", {'id': id})


def count_status(): # Funkcja zliczająca projekty według statusu
    c.execute("SELECT status, COUNT(*) FROM project GROUP BY status")
    return c.fetchall()

def get_info_by_name(name): # Funkcja pobierająca informacje o projekcie po jego nazwie
    c.execute("SELECT id, price, manager_first, manager_last, description, status FROM project WHERE name=:name", {'name':name})
    return c.fetchall()

pr_1=Project(1, 'KPMG', 10000, 'Pawel', 'Prytko', 'Accounting project', 'Finished' ) # Tworzenie instancji projektów
pr_2=Project(2, 'KPMG', 14000, 'Pawel', 'Prytko', 'Accounting project', 'Processing' )
pr_3=Project(3, 'Sii', 15000, 'Anna', 'Folowa', 'IT project', 'In progress' )
pr_4 = Project(4, 'Deloitte', 12000, 'Adam', 'Nowak', 'Financial analysis', 'Accepted')
pr_5 = Project(5, 'PwC', 11000, 'Katarzyna', 'Kowalska', 'Tax advisory', 'Processing')
pr_6 = Project(6, 'Ernst & Young', 13000, 'Michał', 'Wiśniewski', 'Audit project', 'In progress')
pr_7 = Project(7, 'Accenture', 16000, 'Magdalena', 'Kaczmarek', 'Consulting project', 'Processing')
pr_8 = Project(8, 'Capgemini', 14500, 'Karolina', 'Lewandowska', 'Software development', 'In progress')
pr_9 = Project(9, 'Sii', 17000, 'Tomasz', 'Nowicki', 'Big data project', 'Processing')
pr_10 = Project(10, 'Microsoft', 20000, 'Anna', 'Kowalczyk', 'Cloud computing project', 'Accepted')


insert_pr(pr_1) # Dodanie projektów do bazy danych
insert_pr(pr_2)
insert_pr(pr_3)
insert_pr(pr_4)
insert_pr(pr_5)
insert_pr(pr_6)
insert_pr(pr_7)
insert_pr(pr_8)
insert_pr(pr_9)
insert_pr(pr_10)


