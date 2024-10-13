from django.core.management.base import BaseCommand
# from clients.utils import load_clients_csv, load_potential_clients_csv
from clients.utils import load_passports_csv

# class Command(BaseCommand):
#     help = 'Загрузи файл CSV'

#     def handle(self, *args, **kwargs):
#         # load_clients_csv('/home/soc_sent1nelx/Projects/Project_Alih/django_zaimer_project/CSV_FILES/clients.csv')
#         load_passports_csv('/home/soc_sent1nelx/Projects/Project_Alih/django_zaimer_project/CSV_FILES/passports.csv')
#         # load_potential_clients_csv('/home/soc_sent1nelx/Projects/Project_Alih/django_zaimer_project/CSV_FILES/potential_clients.csv')
#         self.stdout.write(self.style.SUCCESS('Данные успешно загружены УРА'))


class Command(BaseCommand):
    help = 'Загрузить данные из CSV'

    def handle(self, *args, **kwargs):
        start_row = 1619356
        load_passports_csv('/home/soc_sent1nelx/Projects/Project_Alih/django_zaimer_project/CSV_FILES/passports.csv', start_row=start_row)
        self.stdout.write(self.style.SUCCESS('Данные успешно загружены УРА'))



# from django.core.management.base import BaseCommand
# from clients.utils import load_clients_csv

# class Command(BaseCommand):
#     help = 'Загрузи файл CSV с указанной строки'

#     def add_arguments(self, parser):
#         # Добавляем аргумент для указания стартовой строки
#         parser.add_argument('--start_row', type=int, help='Номер строки, с которой начать загрузку', default=0)

#     def handle(self, *args, **options):
#         start_row = options['start_row']  # Получаем номер строки
#         load_clients_csv('/home/soc_sent1nelx/Projects/Project_Alih/django_zaimer_project/CSV_FILES/clients.csv', start_row=start_row)
#         self.stdout.write(self.style.SUCCESS(f'Данные успешно загружены с {start_row} строки!'))
