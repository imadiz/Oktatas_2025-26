-- DB schema
CREATE DATABASE Bolt
CHARACTER SET utf8mb4
COLLATE utf8mb4_hungarian_ci;


CREATE TABLE Products (
	ID int,
    Name varchar(255),
	Kcal int,
    Price int,
    Restricted bool
);

CREATE TABLE Employees(
	ID int,
    Name varchar(255),
    Wage int,
    Position varchar(255),
    Password text
);
-- Teszt felhasználó hozzáadása
INSERT INTO Employees(
    Employees.ID,
    Employees.Name,
    Employees.Wage,
    Employees.Position
    Employees.Password
)
VALUES(
    1,
    "Test Thomas",
    1500,
    "TestPos",
    "14f8f4bb8c0e79a02670a5fea5682da717a5b3d3dc7b1706f7a4bab9afae18c2"
);