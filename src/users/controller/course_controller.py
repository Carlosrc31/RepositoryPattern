from flask import Blueprint, jsonify, request
from users.model.course_model import Course
from users.repository.courses_memory import CourseRepo

blueprint = Blueprint('course_controller', __name__)
courseRepo = CourseRepo()

#Endpoint to add Courses
@blueprint.route('/courses', methods=['POST'])
def insert_course():
    #Get the course data from the requesr
    course_data = request.get_json()

    #Creating the object
    course = Course(
        id = len(courseRepo.courses) + 1,
        name=course_data['name'],
        description=course_data['description']
    )

    #Adding a course to the array
    exists = courseRepo.add(course)
    
    #If the course not exists sends message
    if exists is False:
        return jsonify({'message': 'This course already exists'}), 404

    #Else sends the array with the courses
    return jsonify(exists)
    
   

#Endpoint to retrieve the course which match with course_id
@blueprint.route('/courses/<course_id>', methods=["GET"])
def get_course(course_id):
    
    course = courseRepo.get(course_id)

    if course is None:
        return jsonify({"message": "Curso no encontrado"}), 404
    
    return jsonify(course)
    

    

