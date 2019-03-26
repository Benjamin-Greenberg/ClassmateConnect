from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
import os
import time


def main():
	scraper();

def scraper():
	driver = webdriver.Chrome(os.getcwd() + "\\chromedriver.exe")

	driver.set_page_load_timeout(10)
	
	# Entry page
	driver.get("https://bannerssb.utk.edu/kbanpr/bwckschd.p_disp_dyn_sched")
	select = Select(driver.find_element_by_name("p_term"))
	select.select_by_visible_text("Fall Sem 2019")
	driver.find_element_by_xpath("//input[@type='submit']").click()

	# Secondary page
	select = Select(driver.find_element_by_xpath("//select[@name='sel_subj']"))
	select.select_by_visible_text("Computer Science")
	driver.find_element_by_xpath("//input[@type='submit']").click()

	# Subject page
	course_titles = driver.find_elements_by_class_name('ddtitle')
	titles = [x.text + '\n' for x in course_titles]

	with open("tmp.txt", 'w') as f:
		f.writelines(titles)

	time.sleep(10)
	driver.quit()


main()