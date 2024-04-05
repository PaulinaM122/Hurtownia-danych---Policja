import os
import pandas as pd
import random
from faker import Faker
from faker.providers import DynamicProvider

import main
import datetime

policemen_filename = 'generated_data/policjanci.csv'
criminals_filename = 'generated_data/przestepcy.csv'
stations_filename = 'generated_data/komisariaty.csv'
equipment_filename = 'generated_data/wyposazenie.csv'
interventions_filename = 'generated_data/interwencje.csv'
criminals_interventions_filename = 'generated_data/przestepcy_interwencje.csv'
policemen_interventions_filename = 'generated_data/policjanci_interwencje.csv'
equipment_interventions_filename = 'generated_data/wyposazenie_interwencje.csv'

def load_data_from_csv(filename):
    if os.path.exists(filename):
        return pd.read_csv(filename)
    else:
        return pd.DataFrame()

def modify_interventions_T1(interventions_T1):
    # Interwencje o statusie "w toku" w danych T1
    in_progress_interventions = interventions_T1[interventions_T1['Status'] == 'W toku']

    for index, row in in_progress_interventions.iterrows():
        interventions_T1.at[index, 'Status'] = 'Zakończona'
        interventions_T1.at[index, 'Powodzenie'] = random.choice([0, 1])

    return interventions_T1

def modify_criminals_T1(criminals_T1):
    for index, row in criminals_T1.iterrows():
        if random.random() < 0.5:
            criminals_T1.loc[index, 'Czy_zatrzymany'] = 1

    return criminals_T1


def generate_interventions(fake, id, start_date=None, end_date=None):
    crime_type_provider = DynamicProvider(
        provider_name="crime_type",
        elements=["kradzież", "zniszczenie mienia", "zastraszanie", "rozbój", "przeciwko życiu człowieka", "spowodowanie uszczerbku na zdrowiu", "oszustwo", "inne"]
    )
    fake.add_provider(crime_type_provider)

    interventions_df = pd.DataFrame(columns=['ID', 'Data', 'Lokalizacja', 'Opis_zdarzenia', 'Rodzaj', 'Status', 'Powodzenie'])
    for i in range(id, id + main.NO_OF_INTERVENTIONS):
        interventions_df.loc[i] = main.generate_intervention(fake, i, start_date, end_date)
    interventions_df = interventions_df.drop_duplicates(keep='first')
    interventions_df.to_csv(interventions_filename)

