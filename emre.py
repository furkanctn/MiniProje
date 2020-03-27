from tkinter import*

class Course : 
	def __init__(self,subject,code,credits,letter_grade):
		self.subject = subject
		self.code = code
		self.credits = credits
		self.letter_grade = letter_grade

class Student:
	def __init__(self,id,courses,gpa):
		self.id = id
		self.courses = courses
		self.gpa = gpa

class CourseGradeDAta:
	
	def __init__(self, students,letter_grade_mappings):
		self.students = students
		self.letter_grade_mappings = letter_grade_mappings

class GUI(Frame):

	def __init__(self,data,student_grades,current_student_id):
		Frame.__init__(self)
		self.data = data
		self.student_grades = student_grades
		self.current_student_id = current_student_id
		self.initUI()

	def initUI(self):
		
		self.title_label = Label(self,text = "Smart Advisor - Your Intelligent Agent",bg="blue",fg="white", 
								  font = "Normal 30",width = 67)
		self.title_label.pack()
		self.pack()

		self.label_frame = Frame(self)
		self.label_frame.pack(fill = X)

		self.upload_button = Button(self.label_frame, text=" Upload Letter Grade Data",font=("Bold"))
		self.upload_button.pack(side=LEFT,padx=75,pady=15,expand=YES)

		self.course_data_button = Button(self.label_frame, text="Upload Past Course Data",font=("Bold"))
		self.course_data_button.pack(side=LEFT,padx=85,pady=15,expand=YES)

		self.transcript_button = Button(self.label_frame, text="Upload Transcript",font=("Bold"))
		self.transcript_button.pack(side=LEFT,padx=95,pady=15,expand=YES)


		#tables

		self.frame0 = Frame(self, borderwidth=2, relief=RIDGE, width=600, height=400, bg="white")
		self.frame0.pack(padx=25, pady=25)

		self.title_label = Label(self.frame0, text="Recommendation Filters", bg="white", fg="black",
				 font=('', '10', 'bold'), width=65, height=4)
		self.title_label.pack()
		self.frame1 = Frame(self.frame0, borderwidth=2, relief=RIDGE, width=60, height=40, bg="white")
		self.frame1.pack(side=LEFT,padx=25, pady=25)
		self.subject_label = Label(self.frame1, text="Subjects:")
		self.subject_label.pack( padx=0, pady=1)
		self.lb = Listbox(self.frame1, selectmode='single')
		self.lb.pack()
		self.frame2=Frame(self.frame0, borderwidth=2, relief=RIDGE, width=60, height=40, bg="white")
		self.frame2.pack(padx=25, pady=25)

		self.button = Button(self.frame0, text="Get Recommendation", bg="white", fg="black", font=('', '8', 'bold'))
		self.button.pack(side=RIGHT, padx=35, pady=75)

		self.frame3 = Frame(self.frame0, borderwidth=2, relief=RIDGE, width=60, height=30, bg="white")
		self.frame3.pack(padx=25, pady=45)
		self.frame4 = Frame(self, borderwidth=2, relief=RIDGE, width=600, height=300, bg="white")
		self.frame4.pack(padx=25, pady=45)




def main():
	root=Tk()
	root.geometry("1200x800+300+150")
	root.title(" Smart Advisor")
	root.resizable(FALSE, FALSE)
	app=GUI(root,"1","1")
	root.mainloop()
		
main()
	

