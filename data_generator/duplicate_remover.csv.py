import csv

def remove_duplicates(input_filename, output_filename):
    # Wczytaj dane z pliku CSV
    with open(input_filename, 'r', newline='', encoding='utf-8') as input_file:
        reader = csv.DictReader(input_file)
        rows = list(reader)

    # Usuń duplikaty na podstawie numeru PESEL
    unique_rows = []
    seen_pesel = set()
    for row in rows:
        pesel = row['PESEL']
        if pesel not in seen_pesel:
            seen_pesel.add(pesel)
            unique_rows.append(row)

    # Zapisz zaktualizowane dane do pliku CSV
    with open(output_filename, 'w', newline='', encoding='utf-8') as output_file:
        fieldnames = reader.fieldnames
        writer = csv.DictWriter(output_file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(unique_rows)

if __name__ == "__main__":
    policjanci_input_filename = 'nowe_T1/policjanciT1.csv'
    przestepcy_input_filename = 'nowe_T1/przestepcyT1.csv'
    policjanciT2_input_filename = 'nowe_T2/policjanciT2.csv'
    przestepcyT2_input_filename = 'nowe_T2/przestepcyT2.csv'

    policjanci_output_filename = 'nowe_T1/policjanciT1_2.csv'
    przestepcy_output_filename = 'nowe_T1/przestepcyT1_2.csv'
    policjanciT2_output_filename = 'nowe_T2/policjanciT2_2.csv'
    przestepcyT2_output_filename = 'nowe_T2/przestepcyT2_2.csv'

    # Usuń duplikaty dla policjantów T1
    remove_duplicates(policjanci_input_filename, policjanci_output_filename)
    print(f'Duplikaty usunięte z pliku {policjanci_input_filename} i zapisane do {policjanci_output_filename}')

    # Usuń duplikaty dla przestępców T1
    remove_duplicates(przestepcy_input_filename, przestepcy_output_filename)
    print(f'Duplikaty usunięte z pliku {przestepcy_input_filename} i zapisane do {przestepcy_output_filename}')

    # Usuń duplikaty dla policjantów T2
    remove_duplicates(policjanciT2_input_filename, policjanciT2_output_filename)
    print(f'Duplikaty usunięte z pliku {policjanciT2_input_filename} i zapisane do {policjanciT2_output_filename}')

    # Usuń duplikaty dla przestępców T2
    remove_duplicates(przestepcyT2_input_filename, przestepcyT2_output_filename)
    print(f'Duplikaty usunięte z pliku {przestepcyT2_input_filename} i zapisane do {przestepcyT2_output_filename}')
