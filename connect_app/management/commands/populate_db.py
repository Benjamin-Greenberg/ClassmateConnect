# This script will populate the django database with courses from a txt file
from django.core.management import BaseCommand
from connect_app.models import Course
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import os


class Command(BaseCommand):
    args = '<data.txt>'
    help = 'This program takes in a txt file and populates the database'

    def _create_object(self, data):
        # If UTK course title is populated badly
        if len(data) > 4:
            _, created = Course.objects.get_or_create(
                crn=data[2],
                title=data[0] + '-' + data[1],
                course_number=data[3],
                section_number=data[4],
            )

        else:
            _, created = Course.objects.get_or_create(
                crn=data[1],
                title=data[0],
                course_number=data[2],
                section_number=data[3],
            )

        return _

    def web_scraper(self):
        driver = webdriver.Chrome(os.getcwd() + "\\chromedriver.exe")

        # Entry page
        driver.get("https://bannerssb.utk.edu/kbanpr/bwckschd.p_disp_dyn_sched")
        select = Select(driver.find_element_by_name("p_term"))
        select.select_by_visible_text("Fall Sem 2019")
        driver.find_element_by_xpath("//input[@type='submit']").click()

        # Secondary page
        select = Select(driver.find_element_by_xpath("//select[@name='sel_subj']"))

        options = [option.text for option in select.options]
        for option in options:
            select.select_by_visible_text(option)

        driver.find_element_by_xpath("//input[@type='submit']").click()

        # Subject page
        course_titles = driver.find_elements_by_class_name('ddtitle')

        # Place the course titles in a list with only the necessary info
        titles = [x.text + '\n' for x in course_titles]

        for title in titles:
            self._create_object(title.split(" - "))

        driver.quit()

    def handle(self, *args, **options):
        self.web_scraper()




