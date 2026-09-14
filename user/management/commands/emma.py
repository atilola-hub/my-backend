from django.core.management.base import BaseCommand
from authentication.models import User
from django.db import connection

class Command(BaseCommand):
    def handle(self, *args, **options):
        self.hiit()
    def hiit(self):
        users = User.objects.all()
        #list(users)
        print(users)
        print(connection.queries)
