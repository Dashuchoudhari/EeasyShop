from django.core.management.base import BaseCommand
from userauths.models import User

class Command(BaseCommand):
    help = 'Crates a superuser automatically if none exists'

    def handle(self, *args, **options):
        if not User.objects.filter(is_superuser=True).exists():
            User.objects.create_superuser(
                email="admin@gmail.com",
                username="admin",
                password="AdminPassword123"
            )
            self.stdout.write(self.style.SUCCESS('Successfully created superuser'))
        else:
            self.stdout.write('Superuser already exists')
