# Name: Gavin Riegel
# File: academic_award.py
# Description: This script will print if the student has made the Dean's List or Honor Roll by achieving a GPA of 3.5 or 3.25, respectively.
last_name = input("Enter student's last name: ")
while last_name != "ZZZ":
	first_name = input("Enter student's first name: ")
	gpa = float(input("Enter studet's GPA: "))
	if (gpa >= 3.5):
		print(first_name, last_name, "has made the Dean's List.")
	if (gpa >= 3.25):
		print(first_name, last_name, "has made the Honor Roll.")