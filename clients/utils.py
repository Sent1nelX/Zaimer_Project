import csv
from .models import Client, Passport, PotentialClient
from django.utils.dateparse import parse_datetime

# def load_clients_csv(file_path):
#     with open(file_path, mode='r', encoding='utf-8') as file:
#         reader = csv.reader(file)
#         for row in reader:
#             Client.objects.create(
#                 client_id=row[0],
#                 first_name=row[1],
#                 last_name=row[2],
#                 middle_name=row[3],
#                 gender=row[4],
#                 source=row[5],
#                 phone=row[6],
#                 email=row[7],
#                 status=row[8],
#                 other1=row[9],
#                 other2=row[10],
#                 credit_status=row[11],
#                 other_details=row[12],
#                 created_at=parse_datetime(row[13]),
#                 updated_at=parse_datetime(row[14]),
#                 language=row[15],
#                 uuid=row[16]
#             )


def load_clients_csv(file_path, start_row=0):
    with open(file_path, mode='r', encoding='utf-8') as file:
        reader = csv.reader(file)
        row_count = 0  # Счётчик строк
        for row in reader:
            row_count += 1
            if row_count < start_row:
                continue  # Пропускаем строки до указанного номера

            # Создаем запись в модели Client
            try:
                Client.objects.create(
                    client_id=row[0],
                    first_name=row[1],
                    last_name=row[2],
                    middle_name=row[3],
                    gender=row[4],
                    source=row[5],
                    phone=row[6],
                    email=row[7],
                    status=row[8],
                    other1=row[9],
                    other2=row[10],
                    credit_status=row[11],
                    other_details=row[12],
                    created_at=parse_datetime(row[13]),
                    updated_at=parse_datetime(row[14]),
                    language=row[15],
                    uuid=row[16]
                )
            except Exception as e:
                print(f"Ошибка при обработке строки {row_count}: {e}")


# def load_passports_csv(file_path):
#     with open(file_path, mode='r', encoding='utf-8') as file:
#         reader = csv.reader(file)
#         for row in reader:
#             Passport.objects.create(
#                 client_id=row[0],
#                 passport_number=row[2],
#                 issue_date=row[4],
#                 expiry_date=row[5],
#                 issuing_authority=row[6],
#                 birth_date=row[7],
#                 place_of_birth=row[8],
#                 created_at=parse_datetime(row[9]),
#                 updated_at=parse_datetime(row[10])
#             )

# 388091

# def load_passports_csv(file_path):
#     with open(file_path, mode='r', encoding='utf-8') as file:
#         reader = csv.reader(file)
#         for row in reader:
#             try:
#                 # Пытаемся найти клиента
#                 client = Client.objects.get(id=row[0])
#             except Client.DoesNotExist:
#                 client = None  # Если клиент не найден, оставляем None

#             # Создаём запись в модели Passport
#             Passport.objects.create(
#                 client=client,  # Можно оставить None, если клиент не найден
#                 passport_number=row[2],
#                 issue_date=row[4],
#                 expiry_date=row[5],
#                 issuing_authority=row[6],
#                 birth_date=row[7],
#                 place_of_birth=row[8],
#                 created_at=parse_datetime(row[9]),
#                 updated_at=parse_datetime(row[10])
#             )


def load_passports_csv(file_path, start_row=0):
    with open(file_path, mode='r', encoding='utf-8') as file:
        reader = csv.reader(file)
        for i, row in enumerate(reader):
            if i < start_row:
                continue  # Пропускаем строки до start_row

            try:
                # Пытаемся найти клиента
                client = Client.objects.get(id=row[0])
            except Client.DoesNotExist:
                client = None  # Если клиент не найден, оставляем None

            # Создаём запись в модели Passport
            Passport.objects.create(
                client=client,  # Можно оставить None, если клиент не найден
                passport_number=row[2],
                issue_date=row[4],
                expiry_date=row[5],
                issuing_authority=row[6],
                birth_date=row[7],
                place_of_birth=row[8],
                created_at=parse_datetime(row[9]),
                updated_at=parse_datetime(row[10])
            )



def load_potential_clients_csv(file_path):
    with open(file_path, mode='r', encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            PotentialClient.objects.create(
                client_id=row[0],
                created_at=parse_datetime(row[10]),
                updated_at=parse_datetime(row[11]),
                phone=row[12],
                contract_id=row[13],
                external_data=row[15]
            )