def generate_data_T2():
    policemen_T1 = load_data_from_csv(policemen_filename)
    criminals_T1 = load_data_from_csv(criminals_filename)
    stations_T1 = load_data_from_csv(stations_filename)
    equipment_T1 = load_data_from_csv(equipment_filename)
    interventions_T1 = load_data_from_csv(interventions_filename)
    policemen_interventions_T1 = load_data_from_csv(policemen_interventions_filename)
    criminals_interventions_T1 = load_data_from_csv(criminals_interventions_filename)
    equipment_interventions_T1 = load_data_from_csv(equipment_interventions_filename)

    #Zapisanie danych T1, bo poprzednie zostaną nadpisane przez T2
    policemen_T1.to_csv("generated_data/policjanciT1.csv", index=False)
    criminals_T1.to_csv("generated_data/przestepcyT1.csv", index=False)
    stations_T1.to_csv("generated_data/komisariatyT1.csv", index=False)
    equipment_T1.to_csv("generated_data/wyposazenieT1.csv", index=False)
    interventions_T1.to_csv("generated_data/interwencjeT1.csv", index=False)
    policemen_interventions_T1.to_csv("generated_data/policjanci_interwencjeT1.csv", index=False)
    criminals_interventions_T1.to_csv("generated_data/przestepcy_interwencjeT1.csv", index=False)
    equipment_interventions_T1.to_csv("generated_data/wyposazenie_interwencjeT1.csv", index=False)

    # Obliczanie nowych indeksów bazując na ostatnich dostępnych indeksach w plikach T1
    last_policeman_id = max(policemen_T1.iloc[:, 0]) if not policemen_T1.empty else -1
    last_criminal_id = max(criminals_T1.iloc[:, 0]) if not criminals_T1.empty else -1
    last_equipment_id = max(equipment_T1['ID']) if not equipment_T1.empty else -1
    last_intervention_id = max(interventions_T1['ID']) if not interventions_T1.empty else -1
    last_policemen_interventions_id = max(policemen_interventions_T1.iloc[:, 0]) if not policemen_interventions_T1.empty else -1
    last_criminals_interventions_id = max(criminals_interventions_T1.iloc[:, 0]) if not criminals_interventions_T1.empty else -1
    last_equipment_interventions_id = max(equipment_interventions_T1.iloc[:, 0]) if not equipment_interventions_T1.empty else -1

    # Generowanie nowych danych dla czasu T2
    main.generate_policemen(start_id=last_policeman_id + 1)
    policemen_T2 = load_data_from_csv(policemen_filename)

    # Aktualizacja liczby funkcjonariuszy w komisariatach
    for station_id in range(main.NO_OF_STATIONS):
        old_staff_count = stations_T1[stations_T1['ID'] == station_id]['Zatrudnieni_funkcjonariusze'].values[0]
        new_staff_count = len(policemen_T2[policemen_T2['Komisariat_FK'] == station_id])
        updated_staff_count = old_staff_count + new_staff_count
        stations_T1.loc[stations_T1['ID'] == station_id, 'Zatrudnieni_funkcjonariusze'] = updated_staff_count

    stations_T1.to_csv(stations_filename)
    criminals_T1 = modify_criminals_T1(criminals_T1)
    main.generate_criminals(start_id=last_criminal_id + 1)
    main.generate_equipment(start_id=last_equipment_id + 1)
    interventions_T1 = modify_interventions_T1(interventions_T1)
    generate_interventions(fake=Faker('pl_PL'), id=last_intervention_id + 1, start_date=datetime.date(2023, 11, 1), end_date=datetime.date(2023, 12, 1))

    # Wczytywanie nowych danych wygenerowanych w czasie T2
    criminals_T2 = load_data_from_csv(criminals_filename)
    equipment_T2 = load_data_from_csv(equipment_filename)
    interventions_T2 = load_data_from_csv(interventions_filename)

    # Łączenie danych z T1 i T2
    policemen_combined = pd.concat([policemen_T1, policemen_T2])
    criminals_combined = pd.concat([criminals_T1, criminals_T2])
    equipment_combined = pd.concat([equipment_T1, equipment_T2])
    interventions_combined = pd.concat([interventions_T1, interventions_T2], ignore_index=True)

    # Zapisanie połączonych danych
    policemen_combined.to_csv("generated_data/policjanciT2.csv", index=False)
    criminals_combined.to_csv("generated_data/przestepcyT2.csv", index=False)
    equipment_combined.to_csv("generated_data/wyposazenieT2.csv", index=False)
    interventions_combined.to_csv("generated_data/interwencjeT2.csv", index=False)

    main.generate_policeman_intervention_relationship(last_policemen_interventions_id + 1, main.NO_OF_INTERVENTIONS, "generated_data/policjanciT2.csv")
    main.generate_criminal_intervention_relationship(last_criminals_interventions_id + 1, main.NO_OF_CRIMINALS, "generated_data/przestepcyT2.csv")
    main.generate_equipment_intervention_relationship(last_equipment_interventions_id + 1, "generated_data/wyposazenieT2.csv")

    # Wczytywanie nowych danych wygenerowanych w czasie T2
    policemen_interventions_T2 = load_data_from_csv(policemen_interventions_filename)
    criminals_interventions_T2 = load_data_from_csv(criminals_interventions_filename)
    equipment_interventions_T2 = load_data_from_csv(equipment_interventions_filename)

    # Łączenie danych z T1 i T2
    policemen_interventions_combined = pd.concat([policemen_interventions_T1, policemen_interventions_T2])
    criminals_interventions_combined = pd.concat([criminals_interventions_T1, criminals_interventions_T2])
    equpment_interventions_combined = pd.concat([equipment_interventions_T1, equipment_interventions_T2])

    # Zapisywanie połączonych danych do nowych plików CSV
    policemen_interventions_combined.to_csv("generated_data/policjanci_interwencjeT2.csv", index=False)
    criminals_interventions_combined.to_csv("generated_data/przestepcy_interwencjeT2.csv", index=False)
    equpment_interventions_combined.to_csv("generated_data/wyposazenie_interwencjeT2.csv", index=False)

if __name__ == '__main__':
    generate_data_T2()
