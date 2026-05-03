CREATE DATABASE students;
GO

USE students;
GO

CREATE TABLE studentsinfo (
    id INT PRIMARY KEY,              
    fullname NVARCHAR(100),
    department NVARCHAR(100),
    numberstudent BIGINT,                   
    class NVARCHAR(50),              
    gpa FLOAT                        
);
GO

SELECT * FROM studentsinfo;
GO

USE students;
GO

INSERT INTO studentsinfo (id, fullname, department, numberstudent, [class], gpa) VALUES
(101, 'Liam Smith', 'Computer Science', 2024001, 'Freshman', 3.85),
(102, 'Emma Johnson', 'Electrical Engineering', 2024002, 'Sophomore', 3.42),
(103, 'Noah Williams', 'Mechanical Engineering', 2024003, 'Junior', 2.95),
(104, 'Olivia Brown', 'Civil Engineering', 2024004, 'Senior', 3.15),
(105, 'William Jones', 'Computer Science', 2024005, 'Freshman', 3.92),
(106, 'Sophia Garcia', 'Mathematics', 2024006, 'Sophomore', 3.78),
(107, 'James Miller', 'Physics', 2024007, 'Junior', 3.55),
(108, 'Isabella Davis', 'Software Engineering', 2024008, 'Senior', 3.68),
(109, 'Benjamin Rodriguez', 'Software Engineering', 2024009, 'Freshman', 2.80),
(110, 'Mia Martinez', 'Economics', 2024010, 'Sophomore', 3.30),
(111, 'Lucas Hernandez', 'Computer Science', 2024011, 'Junior', 3.95),
(112, 'Charlotte Lopez', 'Biology', 2024012, 'Senior', 3.22),
(113, 'Theodore Gonzalez', 'Mechanical Engineering', 2024013, 'Freshman', 2.50),
(114, 'Amelia Wilson', 'Electrical Engineering', 2024014, 'Sophomore', 3.88),
(115, 'Henry Anderson', 'Mathematics', 2024015, 'Junior', 3.60),
(116, 'Evelyn Thomas', 'Physics', 2024016, 'Senior', 3.45),
(117, 'Sebastian Taylor', 'Civil Engineering', 2024017, 'Freshman', 3.10),
(118, 'Abigail Moore', 'Computer Science', 2024018, 'Sophomore', 2.75),
(119, 'Jack Jackson', 'Economics', 2024019, 'Junior', 3.90),
(120, 'Harper Martin', 'Software Engineering', 2024020, 'Senior', 3.52),
(121, 'Alexander Lee', 'Biology', 2024021, 'Freshman', 3.35),
(122, 'Emily Perez', 'Mechanical Engineering', 2024022, 'Sophomore', 3.18),
(123, 'Daniel Thompson', 'Computer Science', 2024023, 'Junior', 3.70),
(124, 'Madison White', 'Electrical Engineering', 2024024, 'Senior', 2.90),
(125, 'Matthew Harris', 'Mathematics', 2024025, 'Freshman', 3.40),
(126, 'Scarlett Sanchez', 'Software Engineering', 2024026, 'Sophomore', 3.98),
(127, 'Samuel Clark', 'Civil Engineering', 2024027, 'Junior', 3.25),
(128, 'Victoria Ramirez', 'Physics', 2024028, 'Senior', 3.05),
(129, 'Joseph Lewis', 'Computer Science', 2024029, 'Freshman', 3.62),
(130, 'Aria Robinson', 'Biology', 2024030, 'Sophomore', 3.48),
(131, 'David Walker', 'Mechanical Engineering', 2024031, 'Junior', 2.65),
(132, 'Grace Young', 'Economics', 2024032, 'Senior', 3.75),
(133, 'Wyatt Allen', 'Software Engineering', 2024033, 'Freshman', 3.82),
(134, 'Chloe King', 'Electrical Engineering', 2024034, 'Sophomore', 3.12),
(135, 'Carter Wright', 'Mathematics', 2024035, 'Junior', 3.58),
(136, 'Zoey Scott', 'Physics', 2024036, 'Senior', 2.98),
(137, 'Owen Torres', 'Civil Engineering', 2024037, 'Freshman', 3.28),
(138, 'Penelope Nguyen', 'Computer Science', 2024038, 'Sophomore', 3.86),
(139, 'John Hill', 'Biology', 2024039, 'Junior', 3.42),
(140, 'Layla Flores', 'Software Engineering', 2024040, 'Senior', 3.91),
(141, 'Luke Green', 'Mechanical Engineering', 2024041, 'Freshman', 2.70),
(142, 'Riley Adams', 'Economics', 2024042, 'Sophomore', 3.33),
(143, 'Gabriel Nelson', 'Electrical Engineering', 2024043, 'Junior', 3.64),
(144, 'Nora Baker', 'Mathematics', 2024044, 'Senior', 3.50),
(145, 'Isaac Hall', 'Computer Science', 2024045, 'Freshman', 3.02),
(146, 'Lily Rivera', 'Physics', 2024046, 'Sophomore', 3.72),
(147, 'Anthony Campbell', 'Civil Engineering', 2024047, 'Junior', 3.14),
(148, 'Mila Mitchell', 'Biology', 2024048, 'Senior', 3.80),
(149, 'Dylan Carter', 'Software Engineering', 2024049, 'Freshman', 3.56),
(150, 'Elena Roberts', 'Mathematics', 2024050, 'Sophomore', 3.39);
GO