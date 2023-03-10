from django.core.management.base import BaseCommand, CommandError
from django.conf import settings

from stores.models import Store, StoreReport
from stores.services import generate_store_report

import logging
import os


class Command(BaseCommand):
    help = 'Creates store reports for all stores'

    def handle(self, *args, **options):
        # Set up logging
        log_file_path = settings.LOGS_DIRECTORY + '/reports.log'
        logging.basicConfig(filename=log_file_path, level=logging.DEBUG, filemode='w')

        try:
            stores = Store.objects.all().values_list('store_id', flat=True)
            for store_id in stores:
                try:
                    report = generate_store_report(store_id)
                    if report is not None and isinstance(report, StoreReport):
                        message = f"Generated report successfully for {store_id}"
                        print(message)
                        logging.info(message)
                    else:
                        message = f"Error generating report for store {store_id}"
                        logging.exception(message)
                        print(message)
                except Exception as e:
                    message = f"Error generating report for store {store_id}: {e}"
                    logging.exception(message)
                    print(message)
        except Exception as e:
            logging.error(f"Error: {e}")
