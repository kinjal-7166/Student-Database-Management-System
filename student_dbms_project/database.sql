
CREATE DATABASE student_dbms;
USE student_dbms;

CREATE TABLE students(
student_id INT AUTO_INCREMENT PRIMARY KEY,
name VARCHAR(100),
email VARCHAR(100),
phone VARCHAR(15),
address VARCHAR(200),
course VARCHAR(100),
admission_year INT
);

CREATE TABLE attendance(
attendance_id INT AUTO_INCREMENT PRIMARY KEY,
student_id INT,
percentage INT,
FOREIGN KEY(student_id) REFERENCES students(student_id)
);

CREATE TABLE results(
result_id INT AUTO_INCREMENT PRIMARY KEY,
student_id INT,
subject VARCHAR(100),
marks INT,
grade VARCHAR(5),
FOREIGN KEY(student_id) REFERENCES students(student_id)
);

CREATE TABLE fees(
fee_id INT AUTO_INCREMENT PRIMARY KEY,
student_id INT,
amount INT,
status VARCHAR(20),
payment_date DATE,
FOREIGN KEY(student_id) REFERENCES students(student_id)
);
