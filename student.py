class Student:
    def __init__(self,):
        self.name = ""
        self.studentID = ""
        self.courseList = []
        
    def setName(self, name):
        self.name = name
    def getName(self):
        return self.name
    
    def setStudentID(self, studentID):
        self.studentID = studentID
    def getStudentID(self):
        return self.studentID
    
    def addCourse(self, course):
        self.courseList.append(course)
    def removeCourse(self, course):
        if course in self.courseList:
            self.courseList.remove(course)
    def displayCourses(self):
        for course in self.courseList:
            print(course)
            