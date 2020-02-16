from django.core.management.base import BaseCommand
from datetime import datetime, timedelta
from employers.models import JobPost

class Command(BaseCommand):
    help = ' Delete Job Listing(s) after 30 days'

    def handle(self, *args, **kwargs):
        no_days = datetime.now() - timedelta(days=30)
        print(no_days)
        delete_listings = JobPost.objects.filter(date_posted__gte=no_days)
        delete_listings.delete()
        delete_listings.deleted_after_30_days = True
        self.stdout.write(self.style.SUCCESS('Deleted Job Listings older than 30 days'))

