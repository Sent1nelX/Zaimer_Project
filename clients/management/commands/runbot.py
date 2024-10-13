from django.core.management.base import BaseCommand
from clients.telegram_bot import RunBot  # Подкорректируй путь, если нужно

class Command(BaseCommand):
    help = 'Запуск Telegram бота'

    def handle(self, *args, **kwargs):
        RunBot()
