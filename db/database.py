from datetime import date, datetime
from xmlrpc.client import DateTime
from sqlalchemy import INTEGER, ForeignKey, create_engine, Column, String, Boolean, Integer, Date, DateTime, orm, Index, text
import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session

Base = automap_base()

class Database():
    def __init__(self):
        self.Base = Base
        self.dialect = "mariadb"
        self.driver = "mariadbconnector"
        self.host = "127.0.0.1"
        self.port = "3306"
        self.username = None
        self.password = None
        self.engine = None
        self.session = None
        self.conn = None
        self.Adresy = None
        self.Autorzy = None
        self.Bibliotekarze = None
        self.Osoby = None
        self.Czytelnicy = None
        self.Egzemplarze = None
        self.Ksiazki = None
        self.Wydawnictwa = None
        self.Kategorie = None
        self.Rezerwacje = None
        self.Wypozyczenia = None

    def connect(self, username, password):
        uri = f"{self.dialect}+{self.driver}://{username}:{password}@{self.host}:{self.port}/Lib"
        self.engine = create_engine(uri, echo = True)
        self.Base.prepare(self.engine, reflect=True)
        Session = orm.sessionmaker(bind=self.engine)
        self.session = Session()
        self.conn = self.engine.connect()

    def get_tables(self):
        self.Adresy = self.Base.classes.Adresy
        self.Autorzy = self.Base.classes.Autorzy
        self.Bibliotekarze = self.Base.classes.Bibliotekarze
        self.Osoby = self.Base.classes.Osoby
        self.Czytelnicy = self.Base.classes.Czytelnicy
        self.Egzemplarze = self.Base.classes.Egzemplarze
        self.Ksiazki = self.Base.classes.Ksiazki
        self.Wydawnictwa = self.Base.classes.Wydawnictwa
        self.Kategorie = self.Base.classes.Kategorie
        self.Rezerwacje = self.Base.classes.Rezerwacje
        self.Wypozyczenia = self.Base.classes.Wypozyczenia

    def print_tables(self):
        for table in self.Base.classes:
            print(table)

    def deleteAllFromTable(self, table):
        print(table)
        self.db.session.execute(text(f"DELETE FROM {table};"))
        self.db.session.commit()

    def resetIndexInTable(self, table):
        print(table)
        self.db.session.execute(text(f"ALTER TABLE {table} auto_increment=1;"))
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
        instr = text(f"CALL UsunWypozyczenie ('{Wypozyczenie}') ;")
        self.db.session.execute(instr)
        self.db.session.commit()
    
    def UsunRezerwacje(self, Rezerwacja):
        instr = text(f"CALL UsunRezerwacje ('{Rezerwacja}') ;")
        self.db.session.execute(instr)
        self.db.session.commit()

    def DodawanieWypozyczenia(self, Karta, Egzemplarz, Bibliotekarz):
        instr = text(f"CALL DodawanieWypozyczenia ('{Karta}', '{Egzemplarz}', '{Bibliotekarz}') ;")
        self.db.session.execute(instr)
        self.db.session.commit()

    def DodawanieRezerwacji(self, Karta, Tytul):
        instr = text(f"CALL DodawanieRezerwacji ('{Karta}', '{Tytul}') ;")
        self.db.session.execute(instr)
        self.db.session.commit()

    def DodawanieKsiazki(self, Imie, Nazwisko, Nazwa, Numer, Rok, Kategoria, Wydawnictwo):
        instr = text(f"""CALL DodawanieKsiazki ('{Imie}', '{Nazwisko}', '{Nazwa}', '{Numer}', '{Rok}', 
        {Kategoria}, '{Wydawnictwo}') ;""")
        self.db.session.execute(instr)
        self.db.session.commit()

    def DodawanieCzytelnika(self, Imie, Nazwisko, Miasto, Kod, Ulica, Numer, Telefon, Email):
        instr = text(f"""CALL DodawanieCzytelnika ('{Imie}', '{Nazwisko}', '{Miasto}', '{Kod}', '{Ulica}', 
        {Numer}, '{Telefon}', '{Email}') ;""")
        self.db.session.execute(instr)
        self.db.session.commit()

    def DodawanieBibliotekarza(self, Imie, Nazwisko, Miasto, Kod, Ulica, Numer, Telefon, Email, Login, Haslo):
        instr = text(f"""CALL DodawanieBibliotekarza ('{Imie}', '{Nazwisko}', '{Miasto}', '{Kod}', '{Ulica}', 
        {Numer}, '{Telefon}', '{Email}', '{Login}', '{Haslo}') ;""")
        self.db.session.execute(instr)
        self.db.session.commit()

##################################################################################################################################

    def Add_adres():
        pass

    def Add_autor():
        pass




if __name__ == "__main__":
    db = Database("root", "maciej")
    db.connect()
    db.get_tables()
    db.print_tables()
