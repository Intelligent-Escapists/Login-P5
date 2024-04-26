CREATE DATABASE mercaditApp;
-- Descomentar la siguiente linea si el usuario no se ha creado
-- create user 'lab'@'localhost' identified by 'Developer123!'

GRANT ALL PRIVILEGES ON mercaditApp.* to 'lab'@'localhost' WITH GRANT OPTION;

USE mercaditApp;

CREATE TABLE usuario (
	id_usuario INT NOT NULL AUTO_INCREMENT,
    correo VARCHAR(345) NOT NULL,
    password VARCHAR(64) NOT NULL,
    PRIMARY KEY (id_usuario),
    UNIQUE KEY correo (correo)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

SELECT * FROM usuario;
DELETE FROM usuario WHERE id_usuario = 3;