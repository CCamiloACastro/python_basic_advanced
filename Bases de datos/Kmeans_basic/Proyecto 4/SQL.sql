CREATE DATABASE Proyecto4 CHARACTER SET utf8mb4 COLLATE utf8mb4_spanish_ci;

use Proyecto4;

#Crear tablas

DROP table Datos;

#Crear tabla "Datos"

CREATE TABLE Datos(
	ID INT PRIMARY KEY auto_increment,
    Nombre VARCHAR(50),
    Archivo longtext
);

SELECT * FROM Datos;

UPDATE Datos
SET Nombre = 'Seleccionar'
WHERE ID =2;

INSERT INTO Datos (Nombre) VALUES ('Seleccionar');

DELETE FROM Datos 
WHERE ID !=1