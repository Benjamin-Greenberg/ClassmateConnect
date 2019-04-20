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

Depending on your system,use pip3 or pip to install python3 dependencies
This will call setup.py
```bash
pip3 install -e .
```


## Using Classmate Connect

In order to use Classmate Connect, you will need to gather information about courses and users. 

### Scraping the course timetable

Explain what these tests test and why

```
Give an example
```

### Administration Use

Explain what these tests test and why

```
Give an example
```

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

The login page is where a user can enter their credential to access their profile. The profile consists of all relevant
user data as well as a list of classmates paired with the number of similar classes to the user.

#### Sign Up

The sign up page allows new users to enter their information and find classmates. Once a user has signed up, they will
be redirected to the login page, where they can sign in.

## Deployment

Add additional notes about how to deploy this on a live system

## Built With

* [Dropwizard](http://www.dropwizard.io/1.0.2/docs/) - The web framework used
* [Maven](https://maven.apache.org/) - Dependency Management
* [ROME](https://rometools.github.io/rome/) - Used to generate RSS Feeds

## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags). 

## Authors

* **Billie Thompson** - *Initial work* - [PurpleBooth](https://github.com/PurpleBooth)

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Hat tip to anyone whose code was used
* Inspiration
* etc