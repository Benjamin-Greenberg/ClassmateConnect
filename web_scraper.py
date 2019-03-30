from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
import os
import time
import re


# chromedriver.exe available in git repo
driver = webdriver.Chrome(os.getcwd() + "\\chromedriver.exe")

# Entry page
driver.get("https://bannerssb.utk.edu/kbanpr/bwckschd.p_disp_dyn_sched")
select = Select(driver.find_element_by_name("p_term"))
select.select_by_visible_text("Fall Sem 2019")
driver.find_element_by_xpath("//input[@type='submit']").click()

# Secondary page
select = Select(driver.find_element_by_xpath("//select[@name='sel_subj']"))

# Place following code in block comment when testing, will take a long time otherwise
options = [option.text for option in select.options]
for option in options:
	select.select_by_visible_text(option)

# Uncomment line below for testing purposes
# select.select_by_visible("Computer Science")

driver.find_element_by_xpath("//input[@type='submit']").click()

# Subject page
course_titles = driver.find_elements_by_class_name('ddtitle')

# Place the course titles in a list with only the necessary info
titles = [x.text + '\n' for x in course_titles]

# Organize info and remove dashes in between data
for title in range(len(titles)):
	tmp = titles[title].split(" - ")
	tmp[0], tmp[1] = tmp[1], tmp[0]
	tmp[1] = re.sub(' ', '_', tmp[1])
	tmp[2] = re.sub(' ', '_', tmp[2])
	tmp = " ".join(tmp)
	titles[title] = re.sub(' - ', '', tmp)


with open("courses.txt", 'w') as f:
	f.writelines(titles)

time.sleep(4)
driver.quit()
