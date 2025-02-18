CREATE TABLE students (
	student_id serial PRIMARY KEY,
	first_name varchar(30) NOT NULL,
	last_name varchar(30) NOT NULL,
	is_active boolean DEFAULT True,
	age integer,
	pay numeric(6, 2),
	review text,
	email varchar(30) UNIQUE,
	registered date DEFAULT CURRENT_DATE
);

INSERT INTO students (first_name, last_name, age, email) VALUES
('Otar', 'tumanishvili', 33, 'taests@gmail.com'),
('Levan', 'tumanishvili', 25, 'tessts@gmail.com'),
('ANANO', 'tumanishvili', 63, 'testsa@gmail.com'),
('Otar', 'tumanishvili', 33, 'tesfts@gmail.com'),
('NITA', 'tumanishvili', 20, 'testfs@gmail.com'),
('Otar', 'tumanishvili', 33, 'testjs@gmail.com'),
('Alex', 'tumanishvili', 33, 'teslts@gmail.com');

UPDATE students SET pay = 2250;
UPDATE students SET pay = pay * 1.1;

UPDATE students SET pay = pay / 1.1 WHERE age < 30;

UPDATE students SET first_name = UPPER(first_name) RETURNING *;

UPDATE students SET first_name = LOWER(first_name) RETURNING *;

UPDATE students SET first_name = INITCAP(first_name), last_name = INITCAP(last_name) RETURNING *;

UPDATE students SET is_active = False WHERE student_id % 2 = 0 RETURNING *;

UPDATE students SET email = email || '.ge' RETURNING *;

UPDATE students SET email = REPLACE(email, '.ge', '.com') RETURNING *;

ALTER table students ADD COLUMN subject varchar(20);

ALTER table students DROP COLUMN review;

ALTER TABLE students RENAME COLUMN age to asaki;

ALTER TABLE students ALTER COLUMN asaki TYPE integer;

CREATE TABLE programs (
	program_id SERIAL PRIMARY KEY,
	title VARCHAR(30),
	code VARCHAR(10)
);

INSERT INTO programs (title, code) VALUES 
	('Front-End', 'FE001'),
	('Back-End', 'BE001'),
	('DevOps', 'DO001');

CREATE TABLE lecturers (
	lecturer_id SERIAL PRIMARY KEY,
	name VARCHAR(50) UNIQUE,
	hired DATE DEFAULT CURRENT_DATE
);

INSERT INTO lecturers (name) VALUES 
	('Otar Tumanishvili'),
	('Alex Kakauridze'),
	('Ani Mamaladze'),
	('Leqso Kiknadze');

CREATE TABLE courses (
	course_id SERIAL PRIMARY KEY,
	title VARCHAR(30) UNIQUE,
	pay NUMERIC(6, 2) CHECK(pay > 0),
	lecturer_id INTEGER REFERENCES lecturers(lecturer_id) ON DELETE CASCADE,
	program_id INTEGER REFERENCES programs(program_id) ON DELETE SET NULL
);

INSERT INTO courses (title, pay, lecturer_id, program_id) VALUES
	('Python', 1500, 1, 2),
	('HTML-CSS', 800, 1, 1),
	('Docker', 1000, 2, 3),
	('C++', 1200, 1, 2),
	('Angular', 2000, 3, 1);

CREATE TABLE students (
	student_id SERIAL PRIMARY KEY,
	first_name VARCHAR(30),
	last_name VARCHAR(30),
	course_id INTEGER REFERENCES courses(course_id) ON DELETE SET NULL
);

INSERT INTO students (first_name, last_name, course_id) VALUES
	('Nino', 'Machabeli', 2),
	('Nita', 'Glonti', 1),
	('Irakli', 'Sivsivadze', 3),
	('Levan', 'Mdinaradze', 1);




