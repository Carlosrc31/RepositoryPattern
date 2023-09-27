from users.model import course_model
from users.repository.courses_abstract import CoursesAbstract

class CourseRepo(CoursesAbstract):
    
    def __init__(self):
        self.courses = []

    def add(self, course: course_model.Course ):
        course_exists = next((obj for obj in range(len(self.courses)) if self.courses[obj].name == course.name), True)
        if course_exists is True:
            self.courses.append(course)
            #return course_exists
            return self.courses
        return False
        

    def get(self, course_id) -> course_model.Course:
        #Find the course with the given course_id
        course = next((course for course in self.courses if course.id == int(course_id)), None)
        return course

        #for course in courses:
        #    if course.id == int(course_id):
        #        course=None
        #        break
