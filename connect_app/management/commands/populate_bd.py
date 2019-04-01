from django.core.management import BaseCommand
from connect_app.models import Course


class Command(BaseCommand):
    args = '<data.txt>'
    help = 'This program takes in a txt file and populates the database'

    def _create_object(self, data):
        _, created = Course.create(
            crn=data[0],
            title=data[1],
            course_number=data[2],
            section_number=data[3],
        )
        return

    def handle(self, *args, **options):
        pass
