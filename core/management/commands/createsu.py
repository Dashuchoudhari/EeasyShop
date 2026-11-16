from django.core.management.base import BaseCommand
from userauths.models import User

class Command(BaseCommand):
    help = 'Forces creation or password reset for admin user'

    def handle(self, *args, **options):
        username = "admin"
        email = "admin@gmail.com"
        password = "AdminPassword123"

        if User.objects.filter(username=username).exists():
            user = User.objects.get(username=username)
            user.set_password(password)
            user.is_superuser = True
            user.is_staff = True
            user.save()
            self.stdout.write(self.style.SUCCESS(f'Successfully reset password for existing user: {username}'))
        else:
            User.objects.create_superuser(
                email=email,
                username=username,
                password=password
            )
            self.stdout.write(self.style.SUCCESS(f'Successfully created new superuser: {username}'))
