# This script will populate the django database with courses from a txt file
from django.core.management import BaseCommand
from connect_app.models import Course


class Command(BaseCommand):
    args = '<data.txt>'
    help = 'This program takes in a txt file and populates the database'

    def _create_object(self, data):
        _, created = Course.objects.get_or_create(
            crn=data[1],
            title=data[0],
            course_number=data[2],
            section_number=data[3],
        )
        return _

    def handle(self, *args, **options):
        data_file = input("Enter the full path of the data file (.txt only): ")
        if data_file.endswith('.txt'):
            with open(data_file) as data:
                for data_line in data:
                    self._create_object(data_line.split(" - "))
