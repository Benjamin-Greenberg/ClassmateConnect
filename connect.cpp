/**************************************************************
 * Classmate Connect - Prototype for final project in CS302
 * Written By Daniel Troutman and Benjamin Greenberg
 * Description: Finds students who share classes together
**************************************************************/

#include <iostream>
#include <map>
#include <vector>
#include <algorithm>
#include <fstream>
#include <sstream>

using namespace std;

class Course;

class User{

	string netid;
	string name;
	string email;
	string phone_number;
	map <int, Course *> courses;

	public:
	User(string name, string netid, string email, string phone_number);

	void addCourse(int, Course *);
	void print();
	string getNetID();
};

class Course{

	int crn;
	string name;
	string number;
	string section;
	vector<User*> students;

	public:
	Course(int crn, string name, string number, string section);

	void addStudents(map<User*, int>&);
	void addUser(User *);
};

bool cmp(pair<User*,int> &u1, pair<User*, int> &u2){
	return u1.second < u2.second;
}

int main(int argc, char *argv[]){

	fstream courseFile, userFile;
	istringstream sin;
	int crn;
	string name, number, section, line, email, netid;
	map<int, Course *> courses;
	map<int, Course *>::iterator mit;
	map<User *, int> classmates_map;
	vector<User*> users;
	User* tmpUser;
	Course* tmpCourse;

	if (argc != 3){
		cout<<"Usage: ./connect course_file user_file\n";
		return 1;
	}

	courseFile.open(argv[1]);
	userFile.open(argv[2]);

	//read in courses
	while(courseFile >> crn){

		courseFile >> name >> number >> section;

		courses[crn] = new Course(crn, name, number, section);
	}

	//read in users and add to courses
	while(getline(userFile, line)){

		sin.str(line);

		sin >> netid >> name>> email >> number;

		tmpUser = new User(netid, name, email, number);

		users.push_back(tmpUser);

		while(sin >> crn){

			courses[crn]->addUser(tmpUser);
			tmpUser->addCourse(crn, courses[crn]);
		}

		sin.clear();
	}

	userFile.close();
	userFile.open(argv[2], ios::out | ios::app);

	//get new user info
	cout << "Name?\n";
	cin >> name;
	cout << "NetID?\n";
	cin >> netid;
	cout << "Email?\n";
	cin >> email;
	cout << "Phone Number?\n";
	cin >> number;

	//write new user to database
	userFile << netid << " " << name << " " << email << " " << number;

	//searches through classes and adds classmates
	cout << "Enter courses by CRN\n";
	while(cin >> crn){

		if (courses.find(crn) != courses.end()){

			tmpCourse = courses[crn];

			tmpCourse->addStudents(classmates_map);
		}

		userFile << " " << crn;
	}

	userFile << endl;

	//turn classmates into heap
	vector<pair<User *, int> > classmates_vec(classmates_map.begin(), classmates_map.end());
	make_heap(classmates_vec.begin(), classmates_vec.end(), cmp);

	//output classmate

	//Option 1
	/*
	cout<<"Your match is ";
	classmates_vec.at(0).first->print();
	cout<<"You have "<<classmates_vec.at(0).second<<" classes in common"<<endl;
	pop_heap(classmates_vec.begin(), classmates_vec.end());
	*/

	//Option 2
	cout<<classmates_vec.at(0).first->getNetID()<<" "<<classmates_vec.at(0).second<<",\n";

	for(mit=courses.begin();mit!=courses.end();++mit){
		delete mit->second;
	}

	for(int i=0;i<users.size();i++){
		delete users.at(i);
	}

	courseFile.close();
	userFile.close();

	return 0;
}

User::User(string netid, string name, string email, string phone_number){
	this->netid = netid;
	this->name = name;
	this->email = email;
	this->phone_number = phone_number;
}

void User::addCourse(int crn, Course* course){
	this->courses[crn] = course;
}

void User::print(){
	printf("%s\nPhone Number:%s\nEmail:%s\n", name.c_str(), phone_number.c_str(), email.c_str());
}

string User::getNetID(){
    return netid;
}

Course::Course(int crn, string name, string number, string section){
	this->crn = crn;
	this->name = name;
	this->number = number;
	this->section = section;
}

void Course::addStudents(map<User*, int>& classmates_map){
	for(int i=0;i<students.size();i++){
		classmates_map[students.at(i)]++;
	}
}

void Course::addUser(User* user){
	students.push_back(user);
}
