import pandas as pd
import random
import datetime
from faker import Faker
from faker.providers import DynamicProvider
from random_pesel import RandomPESEL

NO_OF_POLICEMEN = 100
NO_OF_CRIMINALS = 100
NO_OF_STATIONS = 10
NO_OF_EQUIPMENT = 50
NO_OF_INTERVENTIONS = 100

policemen_filename = 'generated_data/policjanci.csv'
criminals_filename = 'generated_data/przestepcy.csv'
stations_filename = 'generated_data/komisariaty.csv'
equipment_filename = 'generated_data/wyposazenie.csv'
interventions_filename = 'generated_data/interwencje.csv'
criminals_interventions_filename = 'generated_data/przestepcy_interwencje.csv'
policemen_interventions_filename = 'generated_data/policjanci_interwencje.csv'
equipment_interventions_filename = 'generated_data/wyposazenie_interwencje.csv'

def generate_policemen():
    fake = Faker('pl_PL')
    police_rank_provider = DynamicProvider(
        provider_name="police_rank",
        elements=["aspirant", "funkcjonariusz", "sierżant", "inspektor", "komisarz", "nadkomisarz", "komendant"]
    )
    fake.add_provider(police_rank_provider)

    policemen_df = pd.DataFrame(columns=['PESEL', 'Imię', 'Nazwisko', 'Płeć', 'Stanowisko', 'Adres', 'Data_zatrudnienia', 'Komisariat_FK'])
    for i in range(NO_OF_POLICEMEN):
        policemen_df.loc[i] = generate_policeman(fake)
    policemen_df = policemen_df.drop_duplicates(keep='first')
    policemen_df.to_csv(policemen_filename)


def generate_policeman(fake):
    pesel = RandomPESEL()
    gender = random.randint(0, 1)
    work_exp = random.randint(1, 40)
    policeman = []

    if gender:
        policeman.append(pesel.generate(gender='m', min_age=work_exp+18))
        policeman.append(fake.first_name_male())
        policeman.append(fake.last_name_male())
        policeman.append('Mężczyzna')
    else:
        policeman.append(pesel.generate(gender='f', min_age=work_exp+18))
        policeman.append(fake.first_name_female())
        policeman.append(fake.last_name_female())
        policeman.append("Kobieta")

    policeman.append(fake.police_rank())
    policeman.append(fake.address())
    start_date = datetime.date.today() - datetime.timedelta(days=work_exp*365)
    end_date = datetime.date.today() - datetime.timedelta(days=(work_exp-1)*365)
    policeman.append(fake.date_between(start_date=start_date, end_date=end_date))
    policeman.append(random.randint(0, NO_OF_STATIONS-1))
    return policeman


def generate_criminals():
    criminals_df = pd.DataFrame(columns=['PESEL', 'Imię', 'Nazwisko', 'Płeć', 'Adres', 'Czy_zatrzymany'])
    for i in range(NO_OF_CRIMINALS):
        criminals_df.loc[i] = generate_criminal()
    criminals_df = criminals_df.drop_duplicates(keep='first')
    criminals_df.to_csv(criminals_filename)


def generate_criminal():
    fake = Faker('pl_PL')
    pesel = RandomPESEL()
    gender = random.randint(0, 1)
    is_arrested = random.randint(0, 1)
    criminal = []

    if gender:
        criminal.append(pesel.generate(gender='m', min_age=18))
        criminal.append(fake.first_name_male())
        criminal.append(fake.last_name_male())
        criminal.append("Mężczyzna")
    else:
        criminal.append(pesel.generate(gender='f', min_age=18))
        criminal.append(fake.first_name_female())
        criminal.append(fake.last_name_female())
        criminal.append("Kobieta")

    criminal.append(fake.address())
    criminal.append(is_arrested)
    return criminal


def generate_police_stations():
    stations_df = pd.DataFrame(columns=['ID', 'Nazwa', 'Adres', 'Zatrudnieni_funkcjonariusze'])
    policemen = pd.read_csv(policemen_filename, delimiter=',')
    for i in range(NO_OF_STATIONS):
        stations_df.loc[i] = generate_police_station(policemen, i)
    stations_df = stations_df.drop_duplicates(keep='first')
    stations_df.to_csv(stations_filename)


