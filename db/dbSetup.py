from datetime import date, datetime
from xmlrpc.client import DateTime
from sqlalchemy import INTEGER, ForeignKey, create_engine, Column, String, Boolean, Integer, Date, DateTime, orm, Index
import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.automap import automap_base

# settings for connection
dialect = "mariadb"
driver = "mariadbconnector"
username = "root"
password = "maciej"
host = "127.0.0.1"
port = "3306"
uri = f"{dialect}+{driver}://{username}:{password}@{host}:{port}/Library"

engine = create_engine(uri, echo = True)
# conn = engine.connect()

############################## CREATING MODELS ##############################

Base = automap_base()

class AutorModel(Base):
    __tablename__ = 'Autorzy'
    Id_autora = Column(Integer, primary_key=True, autoincrement = True)
    Imie = Column(String(length=20), nullable=False)
    Nazwisko = Column(String(length=20), nullable=False)
    class Config:
        orm_mode = True

Index('Idx_Imie_Nazwisko', AutorModel.Imie, AutorModel.Nazwisko)

class KsiazkaModel(Base):
    __tablename__ = 'Ksiazki'
    Id_ksiazki = Column(Integer, primary_key=True, autoincrement = True)
    Tytul = Column(String(length=100), index = True, nullable=False)
    ISBN = Column(String(length=14), index = True)
    Rok_wydania = Column(DateTime)
    class Config:
        orm_mode = True

class KategoriaModel(Base):
    __tablename__ = 'Kategorie'
    Id_kategorii = Column(Integer, primary_key=True, autoincrement = True)
    Nazwa_kategorii = Column(String(length=30), index = True, nullable=False)
    class Config:
        orm_mode = True

# Index('Idx_Nazwa_kategorii', 'Kategorie.Nazwa_Kategorii')

class WydawnictwoModel(Base):
    __tablename__ = 'Wydawnictwa'
    Id_wydawnictwa = Column(Integer, primary_key=True, autoincrement = True)
    Nazwa_wydawnictwa = Column(String(length=45), index = True, nullable=False)
    class Config:
        orm_mode = True

class EgzemplarzModel(Base):
    __tablename__ = 'Egzemplarze'
    Id_egzemplarza = Column(Integer, primary_key=True, autoincrement = True)
    Id_ksiazki = Column(Integer, ForeignKey('Ksiazki.Id_ksiazki'), index = True, nullable=False)
    Id_wydawnictwa = Column(Integer, ForeignKey('Wydawnictwa.Id_wydawnictwa'), index = True, nullable=False)
    Dostepny = Column(Integer, index = True)
    class Config:
        orm_mode = True

class AdresModel(Base):
    __tablename__ = 'Adresy'
    id_adresu = Column(Integer, primary_key=True, autoincrement = True)
    Miasto = Column(String(length=20), nullable=False)
    Kod_pocztowy = Column(String(length=7), nullable=False)
    Ulica = Column(String(length=30), nullable=False)
    Numer = Column(Integer(), nullable=False)
    class Config:
        orm_mode = True

class OsobaModel(Base):
    __tablename__ = 'Osoby'
    Id_osoby = Column(Integer, primary_key=True, autoincrement = True)
    Imie = Column(String(length=20), nullable=False)
    Nazwisko = Column(String(length=20), nullable=False)
    Id_adresu = Column(Integer, ForeignKey('Adresy.id_adresu'), index = True, nullable=False)
    Telefon = Column(String(length=10), nullable=False)
    Email = Column(String(length=45))
    class Config:
        orm_mode = True

Index('Idx_Imie_Nazwisko', OsobaModel.Imie, OsobaModel.Nazwisko)

class CzytelnikModel(Base):
    __tablename__ = 'Czytelnicy'
    Id_karty = Column(Integer, primary_key=True, autoincrement = True)
    Id_osoby = Column(Integer, ForeignKey('Osoby.Id_osoby'), index = True, nullable=False)
    class Config:
        orm_mode = True

