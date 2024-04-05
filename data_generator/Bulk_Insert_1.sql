use Policja
GO

BULK INSERT Komisariat
FROM 'C:\Users\pauli\OneDrive\Pulpit\semestr 5\Hurtownie danych\lab2\dane\komisariat.csv'
WITH (
	FIELDTERMINATOR = ',',
	ROWTERMINATOR = '\n',
	FIRSTROW = 2
);

BULK INSERT Policjant
FROM 'C:\Users\pauli\OneDrive\Pulpit\semestr 5\Hurtownie danych\lab2\dane\policjant.csv'
WITH (
	FIELDTERMINATOR = ',',
	ROWTERMINATOR = '\n',
	FIRSTROW = 2
);

BULK INSERT Przestepca
FROM 'C:\Users\pauli\OneDrive\Pulpit\semestr 5\Hurtownie danych\lab2\dane\przestepca.csv'
WITH (
	FIELDTERMINATOR = ',',
	ROWTERMINATOR = '\n',
	FIRSTROW = 2
);

BULK INSERT Interwencja
FROM 'C:\Users\pauli\OneDrive\Pulpit\semestr 5\Hurtownie danych\lab2\dane\interwencja.csv'
WITH (
	FIELDTERMINATOR = ',',
	ROWTERMINATOR = '\n',
	FIRSTROW = 2
);

BULK INSERT Wyposazenie
FROM 'C:\Users\pauli\OneDrive\Pulpit\semestr 5\Hurtownie danych\lab2\dane\wyposazenie.csv'
WITH (
	FIELDTERMINATOR = ',',
	ROWTERMINATOR = '\n',
	FIRSTROW = 2
);

BULK INSERT Wyposazenie_podczas_interwencji
FROM 'C:\Users\pauli\OneDrive\Pulpit\semestr 5\Hurtownie danych\lab2\dane\wyposazenie_podczas_interwencji.csv'
WITH (
	FIELDTERMINATOR = ',',
	ROWTERMINATOR = '\n',
	FIRSTROW = 2
);

BULK INSERT Przestepca_powoduje_interwencje
FROM 'C:\Users\pauli\OneDrive\Pulpit\semestr 5\Hurtownie danych\lab2\dane\przestepca_powoduje_interwencje.csv'
WITH (
	FIELDTERMINATOR = ',',
	ROWTERMINATOR = '\n',
	FIRSTROW = 2
);

BULK INSERT Policjant_na_interwencji
FROM 'C:\Users\pauli\OneDrive\Pulpit\semestr 5\Hurtownie danych\lab2\dane\policjant_na_interwencji.csv'
WITH (
	FIELDTERMINATOR = ',',
	ROWTERMINATOR = '\n',
	FIRSTROW = 2
);