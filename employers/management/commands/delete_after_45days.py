from django.core.management.base import BaseCommand
from datetime import datetime, timedelta
from employers.models import JobPost

class Command(BaseCommand):
    help = ' Delete Job Listing(s) after 30 days'

    def handle(self, *args, **kwargs):
        delete_listings = JobPost.objects.filter(date_posted__gte=datetime.now()-timedelta(days=46))
        
        delete_listings.delete()
        delete_listings.deleted_after_45_days = True
        self.stdout.write('Deleted Job Listings older than 45 days')