def generate_police_station(policemen, id):
    fake = Faker('pl_PL')
    station = []
    station.append(id)
    station_name = "Komisariat " + str(id + 1)
    station.append(station_name)
    station.append(fake.address())
    no_of_policemen = (policemen['Komisariat_FK'] == id).sum()
    station.append(no_of_policemen)
    return station


def generate_equipment():
    fake = Faker()
    equipment_type_provider = DynamicProvider(
        provider_name="equipment_type",
        elements=["broń", "pojazd", "środki_łączności", "inne"]
    )
    fake.add_provider(equipment_type_provider)
    vehicle_model_provider = DynamicProvider(
        provider_name="vehicle",
        elements=["Kia Ceed III", "Opel Crossland X", "Volkswagen Transporter", "Volkswagen Crafter", "BMW serii 3", "Skoda Superb", "Toyota Corolla", "Hyundai Tucson"]
    )
    fake.add_provider(vehicle_model_provider)
    weapon_provider = DynamicProvider(
        provider_name="weapon",
        elements=["Walther P99", "Glock 17", "Glock 19", "Glock 26", "Beretta APX", "Glauberyt PM-98", "H&K MP5A3", "HK UMP", "H&K G36", "Sako TRG-21", "Tonfa"]
    )
    fake.add_provider(weapon_provider)
    means_of_communication_provider = DynamicProvider(
        provider_name="means_of_communication",
        elements=["Radiostacja nasobna", "Terminal Bluebird"]
    )
    fake.add_provider(means_of_communication_provider)
    other_police_equipment_provider = DynamicProvider(
        provider_name="other_equipment",
        elements=["Kamizelka kuloodporna", "Kajdanki", "Apteczka taktyczna", "Alkomat AlcoQuant 6020", "Urządzenie do detekcji narkotyków AlereTM DDS 2", "Latarka taktyczna"]
    )
    fake.add_provider(other_police_equipment_provider)

    equipment_df = pd.DataFrame(columns=['ID', 'Nazwa', 'Numer_seryjny', 'Rodzaj'])
    for i in range(NO_OF_EQUIPMENT):
        equipment_df.loc[i] = generate_equipment_piece(fake, i)
    equipment_df = equipment_df.drop_duplicates(keep='first')
    equipment_df.to_csv(equipment_filename)


def generate_equipment_piece(fake, id):
    equipment = []
    equipment.append(id)
    eq_type = fake.equipment_type()

    if eq_type == "broń":
        eq_name = fake.weapon()
    elif eq_type == "pojazd":
        eq_name = fake.vehicle()
    elif eq_type == "środki_łączności":
        eq_name = fake.means_of_communication()
    else:
        eq_name = fake.other_equipment()

    equipment.append(eq_name)
    equipment.append(fake.vin())
    equipment.append(eq_type)
    return equipment


def generate_interventions():
    fake = Faker('pl_PL')
    crime_type_provider = DynamicProvider(
        provider_name="crime_type",
        elements=["kradzież", "zniszczenie mienia", "zastraszanie", "rozbój", "przeciwko życiu człowieka", "spowodowanie uszczerbku na zdrowiu", "oszustwo", "inne"]
    )
    fake.add_provider(crime_type_provider)

    interventions_df = pd.DataFrame(columns=['ID', 'Data', 'Lokalizacja', 'Opis_zadrzenia', 'Rodzaj', 'Status', 'Powodzenie'])
    for i in range(NO_OF_INTERVENTIONS):
        interventions_df.loc[i] = generate_intervention(fake, i)
    interventions_df = interventions_df.drop_duplicates(keep='first')
    interventions_df.to_csv(interventions_filename)


def generate_intervention(fake, id):
    intervention = []
    intervention.append(id)
    intervention.append(fake.date_between_dates(date_start=datetime.date(2023, 10, 1), date_end=datetime.date(2023, 11, 1)))
    intervention.append(fake.address())
    intervention.append("")
    intervention.append(fake.crime_type())
    status = random.randint(0, 1)
    if status:
        intervention.append("Zakończona")
        intervention.append(random.randint(0, 1))       # success
    else:
        intervention.append("W toku")
        intervention.append(1)                          # if the case isn't closed yet, success = false
    return intervention


