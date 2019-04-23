# ClassmateConnect

One Paragraph of project description goes here

## Getting Started

The following sections will explain how to setup and download Classmate Connect, as well as how to use it with both 
admin and standard users. This code is not ready for official release and is only guaranteed to work in 
testing environments. For ease of use, it is best to run this code with and IDE such as PyCharm.

### Prerequisites

Follow the steps below to be able to download and run Classmate Connect.

You must have python 3.7 or later installed. Instructions below are for Debian-based Linux distros
```bash
sudo apt-get install python3
sudo apt-get install pip3
```

Install other dependencies in case setup doesn't cover everything
```bash
pip3 install django, selenium
```

### Installing

Here are the instructions to install ClassmateConnect

Clone the repo from github
```bash
git clone https://github.com/bgreenb11/ClassmateConnect.git
```

Depending on your system, use pip3 or pip to install python3 dependencies
This will call setup.py
```bash
pip3 install -e .
```


## Using Classmate Connect

In order to use Classmate Connect, you will need to gather information about courses and users. 

### Scraping the course timetable

The web-scraper for this project is built to scrape the UTK public timetables. In order to use
this to gather course info from other institutions, they must use a similar format 
for their public timetables, and the url to the first page and desired semester must be
changed in connect_app/management/commands/populate_db.py as shown below
```
# Url goes in here
driver.get("https://bannerssb.utk.edu/kbanpr/bwckschd.p_disp_dyn_sched")
select = Select(driver.find_element_by_name("p_term"))
# Semester goes here
select.select_by_visible_text("Fall Sem 2019")
driver.find_element_by_xpath("//input[@type='submit']").click()
```

* To use the web-scraper, simply run the following command in the terminal*
```bash
python3 manage.py populate_db
```
_*_ Depending on the number of subjects and courses, the web-scraper could take 
up to several minutes to finish
### Administration Use

* To access the admin site, simply go to the admin page by typing /admin after the domain name for example
```
https://127.0.0.1:8000/admin
```
And you will be directed to the admin login page*<br />
![image](https://user-images.githubusercontent.com/33168761/56465029-a0428f80-63c3-11e9-8364-7ccfe5cc5f63.png)
<br />
*You must have created a super user or you will not be able to access the admin page without another admin's login

* After logging in, you will see the admin index, where you can access the Student and Course models.
The Group model is provided by Django by default and is not in use at the moment.
![image](https://user-images.githubusercontent.com/33168761/56465059-35de1f00-63c4-11e9-8572-49a8d5b209ca.png)
Clicking on connect_app will send you to the connect_app page and its models will be the only thing displayed

* Clicking on the Course model will send you to the page with all Course models
![image](https://user-images.githubusercontent.com/33168761/56465068-72aa1600-63c4-11e9-8888-2ba750134da6.png)
Here you can: <br />
1) Select multiple courses, and then go to actions, where currently the only option is to delete
the selected course models
2) Select the add course option in the upper-right corner

* If you select the add course option, you'll be redirected here and be able to create a new Course model
![image](https://user-images.githubusercontent.com/33168761/56465095-07ad0f00-63c5-11e9-8bd0-6f33ba4d6a9f.png)
You can specify the Course model's title, crn, course number, and section number, as well as the students 
that have already been created to add to the Course model's students field

* The admin page for the Student models is similar to the Course model's admin page
![image](https://user-images.githubusercontent.com/33168761/56465113-7722fe80-63c5-11e9-8a8b-2ca40dfbd04b.png)
There is a search bar on this page that is currently unavailable on the Course model's admin page

* Adding a new Student model is similar to adding a Course model
![image](https://user-images.githubusercontent.com/33168761/56465140-e4369400-63c5-11e9-931e-70bad4fa137f.png)
Here you can specify the Student model's username, first name, last name, encrypted password, and whether
they have admin status or not. Do not unselect the active option.

### Standard Use

Once you go to the landing page for Classmate Connect, there are three options presented:<br />
    1. Courses Index - View every course in the database<br />
    2. Student Login - Use existing user credentials to search for classmates<br />
    3. Sign Up - Creating a new user<br />
![image](https://user-images.githubusercontent.com/39277609/56462451-4032f580-6391-11e9-812c-ea4d58183bb4.png)

#### Courses Index

The courses index contains a list of all classes in the database. Each class will direct to a page with more details
and a list of all the students taking the course.

![image](https://user-images.githubusercontent.com/39277609/56462908-0fef5500-6399-11e9-868e-ba9fec0be442.png)
![image](https://user-images.githubusercontent.com/39277609/56462894-ce5eaa00-6398-11e9-9221-910237f51fbe.png)

#### Student Login

The login page is where a user can enter their credentials to access their profile. The profile consists of all relevant
user data as well as a list of classmates paired with the number of similar classes to the user.

The user can add courses and remove courses at will to fit their current schedule.
#### Sign Up

The sign up page allows new users to enter their information and find classmates. Once a user has signed up, they will
be redirected to the login page, where they can sign in.

## Known Bugs
* It is not possible to add/remove classes for a student model on the admin's page
* Djagno testing environment occaisionally throws error when loggin in, cause is currently unknown
* No option to change/recover password, will be added later


## Built With

* [Django](https://docs.djangoproject.com/en/2.2/) - The backend web framework used
* [SQLite](https://www.sqlite.org/index.html) - Database _-Temp_
* [Python](https://www.python.org/) - Main Language

## Authors

* **Benjamin Greenberg**  - [bgreenb11](https://github.com/bgreenb11)
* **Daniel Troutman** - [daniel-troutman](https://github.com/daniel-troutman)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Hat tip to anyone whose code was used
* Inspiration
* etc
