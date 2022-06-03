from database import *
import sqlalchemy as sql

class Instructions():
    def __init__(self):
        self.db = Database()
        self.db.connect("root", "maciej")
        self.db.get_tables()

    def deleteAllFromTable(self, table):
        print(table)
        self.db.session.execute(sql.text(f"DELETE FROM {table};"))
        self.db.session.commit()

    def resetIndexInTable(self, table):
        print(table)
        self.db.session.execute(sql.text(f"ALTER TABLE {table} auto_increment=1;"))
        self.db.session.commit()

    def clearDatabase(self):
        self.deleteAllFromTable('Wypozyczenia')
        self.resetIndexInTable('Wypozyczenia')
        self.deleteAllFromTable('Rezerwacje')
        self.resetIndexInTable('Rezerwacje')
        self.deleteAllFromTable('Bibliotekarze')
        self.resetIndexInTable('Bibliotekarze')
        self.deleteAllFromTable('Czytelnicy')
        self.resetIndexInTable('Czytelnicy')
        self.deleteAllFromTable('Egzemplarze')
        self.resetIndexInTable('Egzemplarze')
        self.deleteAllFromTable('Osoby')
        self.resetIndexInTable('Osoby')
        self.deleteAllFromTable('Wydawnictwa')
        self.resetIndexInTable('Wydawnictwa')
        self.deleteAllFromTable('Ksiazki')
        self.resetIndexInTable('Ksiazki')
        self.deleteAllFromTable('Kategorie')
        self.resetIndexInTable('Kategorie')
        self.deleteAllFromTable('Autorzy')
        self.resetIndexInTable('Autorzy')
        self.deleteAllFromTable('Adresy')
        self.resetIndexInTable('Adresy')


##################################################################################################################################

    def UsunWypozyczenie(self, Wypozyczenie):
        instr = sql.text(f"CALL UsunWypozyczenie ('{Wypozyczenie}') ;")
        self.db.session.execute(instr)
        self.db.session.commit()
    
    def UsunRezerwacje(self, Rezerwacja):
        instr = sql.text(f"CALL UsunRezerwacje ('{Rezerwacja}') ;")
        self.db.session.execute(instr)
        self.db.session.commit()

    def DodawanieWypozyczenia(self, Karta, Egzemplarz, Bibliotekarz):
        instr = sql.text(f"CALL DodawanieWypozyczenia ('{Karta}', '{Egzemplarz}', '{Bibliotekarz}') ;")
        self.db.session.execute(instr)
        self.db.session.commit()

    def DodawanieRezerwacji(self, Karta, Tytul):
        instr = sql.text(f"CALL DodawanieRezerwacji ('{Karta}', '{Tytul}') ;")
        self.db.session.execute(instr)
        self.db.session.commit()

    def DodawanieKsiazki(self, Imie, Nazwisko, Nazwa, Numer, Rok, Kategoria, Wydawnictwo):
        instr = sql.text(f"""CALL DodawanieKsiazki ('{Imie}', '{Nazwisko}', '{Nazwa}', '{Numer}', '{Rok}', 
        {Kategoria}, '{Wydawnictwo}') ;""")
        self.db.session.execute(instr)
        self.db.session.commit()

    def DodawanieCzytelnika(self, Imie, Nazwisko, Miasto, Kod, Ulica, Numer, Telefon, Email):
        instr = sql.text(f"""CALL DodawanieCzytelnika ('{Imie}', '{Nazwisko}', '{Miasto}', '{Kod}', '{Ulica}', 
        {Numer}, '{Telefon}', '{Email}') ;""")
        self.db.session.execute(instr)
        self.db.session.commit()

    def DodawanieBibliotekarza(self, Imie, Nazwisko, Miasto, Kod, Ulica, Numer, Telefon, Email, Login, Haslo):
        instr = sql.text(f"""CALL DodawanieBibliotekarza ('{Imie}', '{Nazwisko}', '{Miasto}', '{Kod}', '{Ulica}', 
        {Numer}, '{Telefon}', '{Email}', '{Login}', '{Haslo}') ;""")
        self.db.session.execute(instr)
        self.db.session.commit()

##################################################################################################################################

    def Add_adres():
        pass

    def Add_autor():
        pass


if __name__ == "__main__":
    instr = Instructions()
    #instr.clearDatabase()
    instr.DodawanieBibliotekarza('Tomasz', 'Marut', 'Wroclaw', '60-610', 'mokra', 
    1, '123456789', 'Maciej@Biblioteka.com', 'maciejbarnax', 'maciejbarnax')

    #text = sql.text("CALL DodawanieBibliotekarza ('Maciej', 'Barna', 'Wroclaw', '62-610', 'mokra', 1, '123456789', 'maciej@lib.com', 'maciejbarna', 'maciejbarna') ;")
    #text = sql.text("SELECT Add_wydawnictwo('A') FROM DUAL;")
    #text = sql.text("SELECT Add_adres('Wroclaw', '60-610', 'mokra', 1)")
    #instr.db.session.execute(text)
    #instr.db.session.commit()

    # # tak działa
    # wyd = instr.db.Base.classes.Wydawnictwa(Nazwa_wydawnictwa="C")
    # instr.db.session.add(wyd)
    # instr.db.session.commit()