def get_policemen_by_station(station_id):
    policemen = pd.read_csv(policemen_filename)
    # print(policemen[policemen['Komisariat_FK'] == station_id])
    return policemen[policemen['Komisariat_FK'] == station_id]


def generate_criminal_intervention_relationship():
    c_i_relationship_df = pd.DataFrame(columns=['ID_interwencji', 'PESEL_przestępcy'])
    interventions = pd.read_csv(interventions_filename)
    criminals = pd.read_csv(criminals_filename)

    relationship_file_idx = 1

    for i in range(len(interventions)):
        random_criminal_idx = random.randint(0, NO_OF_CRIMINALS - 1)
        if interventions.loc[i]['Powodzenie'] == 0:
            criminals.at[random_criminal_idx, 'Czy_zatrzymany'] = 1
        else:
            criminals.at[random_criminal_idx, 'Czy_zatrzymany'] = 0

        c_i_relationship_df.loc[relationship_file_idx] = [interventions.loc[i]['ID'], criminals.loc[random_criminal_idx]['PESEL']]
        relationship_file_idx += 1

        additional_criminals = random.randint(0, 8)
        for j in range(additional_criminals):
            random_criminal_idx = random.randint(0, NO_OF_CRIMINALS - 1)
            if interventions.loc[i]['Powodzenie'] == 0:
                is_arrested = random.randint(0, 1)
                if is_arrested:
                    criminals.at[random_criminal_idx, 'Czy_zatrzymany'] = 1
                else:
                    criminals.at[random_criminal_idx, 'Czy_zatrzymany'] = 0
            else:
                criminals.at[random_criminal_idx, 'Czy_zatrzymany'] = 1
            c_i_relationship_df.loc[relationship_file_idx] = [interventions.loc[i]['ID'], criminals.loc[random_criminal_idx]['PESEL']]
            relationship_file_idx += 1

    criminals.to_csv(criminals_filename)
    c_i_relationship_df = c_i_relationship_df.drop_duplicates(keep='first')
    c_i_relationship_df.to_csv(criminals_interventions_filename)


def generate_policeman_intervention_relationship():
    p_i_relationship_df = pd.DataFrame(columns=['ID_interwencji', 'PESEL_policjanta'])
    stations = pd.read_csv(stations_filename)

    relationship_file_idx = 1

    for i in range(NO_OF_INTERVENTIONS):
        random_station_idx = random.randint(0, NO_OF_STATIONS-1)
        policemen_from_station = get_policemen_by_station(random_station_idx)
        no_of_policemen_on_intervention = random.randint(1, stations.loc[random_station_idx]['Zatrudnieni_funkcjonariusze'])
        policemen_on_intervention = random.sample(policemen_from_station['PESEL'].to_list(), no_of_policemen_on_intervention)
        for j in range(len(policemen_on_intervention)):
            p_i_relationship_df.loc[relationship_file_idx] = [i, policemen_on_intervention[j]]
            relationship_file_idx += 1

    p_i_relationship_df = p_i_relationship_df.drop_duplicates(keep='first')
    p_i_relationship_df.to_csv(policemen_interventions_filename)


def generate_equipment_intervention_relationship():
    interventions = pd.read_csv(interventions_filename)
    equipment = pd.read_csv(equipment_filename)

    relationship_df = pd.DataFrame(columns=['ID_interwencji', 'ID_wyposazenia'])
    relationship_file_idx = 1

    for i in range(len(interventions)):
        intervention_id = interventions.loc[i]['ID']
        # Randomly select equipment for each intervention
        num_equipment = random.randint(1, 5)
        equipment_sample = random.sample(range(len(equipment)), num_equipment)

        for j in equipment_sample:
            equipment_id = equipment.loc[j]['ID']
            relationship_df.loc[relationship_file_idx] = [intervention_id, equipment_id]
            relationship_file_idx += 1

    relationship_df = relationship_df.drop_duplicates(keep='first')
    relationship_df.to_csv(equipment_interventions_filename)


if __name__ == '__main__':
    generate_policemen()
    generate_criminals()
    generate_police_stations()
    generate_equipment()
    generate_interventions()
    generate_policeman_intervention_relationship()
    generate_criminal_intervention_relationship()
    generate_equipment_intervention_relationship()
