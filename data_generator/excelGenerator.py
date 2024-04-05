import pandas as pd
import random
import datetime
from faker import Faker

# Inicjalizacja generatora danych losowych
fake = Faker()

# Wczytanie plików CSV
equipment_df = pd.read_csv('generated_data/wyposazenieT2.csv')

# Dodanie brakujących kolumn
equipment_df['ID'] = equipment_df.index
equipment_df['Data_zakupu'] = [fake.date_between(start_date='-3y', end_date='now').strftime('%d.%m.%Y') for _ in range(len(equipment_df))]
equipment_df['Data_ostatniej_konserwacji'] = [fake.date_between(start_date='-3m', end_date='now').strftime('%d.%m.%Y') for _ in range(len(equipment_df))]
equipment_df['Czestotliwosc_konserwacji'] = [random.randint(1, 12) for _ in range(len(equipment_df))]
equipment_df['Stan_techniczny'] = [fake.random_element(elements=['bardzo dobry', 'dobry', 'umiarkowany', 'zly', 'bardzo zly']) for _ in range(len(equipment_df))]
equipment_df['Komentarze'] = [fake.text(max_nb_chars=50) for _ in range(len(equipment_df))]

# Arkusz 2 (Dziennik konserwacji)
maintenance_log_data = []

for id in range(1, len(equipment_df) + 1):
    id_jednostki = id
    data_zakupu = fake.date_between(start_date='-3y', end_date='now')
    data_konserwacji = fake.date_between(start_date=data_zakupu, end_date='now')
    technik_konserwacji = fake.name()
    opis_prac = fake.text(max_nb_chars=20)
    wydane_czesci = fake.text(max_nb_chars=20)
    koszty = random.randint(0, 5000)

    maintenance_log_data.append({
        'ID_konserwacji': id,
        'ID_jednostki': id_jednostki,
        'Data_konserwacji': data_konserwacji.strftime('%d.%m.%Y'),
        'Technik_konserwacji': technik_konserwacji,
        'Opis_prac': opis_prac,
        'Wydane_czesci': wydane_czesci,
        'Koszty': koszty
    })

maintenance_log_df = pd.DataFrame(maintenance_log_data)

# Zapisanie danych do arkuszy kalkulacyjnych
equipment_df.to_csv('generated_data/excel_arkusz1.csv', index=False)
maintenance_log_df.to_csv('generated_data/excel_arkusz2.csv', index=False)
