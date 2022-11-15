/*Listar apellidos y nombre de las Personas, convirtiendo ambos elementos a mayúsculas*/

SELECT UPPER(nombre) as 'Nombre', UPPER(apellido1) as 'Apellido 1', UPPER(apellido2) as 'Apellido 2' FROM persona;