import csv
import os
import unicodedata

def usun_pierwsza_kolumne(input_path, output_path):
    with open(input_path, 'r', newline='', encoding='utf-8') as infile, \
            open(output_path, 'w', newline='', encoding='utf-8') as outfile:
        reader = csv.reader(infile)
        writer = csv.writer(outfile)

        # Pomijamy pierwszy wiersz (nagłówek)
        header = next(reader)

        # Zapisujemy nagłówek bez pierwszej kolumny
        writer.writerow(header[1:])

        # Przepisujemy pozostałe wiersze, pomijając pierwszą kolumnę
        for row in reader:
            # Zamieniamy polskie znaki na zwykłe
            row = [unicodedata.normalize('NFKD', str(cell)).encode('ASCII', 'ignore').decode('utf-8') for cell in row[1:]]
            writer.writerow(row)

def usun_dwie_pierwsze_kolumny_przestepcy(input_path, output_path):
    with open(input_path, 'r', newline='', encoding='utf-8') as infile, \
            open(output_path, 'w', newline='', encoding='utf-8') as outfile:
        reader = csv.reader(infile)
        writer = csv.writer(outfile)

        # Pomijamy pierwszy wiersz (nagłówek)
        header = next(reader)

        # Zapisujemy nagłówek bez dwóch pierwszych kolumn
        writer.writerow(header[2:])

        # Przepisujemy pozostałe wiersze, pomijając dwie pierwsze kolumny
        for row in reader:
            # Zamieniamy polskie znaki na zwykłe
            row = [unicodedata.normalize('NFKD', str(cell)).encode('ASCII', 'ignore').decode('utf-8') for cell in row[2:]]
            writer.writerow(row)

# Lista plików wejściowych i wyjściowych
pliki = [
    ('generated_data/policjanciT1.csv', 'nowe_T1/policjanciT1.csv'),
    ('generated_data/policjanciT2.csv', 'nowe_T2/policjanciT2.csv'),
    ('generated_data/policjanci_interwencjeT1.csv', 'nowe_T1/policjanci_interwencjeT1.csv'),
    ('generated_data/policjanci_interwencjeT2.csv', 'nowe_T2/policjanci_interwencjeT2.csv'),
    ('generated_data/przestepcyT1.csv', 'nowe_T1/przestepcyT1.csv'),
    ('generated_data/przestepcyT2.csv', 'nowe_T2/przestepcyT2.csv'),
    ('generated_data/przestepcy_interwencjeT1.csv', 'nowe_T1/przestepcy_interwencjeT1.csv'),
    ('generated_data/przestepcy_interwencjeT2.csv', 'nowe_T2/przestepcy_interwencjeT2.csv'),
    ('generated_data/wyposazenieT1.csv', 'nowe_T1/wyposazenieT1.csv'),
    ('generated_data/wyposazenieT2.csv', 'nowe_T2/wyposazenieT2.csv'),
    ('generated_data/wyposazenie_interwencjeT1.csv', 'nowe_T1/wyposazenie_interwencjeT1.csv'),
    ('generated_data/wyposazenie_interwencjeT2.csv', 'nowe_T2/wyposazenie_interwencjeT2.csv'),
    ('generated_data/komisariatyT1.csv', 'nowe_T1/komisariatyT1.csv'),
    ('generated_data/komisariaty.csv', 'nowe_T2/komisariaty.csv'),
    ('generated_data/interwencjeT1.csv', 'nowe_T1/interwencjeT1.csv'),
    ('generated_data/interwencjeT2.csv', 'nowe_T2/interwencjeT2.csv'),
    ('generated_data/excel_arkusz1.csv', 'nowe_T2/excel_arkusz1.csv'),
]

# Iterujemy przez listę plików i stosujemy odpowiednie funkcje usuwające kolumny
for input_file, output_file in pliki:
    if 'generated_data/przestepcyT1.csv' in input_file or 'generated_data/przestepcyT2.csv' in input_file or 'generated_data/komisariaty.csv' in input_file:
        usun_dwie_pierwsze_kolumny_przestepcy(input_file, output_file)
    else:
        usun_pierwsza_kolumne(input_file, output_file)
    print(f'Plik {input_file} został przetworzony, wynik zapisany w {output_file}.')
