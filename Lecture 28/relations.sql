-- CREATE TABLE users(
-- 	user_id SERIAL PRIMARY KEY,
-- 	name VARCHAR(100),
-- 	username VARCHAR(20) UNIQUE NOT NULL
-- );

-- INSERT INTO users(name, username) VALUES 
-- 	('Otar Tumanishvili', 'tumana'),
-- 	('Merab Todua', 'merab123'),
-- 	('Ilia Goginashvili', 'ilia777'),
-- 	('Giorgi Tavlalashvili', 'giorgi123'),
-- 	('Mamuka Gobejishvili', 'mamuka'),
-- 	('Giorgi Petuashvili', 'giorgipet');

-- CREATE TABLE profiles (
-- 	profile_id SERIAL PRIMARY KEY,
-- 	user_id INT REFERENCES users(user_id) ON DELETE CASCADE UNIQUE,
-- 	bio TEXT
-- );

-- INSERT INTO profiles(user_id, bio) VALUES
-- 	(3, 'Ilia is good student'),
-- 	(4, 'Giorgi is also good student');


-- SELECT name, username, bio FROM users u
-- JOIN profiles p ON u.user_id = p.user_id;


-- CREATE TABLE students(
-- 	student_id SERIAL PRIMARY KEY,
-- 	name VARCHAR(50),
-- 	email VARCHAR(50) UNIQUE,
-- 	is_active BOOLEAN DEFAULT TRUE
-- );

-- CREATE TABLE lecturers(
-- 	lecturer_id SERIAL PRIMARY KEY,
-- 	name VARCHAR(50),
-- 	salary INT
-- );

-- CREATE TABLE courses(
-- 	course_id SERIAL PRIMARY KEY,
-- 	title VARCHAR(30) UNIQUE NOT NULL,
-- 	lecturer_id INT REFERENCES lecturers(lecturer_id) ON DELETE SET NULL
-- );


-- CREATE TABLE enrollments (
-- 	enrollment_id SERIAL PRIMARY KEY,
-- 	student_id INT REFERENCES students(student_id) ON DELETE CASCADE,
-- 	course_id INT REFERENCES courses(course_id) ON DELETE CASCADE,
-- 	enrollment_date DATE DEFAULT CURRENT_DATE
-- );


-- INSERT INTO lecturers(name, salary) VALUES
-- 	('Otar Tumanishvili', 200),
-- 	('Merab Todua', 300);


-- INSERT INTO courses(title, lecturer_id) VALUES
-- 	('Python', 2),
-- 	('Java', 2),
-- 	('C++', 1);


-- INSERT INTO students(name, email) VALUES
-- 	('Giorgi Petuashvili', 'giorgi123@gmail.com'),
-- 	('Ilia Goginashvili', 'giordgi123@gmail.com'),
-- 	('Giorgi Tavlalashvili', 'giorghi123@gmail.com'),
-- 	('Davit Ashchiani', 'giorgsgi123@gmail.com'),
-- 	('Mamuka Gobejishvili', 'gfiorgi123@gmail.com');


-- INSERT INTO enrollments(student_id, course_id) VALUES
-- 	(6, 1),
-- 	(6, 3),
-- 	(9, 2),
-- 	(7, 2),
-- 	(7, 1),
-- 	(8, 1),
-- 	(10, 3);


-- SELECT s.name, title AS course_title, l.name, enrollment_date FROM enrollments e
-- JOIN students s ON s.student_id = e.student_id
-- JOIN courses c ON c.course_id = e.course_id
-- JOIN lecturers l ON c.lecturer_id = l.lecturer_id;





