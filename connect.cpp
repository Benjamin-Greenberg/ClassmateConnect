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

	//friend Course();

	public:
	User();
	//new user
	User(string name, string netid, string email, string phone_number);
	~User();

	void addCourse(int, Course *);
	string getInfo();
};

class Course{

	int crn;
	string name;
	string number;
	string section;
	// <netid, user*>
	map <string, User *> students;

	public:
	Course();
	Course(int crn, string name, string number, string section);
	~Course();

	User* find(string netid);
	void addUser(string, User *);
};

/*
// max heap
class StudentHeap{

	vector<User *> h;

	public:
	StudentHeap();
	~StudentHeap();

	void Push(int d);
	int Pop();
	int Size();
	bool Empty();
	void Print();

};
*/

int main(int argc, char *argv[]){

	ifstream courseFile, userFile;
	istringstream sin;
	int crn;
	string name, number, section, line, email, netid;
	map<int, Course *> courses;
	map<int, Course *>::iterator mit;
	User* tmpUser;

	if (argc != 3){
		cout<<"Usage: ./connect course_file user_file\n";
	}

	courseFile.open(argv[1]);
	userFile.open(argv[2]);

	//read in courses
	while(courseFile >> crn){

		courseFile >> name >> number >> section;

		courses[crn] = new Course(crn, name, number, section);
	}

for(mit=courses.begin();mit!=courses.end();++mit){
	cout<<mit->first<<endl;
}

	//read in users and add to courses
	while(getline(userFile, line)){

		sin.str(line);

		sin >> netid >> name>> email >> number;

		tmpUser = new User(netid, name, email, number);

		while(sin >> crn){

			courses[crn]->addUser(netid, tmpUser);
			tmpUser->addCourse(crn, courses[crn]);
		}

		sin.clear();
	}

	//Get info stdin
	//add first class, second, third
	//map to heap
	//pop heap

	return 0;
}

User::User(){

}

User::User(string netid, string name, string email, string phone_number){
	this->netid = netid;
	this->name = name;
	this->email = email;
	this->phone_number = phone_number;
}

User::~User(){

}

void User::addCourse(int crn, Course* course){
	this->courses[crn] = course;
}

Course::Course(){

}

Course::Course(int crn, string name, string number, string section){
	this->crn = crn;
	this->name = name;
	this->number = number;
	this->section = section;
}

Course::~Course(){

}

User* Course::find(string netid){

}

void Course::addUser(string netid, User* user){
	this->students[netid] = user;
}
