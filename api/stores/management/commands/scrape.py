from django.core.management.base import BaseCommand
from discountHunter.cron import get_data


class Command(BaseCommand):
    help = 'Scrape for the available websites for new data'

    def handle(self, *args, **options):
        get_data()
        self.stdout.write(self.style.SUCCESS('Successfully scraped for new data'))
