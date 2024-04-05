use Policja
GO

BULK INSERT Komisariat
FROM 'C:\Users\pauli\OneDrive\Pulpit\semestr 5\Hurtownie danych\lab2\dane\komisariat2.csv'
WITH (
	FIELDTERMINATOR = ',',
	ROWTERMINATOR = '\n',
	FIRSTROW = 2
);

BULK INSERT Policjant
FROM 'C:\Users\pauli\OneDrive\Pulpit\semestr 5\Hurtownie danych\lab2\dane\policjant2.csv'
WITH (
	FIELDTERMINATOR = ',',
	ROWTERMINATOR = '\n',
	FIRSTROW = 2
);

BULK INSERT Przestepca
FROM 'C:\Users\pauli\OneDrive\Pulpit\semestr 5\Hurtownie danych\lab2\dane\przestepca2.csv'
WITH (
	FIELDTERMINATOR = ',',
	ROWTERMINATOR = '\n',
	FIRSTROW = 2
);

BULK INSERT Interwencja
FROM 'C:\Users\pauli\OneDrive\Pulpit\semestr 5\Hurtownie danych\lab2\dane\interwencja2.csv'
WITH (
	FIELDTERMINATOR = ',',
	ROWTERMINATOR = '\n',
	FIRSTROW = 2
);

BULK INSERT Wyposazenie
FROM 'C:\Users\pauli\OneDrive\Pulpit\semestr 5\Hurtownie danych\lab2\dane\wyposazenie2.csv'
WITH (
	FIELDTERMINATOR = ',',
	ROWTERMINATOR = '\n',
	FIRSTROW = 2
);

BULK INSERT Wyposazenie_podczas_interwencji
FROM 'C:\Users\pauli\OneDrive\Pulpit\semestr 5\Hurtownie danych\lab2\dane\wyposazenie_podczas_interwencji2.csv'
WITH (
	FIELDTERMINATOR = ',',
	ROWTERMINATOR = '\n',
	FIRSTROW = 2
);

BULK INSERT Przestepca_powoduje_interwencje
FROM 'C:\Users\pauli\OneDrive\Pulpit\semestr 5\Hurtownie danych\lab2\dane\przestepca_powoduje_interwencje2.csv'
WITH (
	FIELDTERMINATOR = ',',
	ROWTERMINATOR = '\n',
	FIRSTROW = 2
);

BULK INSERT Policjant_na_interwencji
FROM 'C:\Users\pauli\OneDrive\Pulpit\semestr 5\Hurtownie danych\lab2\dane\policjant_na_interwencji2.csv'
WITH (
	FIELDTERMINATOR = ',',
	ROWTERMINATOR = '\n',
	FIRSTROW = 2
);