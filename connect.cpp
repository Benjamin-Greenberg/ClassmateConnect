/**************************************************************
 * Classmate Connect - Prototype for final project in CS302
 * Written By Daniel Troutman and Benjamin Greenberg
 * Description: Finds students who share classes together
**************************************************************/

#include <iostream>
#include <map>
#include <vector>

using namespace std;

class User{

	string name;
	string netid;
	string email;
	string phone_number;
	map <int, course*> courses;

	friend Course();

	public:
	User();
	//new user
	User(string name, string netid, string email, string phone_number = “”);
	~User();

	void addCourse(int crn);
	string getInfo();
};

class Course{

	string name;
	string description;
	int crn;
	// <netid, user*>
	map <string, user*> students

	public:
	Course();
	~Course();

	User* find(string netid);
};

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

int main(){

	return 0;
}

User::User(){

}

User::User(string name, string netid, string email, string phone_number){

}

User::~User(){

}

User::addCourse(int crn){

}

Course::Course(){

}

Course::~Course(){

}

User* Course::find(string netid){

}

