/*Listar  apellidos y nombres de Profesores mayores a 40 años en la Universidad.*/

SELECT nombre as 'Nombre', apellido1 as 'Apellido 1', apellido2 as 'Apellido 2' 
FROM persona WHERE id IN (SELECT id_profesor from profesor) AND DATEDIFF(YEAR, fecha_nacimiento, GETDATE()) > 40;