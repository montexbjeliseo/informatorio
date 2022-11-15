/*
De la tabla de pedidos, el gasto de envío promedio 
y el máximo gasto de envío.*/

SELECT AVG(Freight) AS 'Promedio', MAX(Freight) as 'Maximo' FROM Orders;