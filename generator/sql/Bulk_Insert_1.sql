use Policja
GO

BULK INSERT Komisariat
FROM 'C:\Users\pauli\OneDrive\Pulpit\semestr 5\Hurtownie danych\lab2\generated_data\komisariaty.csv'
WITH (
	FIELDTERMINATOR = ',',
	ROWTERMINATOR = '\n',
	FIRSTROW = 2
);

BULK INSERT Policjant
FROM 'C:\Users\pauli\OneDrive\Pulpit\semestr 5\Hurtownie danych\lab2\generated_data\policjanci.csv'
WITH (
	FIELDTERMINATOR = ',',
	ROWTERMINATOR = '\n',
	FIRSTROW = 2
);

BULK INSERT Przestepca
FROM 'C:\Users\pauli\OneDrive\Pulpit\semestr 5\Hurtownie danych\lab2\generated_data\przestepcy.csv'
WITH (
	FIELDTERMINATOR = ',',
	ROWTERMINATOR = '\n',
	FIRSTROW = 2
);

BULK INSERT Interwencja
FROM 'C:\Users\pauli\OneDrive\Pulpit\semestr 5\Hurtownie danych\lab2\generated_data\interwencje.csv'
WITH (
	FIELDTERMINATOR = ',',
	ROWTERMINATOR = '\n',
	FIRSTROW = 2
);

BULK INSERT Wyposazenie
FROM 'C:\Users\pauli\OneDrive\Pulpit\semestr 5\Hurtownie danych\lab2\generated_data\wyposazenie.csv'
WITH (
	FIELDTERMINATOR = ',',
	ROWTERMINATOR = '\n',
	FIRSTROW = 2
);

BULK INSERT Wyposazenie_podczas_interwencji
FROM 'C:\Users\pauli\OneDrive\Pulpit\semestr 5\Hurtownie danych\lab2\generated_data\wyposazenie_interwencje.csv'
WITH (
	FIELDTERMINATOR = ',',
	ROWTERMINATOR = '\n',
	FIRSTROW = 2
);

BULK INSERT Przestepca_powoduje_interwencje
FROM 'C:\Users\pauli\OneDrive\Pulpit\semestr 5\Hurtownie danych\lab2\generated_data\przestepcy_interwencje.csv'
WITH (
	FIELDTERMINATOR = ',',
	ROWTERMINATOR = '\n',
	FIRSTROW = 2
);

BULK INSERT Policjant_na_interwencji
FROM 'C:\Users\pauli\OneDrive\Pulpit\semestr 5\Hurtownie danych\lab2\generated_data\policjanci_interwencje.csv'
WITH (
	FIELDTERMINATOR = ',',
	ROWTERMINATOR = '\n',
	FIRSTROW = 2
);