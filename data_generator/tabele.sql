create table Komisariat (
	ID INT PRIMARY KEY,
	Nazwa VARCHAR(30),
	Adres VARCHAR(100),
	Zatrudnieni_funkcjonariusze INT
);

create table Policjant (
	Pesel VARCHAR(11) PRIMARY KEY,
	Imie VARCHAR(30),
	Nazwisko VARCHAR(30),
	Plec VARCHAR(10),
	Stanowisko VARCHAR(30),
	Adres VARCHAR(200),
	Data_zatrudnienia Date,
	Komisariat INT REFERENCES Komisariat
);

create table Przestepca (
	Pesel VARCHAR(11) PRIMARY KEY,
	Imie VARCHAR(30),
	Nazwisko VARCHAR(30),
	Plec VARCHAR(10),
	Adres VARCHAR(30),
	Czy_zatrzymany BOOLEAN
);

create table Interwencja(
	ID INT PRIMARY KEY,
	Data_interwencji Date,
	Lokalizacja VARCHAR(100),
	Opis_zdarzenia VARCHAR(500),
	Rodzaj VARCHAR(40),
	Status VARCHAR(20),
	Powodzenie BOOLEAN
);

create table Wyposazenie(
	ID INT PRIMARY KEY,
	Nazwa VARCHAR(60),
	Numer_seryjny VARCHAR(20),
	Rodzaj VARCHAR(40)
);

create table Wyposazenie_podczas_interwencji(
	ID_interwencji INT REFERENCES Interwencja,
	ID_wyposazenia INT REFERENCES Wyposazenie,
	PRIMARY KEY (ID_interwencji, ID_wyposazenia)
);

create table Przestepca_powoduje_interwencje (
	ID_interwencji INT REFERENCES Interwencja,
	Pesel_przestepcy VARCHAR(11)REFERENCES Przestepca, 
	PRIMARY KEY (Pesel_przestepcy, ID_interwencji)
);

create table Policjant_na_interwencji (
	ID_interwencji INT REFERENCES Interwencja,
	Pesel_policjanta VARCHAR(11)REFERENCES Policjant, 
	PRIMARY KEY (Pesel_policjanta, ID_interwencji)
);