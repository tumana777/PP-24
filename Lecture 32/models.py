from password.password import PASSWORD
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker, declarative_base

Base = declarative_base()

HOST = 'localhost'
PORT = 5432
DATABASE = 'students'
USER = 'postgres'
PASSWORD = PASSWORD

engine = create_engine(f"postgresql+psycopg2://{USER}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}")

class Course(Base):
    __tablename__ = 'course'

    course_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(20), unique=True, nullable=False)

class Student(Base):
    __tablename__ = 'student'

    student_id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String(20))
    last_name = Column(String(20))
    course_id = Column(Integer, ForeignKey('course.course_id', ondelete='CASCADE'))

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()