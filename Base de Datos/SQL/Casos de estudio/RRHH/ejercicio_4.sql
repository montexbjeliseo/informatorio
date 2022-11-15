/* Listar la cantidad de personas de la tabla EMPLOYEES, 
que tengan el cargo de Programador. 
Y cuantas de estas personas superen el sueldo mínimo en esa categoría. */

SELECT empleado.nombre FROM empleado 
WHERE empleado.idcar = (SELECT idcar FROM car WHERE car.nombre = 'Programador');