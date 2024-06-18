# OOP-project-python-GUI
Program jest przeznaczony dla firmy specjalizującej się w świadczeniu różnorodnych usług biznesowych i IT. To aplikacja graficzna z interfejsem, który umożliwia użytkownikom zarządzanie zamówieniami firmy.
W programie zaimplementowane są następujące funkcje:

  •	Dodawanie nowych zamówień: pracownicy mogą wprowadzać dane dotyczące nowych zamówień, takie jak nazwa zamówienia, koszt, menedżerowie i opis.
  
  •	Usuwanie zamówień: możliwość usuwania zamówień z bazy danych w celu zachowania aktualności informacji.
  
  •	Przeglądanie statusu zamówień: pracownicy mogą przeglądać aktualny status wszystkich zamówień firmy.
  
  •	Zmiana statusu zamówień: funkcja umożliwia użytkownikom zmianę statusu określonego zamówienia, na przykład z "Processing" na "Finished".
  
  •	Tworzenie raportów o zamówieniach: możliwość generowania raportów o zamówieniach, które zapewniają szczegółowe informacje o zamówieniach firmy, na przykład ogólną liczbę zamówień, statusy zamówień itp.

Program współdziała z bazą danych, w której przechowywane są informacje o zamówieniach firmy. Dzięki temu dane o zamówieniach są przechowywane i mogą być łatwo dostępne i aktualizowane za pośrednictwem interfejsu graficznego programu.

Typ licencji programu: licencja własnościowa. Program ten nie może być dystrybuowany bez mojej zgody, ograniczenie ilości kopii oprogramowania, które mogą być zainstalowane na różnych komputerach. Wymagana jest płatna licencja do komercyjnego użytkowania oprogramowania.
Użyte biblioteki: tkinter, sqlite3.
Wersja Python: python3.11 

# Funkcjonalność i interfejs graficzny
Główny plik (main.py) programu zawiera interfejs graficzny
z możliwością wyboru funkcji „Status”, „Order Administration” i „Report”. Interfejs ma górne menu. Każde okno przy próbie zamknięcia wyświetla ostrzeżenie. 

Plik (choose_status.py) otwiera się po wyborze przez użytkownika kategorii “Status”. Okno zawiera górne menu z możliwością powrotu.

Plik (check.py) otwiera się po wyborze przez użytkownika kategorii “Check status”. Okno zawiera sprawdzenie statusu: użytkownik wprowadza identyfikator (ID), a program wyszukuje ten ID w bazie danych (sql.py) i wyświetla status projektu. Program również zawiera sprawdzenie, czy taki projekt istnieje, czy ID jest liczbą.

Plik (edit_status.py) otwiera się po wyborze przez użytkownika kategorii “Edit status”. Okno zawiera funkcję zmiany statusu: użytkownik wprowadza identyfikator (ID), a program wyszukuje ten ID w bazie danych (sql.py) i zmienia status projektu. Program również zawiera sprawdzenie, czy taki projekt istnieje.

Plik (choose_order.py) otwiera się po wyborze przez użytkownika kategorii “Order Administration”. Okno zawiera górne menu z możliwością powrotu.

Plik (add_ptoject.py) otwiera się po wyborze przez użytkownika kategorii “Add new order”. Okno zawiera funkcję dodawania danych o nowym projekcie do bazy danych (sql.py) poprzez tworzenie atrybutu klasy Projekt (classP.py). Program zawiera również sprawdzenie poprawności wprowadzonych danych.

Plik (delete_ptoject.py) otwiera się po wyborze przez użytkownika kategorii “Delete order”. Okno zawiera funkcję usuwania danych o projekcie z bazy danych (sql.py) poprzez wyszukiwanie atrybutu po ID. Program również zawiera sprawdzenie, czy taki projekt istnieje.

Plik (create_report.py) otwiera się po wyborze przez użytkownika kategorii “Report”. Okno zawiera górne menu z możliwością powrotu.

Plik (report_company.py) otwiera się po wyborze przez użytkownika kategorii “Create Report”. Okno wyświetla statystyki dotyczące wybranej firmy z bazy danych (sql.py). Program również zawiera sprawdzenie, czy taka firma istnieje w bazie danych; scrollbar.
Plik (statistica.py) otwiera się po wyborze przez użytkownika kategorii “See statistics Okno liczy ilość projektów (sql.py) w każdym statusie i wyświetla je na ekranie.



















