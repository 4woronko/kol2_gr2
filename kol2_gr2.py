#!/usr/bin/env python


class Student(object):
	def __init__(self,first_name,last_name):
		if isinstance(first_name,str) and isinstance(last_name,str):
			self.__first_name = first_name
			self.__last_name = last_name
			self.__lectures = []
		else:
			raise TypError("Wrong type - names are strings")
	def add_lecture(self,new_lecture):
		if isinstance(new_lecture,Lecture):
			self.__lectures.append(new_lecture)
		else:
			raise TypError("Wrong type - You have to add a lecture")
	def get_full_name(self):
		return self.__first_name + self.__last_name
	def get_average_score(self):
		aver = 0
		count = 0
		for lecture in self.__lectures:
			aver += sum(lecture.get_scores())
			count +=len(lecture.get_scores())
		return aver/count
	def get_full_attendance(self):
		total = 0
		for lecture in self.__lectures:
			total+= sum(lecture.get_attendance())
		return total
	def get_lecture_by_name(self,name):
		if isinstance(name,str):
			for lecture in self.__lectures:
				if lecture.get_lecture_name() == name:
					return lecture
		

class Lecture(object):
	def __init__(self,lecture_name):
		if isinstance(lecture_name,str):
			self.__lecture_name = lecture_name
			self.__attendance = []
			self.__scores = []
		else:
			raise TypError("Wrong type - lecture names are strings")
	def add_score(self,score):
		if isinstance(score,float):
			self.__scores.append(score)
		else:
			raise TypError("Wrong type - scores are numbers")
	def	add_attendance(self, attendance_status):
		if isinstance(attendance_status,bool):
			self.__attendance.append(attendance_status)
		else:
			raise TypError("Wrong type - attendance is boolean")
	def get_attendance(self):
		temp_attendance = self.__attendance[:]
		return temp_attendance
	def get_scores(self):
		temp_scores = self.__scores[:]
		return temp_scores
	def get_lecture_name(self):
		return self.__lecture_name

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
	s1 = Student("Tezeusz","Woronko")
	l1 = Lecture("Python in the Entrprise")
	l1.add_score(5.0)
	l1.add_attendance(True)
	s1.add_lecture(l1)	
	print s1.get_average_score()
	print s1.get_full_name()
	print s1.get_full_attendance()



if __name__ == "__main__":
	main()
