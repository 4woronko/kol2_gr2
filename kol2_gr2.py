#!/usr/bin/env python
#
# Class diary  
#
# Create program for handling lesson scores.
# Use python to handle student (highscool) class scores, and attendance.
# Make it possible to:
# - Get students total average score (average across classes)
# - get students average score in class
# - hold students name and surname
# - Count total attendance of student
# The default interface for interaction should be python interpreter.
# Please, use your imagination and create more functionalities. 
# Your project should be able to handle entire school.
# If you have enough courage and time, try storing (reading/writing) 
# data in text files (YAML, JSON).
# If you have even more courage, try implementing user interface.


def main():
	#prepare diary
	at = 'Attendance'
	gr = 'Grades'
	l1 = 'C++'
	l2 = 'Python'
	s1 = 'Jan Nowak'
	a1 = [True, False, True, True]
	g1 = [5.0, 3.5, 2.0]
	s2 = 'Piotr Nowak'
	a2 = [True, True, True, True]
	g2 = [5.0, 5.0, 5.0]
	#create diary
	d = { s1 : {l1 : {at : a1, gr : g1}, l2: {at : a2, gr : g2} } }
	d[s2] = {l1 : {at: a2, gr: g2}}
	#total average score of Jan Nowak
	average = 0.0
	no = 0.0
	for i in d['Jan Nowak'].values():
		average += sum(i['Grades'])
		no += len(i['Grades'])
	print "The total average score of Jan Nowak equals: " + str(average/no) + '.'
	#average score of Jan Nowak in C++
	average = sum(d['Jan Nowak']['C++']['Grades'])
	no = len(d['Jan Nowak']['C++']['Grades'])
	print 'The average score of Jan Nowak in C++ equals: ' + str(average/no) + '.'
	#Full Name of students
	print 'Full students\' names : ' + str(d.keys()) + '.'
	#Total attendance of Jan Nowak
	average = 0.0
	no = 0.0
	for i in d['Jan Nowak'].values() :
		average += sum(i['Attendance'])
		no += len(i['Attendance'])
	print 'Jan Nowak\'s attendance equal\'s ' + str(100*(average/no)) + "%."
	
if __name__ == "__main__":
	main()
