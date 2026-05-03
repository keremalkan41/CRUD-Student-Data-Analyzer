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