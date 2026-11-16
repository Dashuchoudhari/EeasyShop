from django.core.management.base import BaseCommand
from userauths.models import User  # Apne user model ka import check kar lena

class Command(BaseCommand):
    help = 'Crates a superuser automatically if none exists'

    def handle(self, *args, **options):
        if not User.objects.filter(is_superuser=True).exists():
            User.objects.create_superuser(
                email="admin@gmail.com",  # Apni marzi ki email
                username="admin",         # Apni marzi ka username
                password="AdminPassword123" # Apna secure password
            )
            self.stdout.write(self.style.SUCCESS('Successfully created superuser'))
        else:
            self.stdout.write(self.style.INFO('Superuser already exists'))
