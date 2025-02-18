from models import session, Course, Student

# course = Course(name='Python Programming')
#
# session.add(course)
# session.commit()

# course = Course(name='Java Programming')
# course2 = Course(name='C++ Programming')
#
# session.add_all([course, course2])
# session.commit()



# student1 = Student(first_name="John", last_name="Smith", course_id=1)
# student2 = Student(first_name="Walter", last_name="White", course_id=2)
# student3 = Student(first_name="Bob", last_name="Uolsh", course_id=2)
# student4 = Student(first_name="George", last_name="Washington", course_id=1)
# student5 = Student(first_name="Walter", last_name="Johnson", course_id=3)
# student6 = Student(first_name="Charlie", last_name="Brown", course_id=1)
#
# students = [student2, student3, student4, student5, student6]
#
# session.add_all(students)
# session.commit()

# students = session.query(Student).all()
#
# print(students)

# courses = session.query(Course).all()
#
# for course in courses:
#     print(course.name)

# student1 = session.query(Student).first()
#
# print(student1.first_name)

# students = session.query(Student).filter(Student.first_name == 'Walter').all()
#
# for student in students:
#     print(student.first_name, student.last_name)

# students = session.query(Student).filter_by(first_name='Walter').all()
#
# for student in students:
#     print(student.first_name, student.last_name)

# students = session.query(Student).filter(Student.student_id > 3).all()
#
# for student in students:
#     print(student.first_name, student.last_name)


# student = session.query(Student).filter_by(first_name='John').first()
#
# if student:
#     student.first_name = 'Giorgi'
#     session.commit()

# session.query(Student).filter_by(first_name='Walter').update({"last_name": "updated"})
# session.commit()

# session.query(Student).filter_by().update({"last_name": "updated"})
# session.commit()

# student = session.query(Student).filter_by(first_name='Bob').first()
#
# if student:
#     session.delete(student)
#     session.commit()

# session.query(Student).filter_by().delete()
# session.commit()