class BibliotekarzModel(Base):
    __tablename__ = 'Bibliotekarze'
    Id_bibliotekarza = Column(Integer, primary_key=True, autoincrement = True)
    Id_osoby = Column(Integer, ForeignKey('Osoby.Id_osoby'), index = True, nullable=False)
    Login = Column(String(length=20), unique = True, nullable=False)
    Haslo = Column(String(length=7), nullable=False)
    class Config:
        orm_mode = True

class WypozyczenieModel(Base):
    __tablename__ = 'Wypozyczenia'
    Id_wypozyczenia = Column(Integer, primary_key=True, autoincrement = True)
    Id_karty = Column(Integer, ForeignKey('Czytelnicy.Id_karty'), index = True, nullable=False)
    Id_bibliotekarza = Column(Integer, ForeignKey('Bibliotekarze.Id_bibliotekarza'), index = True, nullable=False)
    Id_egzemplarza = Column(Integer, ForeignKey('Egzemplarze.Id_egzemplarza'), index = True, nullable=False)
    Data_wypozyczenia = Column(Date, nullable=False)
    Termin_oddania = Column(Date)
    class Config:
        orm_mode = True

class RezerwacjaModel(Base):
    __tablename__ = 'Rezerwacje'
    Id_rezerwacji = Column(Integer, primary_key=True)
    Id_ksiazki = Column(Integer, ForeignKey('Ksiazki.Id_ksiazki'), index = True, nullable=False)
    Id_karty = Column(Integer, ForeignKey('Czytelnicy.Id_karty'), index = True, nullable=False)
    Numer_w_kolejce = Column(Integer, nullable=False)
    Data_rezerwacji = Column(Date)
    class Config:
        orm_mode = True

class KsiazkaHasAutorModel(Base):
    __tablename__ = 'Ksiazki_has_Autorzy'
    Id_ksiazki = Column(Integer, ForeignKey('Ksiazki.Id_ksiazki'), primary_key=True, index = True)
    Id_autora = Column(Integer, ForeignKey('Autorzy.Id_autora'), primary_key=True, index = True)
    class Config:
        orm_mode = True

class KsiazkaHasKategoriaModel(Base):
    __tablename__ = 'Ksiazki_has_Kategorie'
    Id_ksiazki = Column(Integer, ForeignKey('Ksiazki.Id_ksiazki'), primary_key=True, index = True)
    Id_kategorii = Column(Integer, ForeignKey('Kategorie.Id_kategorii'), primary_key=True, index = True)
    class Config:
        orm_mode = True

class WyszukajModel(Base):
    __tablename__ = 'Wyszukaj'
    Tytul = Column(Integer)
    Rok_wydania = Column(Integer)
    Dostepny = Column(Integer)
    Imie = Column(Integer)
    Nazwisko = Column(Integer)
    class Config:
        orm_mode = True

class ZarezerwowaneModel(Base):
    __tablename__ = 'Zarezerwowane'
    Tytul = Column(Integer)
    Numer_w_kolejce = Column(Integer)
    Id_karty = Column(Integer)
    Imie = Column(Integer)
    Nazwisko = Column(Integer)
    Email = Column(Integer)
    class Config:
        orm_mode = True

class WypozyczoneModel(Base):
    __tablename__ = 'Wypozyczone'
    Tytul = Column(Integer)
    Id_egzemplarza = Column(Integer)
    Data_wypozyczenia = Column(Integer)
    Termin_oddania = Column(Integer)
    Id_bibliotekarza = Column(Integer)
    Id_karty = Column(Integer)
    Imie = Column(Integer)
    Nazwisko = Column(Integer)
    Telefon = Column(Integer)
    class Config:
        orm_mode = True

















############################## END OF CREATING MODELS ##############################

Base.metadata.create_all(engine)

# Create a session
Session = orm.sessionmaker()
Session.configure(bind=engine)
session = Session()

# q = session.query(AdresModel).all()
# print(q[0].Ulica)

