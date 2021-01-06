import time
from django.db import connections
from django.db.utils import OperationalError
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    """django command to pause execution until the db became available
    """

    def handle(self, *args, **options):
        db_conn = None
        while not db_conn:
            try:
                db_conn = connections['default']
            except OperationalError:
                self.stdout.write(self.style.WARNING('db is unavailable right now, waiting ...'))
                time.sleep(1)
        self.stdout.write(self.style.SUCCESS('db is available'))
