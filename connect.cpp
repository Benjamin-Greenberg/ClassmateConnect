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
	string getNetID();
};

class Course{

	int crn;
	string name;
	string number;
	string section;
	vector<User*> students;

	public:
	Course();
	Course(int crn, string name, string number, string section);
	~Course();

int size(){return students.size();}
	void addStudents(map<User*, int>&);
	void addUser(User *);
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

	fstream courseFile, userFile;
	istringstream sin;
	int crn;
	string name, number, section, line, email, netid;
	map<int, Course *> courses;
	map<int, Course *>::iterator mit;
	map<User *, int> classmates_map;
	vector<pair<User *, int> > classmates_vec;
	User* tmpUser;
	Course* tmpCourse;

	if (argc != 3){
		cout<<"Usage: ./connect course_file user_file\n";
		return 1;
	}

	courseFile.open(argv[1]);
	//userFile.open(argv[2], fstream::in | fstream::out);
	userFile.open(argv[2]);

	//read in courses
	while(courseFile >> crn){

		courseFile >> name >> number >> section;

		courses[crn] = new Course(crn, name, number, section);
	}

///*
for(mit=courses.begin();mit!=courses.end();++mit){
	cout<<mit->first<<"\t"<<mit->second->size()<<endl;
}
//*/

	//read in users and add to courses
	while(getline(userFile, line)){

		sin.str(line);

		sin >> netid >> name>> email >> number;

		tmpUser = new User(netid, name, email, number);

		while(sin >> crn){

			courses[crn]->addUser(tmpUser);
			tmpUser->addCourse(crn, courses[crn]);
		}

		sin.clear();
	}

	//get new user info
	cout << "Name?\n";
	cin >> name;
	cout << "NetID?\n";
	cin >> netid;
	cout << "Email?\n";
	cin >> email;
	cout << "Phone Number?\n";
	cin >> number;

	//searches through classes and adds classmates
	cout << "Enter courses by CRN\n";
	while(cin >> crn){
//cout<<"here\n";

		tmpCourse = courses[crn];

		tmpCourse->addStudents(classmates_map);
//cout<<classmates_map.begin()->first->getNetID()<<"\t"<<classmates_map.begin()->second<<endl;
	}

	//turn classmates into heap
	copy(classmates_map.begin(), classmates_map.end(), classmates_vec.begin());

for(int i=0;i<classmates_vec.size();i++){
	cout<<classmates_vec.at(i).first->getNetID()<<"\t"<<classmates_vec.at(i).second<<endl;
}

	//add first class, second, third
	//map to heap
	//pop heap
	//add user to file
	courseFile.close();
	userFile.close();

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

string User::getNetID(){
	return netid;
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

void Course::addStudents(map<User*, int>& classmates_map){

/*
map<User*,int>::iterator mit;
for(mit=classmates_map.begin();mit!=classmates_map.end();mit++){
	cout<<mit->first->getNetID()<<"\t"<<mit->second<<endl;
}
*/
cout<<"here3\n";
cout<<students.size()<<endl;
cout<<"here4\n";
	int i;
	for(i=0;i<students.size();i++){

//cout<<"here2\n";
		classmates_map[students.at(i)]++;
	}


}

void Course::addUser(User* user){
	students.push_back(user);
}
