-- 1.	Revisa las tablas Customers (clientes), Employees (empleados) y Orders (pedidos)
select * from customers; select * from employees; select * from orders;

-- 2.	¿Cuántos clientes hay registrados?
select count(customer_id) from customers;

--3.	¿Cuántos pedidos?
select count(order_id) from Orders;

-- 4.	¿Qué clientes viven en Londes y su nombre (CustomerName) empieza por A?
select contact_name from customers where city = 'London' AND lower(contact_name) similar to 'a%';

-- 5.	¿Cuántos clientes hay que son de Londres?
select count(customer_id) from customers where city = 'London';

-- 6.	¿Cuántos clientes hay en cada ciudad?
select city, count(customer_id) from customers group by city;

-- 7.	¿Cuántos empleados nacieron después de 1 de Junio del 1965?
select * from employees where birth_date > '1965-06-01';

-- 8.	Hazme un informe que diga «El empleado N nación el N», siendo N, nombre (FirstName y Last Name) y día de nacimiento (BirthDate)

create or replace procedure getEmployeeData (empl_id integer)
language plpgsql
as $$
	declare 
		emp_name employees.first_name%type;
		emp_lastName employees.last_name%type;
		emp_birthDate employees.birth_date%type;
	begin
		select first_name,last_name,birth_date into emp_name, emp_lastName, emp_birthDate from employees where employee_id = empl_id;

	raise notice 'El empleado ,%,%, nació el, %', emp_name, emp_lastName, emp_birthDate;
end
$$;

-- call getEmployeeData(8);

-- 9.	Hazme el informe anterior, pero sólo para los empleados con id 8, 7, 3 y 10
-- drop procedure getSomeEmpData;

create or replace procedure getSomeEmpData (emp_array INTEGER[])
language plpgsql
as $$
	declare	
		emp_name employees.first_name%type;
		emp_lastName employees.last_name%type;
		emp_birthDate employees.birth_date%type;
	begin
		for i in 1 .. array_length(emp_array,1)
		loop
			select first_name,last_name,birth_date 
			into emp_name, emp_lastName, emp_birthDate 
			from employees 
			where employee_id = emp_array[i];

			IF emp_name IS NULL THEN
				RAISE NOTICE 'El empleado con id % no existe', emp_array[i];
			ELSE 
				raise notice 'El empleado ,%,%, nació el, %', emp_name, emp_lastName, emp_birthDate;
			END IF;
		end loop;
	end;
$$;
	
CALL getSomeEmpData(ARRAY[8,7,3,10]);

-- 10.	Dime los paises que tengan más de 5 clientes, ordenados por el nombre de país

select country, count(customer_id) from customers group by country having count(country) > 5 order by country;

-------- Ejercicios con más de una tabla -------- 
-- 1.	Dime el nombre del cliente del pedido 10360

SELECT customers.contact_name
FROM customers
INNER JOIN orders ON customers.customer_id = orders.customer_id
where order_id = 10360;

-- 2.	Dime el nombre completo de los clientes con los pedidos 10360, 10253 y 10440

SELECT customers.contact_name
FROM customers
INNER JOIN orders ON customers.customer_id = orders.customer_id
WHERE orders.order_id IN (10360, 10361, 10362);


-- 3.	Dime las ciudades y número de pedidos de clientes en esa ciudad
select ship_city, count(order_id)
from orders
inner join customers on orders.customer_id = customers.customer_id
group by ship_city;

--4.	¿Cuales son las ciudades desde las que hay más de 7 pedidos?

select ship_city, count(order_id)
from orders
inner join customers on orders.customer_id = customers.customer_id
group by ship_city
having count(order_id) > 7;

--5.	¿Cuales son los tres países desde los que tengo más pedidos?
select ship_city, count(order_id) as order_count
from orders
inner join customers on orders.customer_id = customers.customer_id
group by ship_city
order by order_count desc
limit 3;


-- 6.	Necesito un informe con el Nombre completo de los Empleados y el número de pedidos que registraron
select * from orders; select * from employees;

CREATE OR REPLACE PROCEDURE getEmpOrders()
LANGUAGE plpgsql
AS $$
DECLARE
    emp_name employees.first_name%TYPE;
    emp_lastname employees.last_name%TYPE;
    emp_orders INTEGER;
    r_employee RECORD;
BEGIN
    FOR r_employee IN 
        SELECT 
            e.first_name,
            e.last_name,
            COUNT(DISTINCT o.order_id) as total_orders
        FROM employees e
        LEFT JOIN orders o ON e.employee_id = o.employee_id
        GROUP BY e.first_name, e.last_name, e.employee_id
    LOOP
        emp_name := r_employee.first_name;
        emp_lastname := r_employee.last_name;
        emp_orders := r_employee.total_orders;
        
        RAISE NOTICE 'El empleado % % ha registrado %, pedidos.',
            emp_name, 
            emp_lastname, 
            emp_orders;
    END LOOP;
END;
$$;
CALL getEmpOrders();

-- 7.	En el informe anterior, sólo necesito los empleados cuyo nombre comience por M


lower(contact_name) similar to 'a%';
        
CREATE OR REPLACE PROCEDURE getEmpOrdersByM()
LANGUAGE plpgsql
AS $$
DECLARE
    emp_name employees.first_name%TYPE;
    emp_lastname employees.last_name%TYPE;
    emp_orders INTEGER;
    r_employee RECORD;
BEGIN
    FOR r_employee IN 
        SELECT 
            e.first_name,
            e.last_name,
            COUNT(DISTINCT o.order_id) as total_orders
        FROM employees e
        LEFT JOIN orders o ON e.employee_id = o.employee_id
        GROUP BY e.first_name, e.last_name, e.employee_id
		HAVING lower(e.first_name) similar to 'm%'
    LOOP
        emp_name := r_employee.first_name;
        emp_lastname := r_employee.last_name;
        emp_orders := r_employee.total_orders;
        
        RAISE NOTICE 'El empleado % % ha registrado %, pedidos.',
            emp_name, 
            emp_lastname, 
            emp_orders;
    END LOOP;
END;
$$;
CALL getEmpOrdersByM();

-- 8.	Quiero saber el número de pedido, qué empleado (sólo el nombre) lo registró y el cliente.

SELECT 
	    e.first_name AS "Nombre Empleado",
	    o.order_id AS "Número de pedido",
	    c.*
	FROM customers c
	INNER JOIN orders o ON c.customer_id = o.customer_id
	INNER JOIN employees e ON o.employee_id = e.employee_id;

-- 9.	¿Hay algún cliente que haya hecho más de un pedido registrado por el mismo empleado?

SELECT 
	c.contact_name,
    c.customer_id AS "ID Cliente",
    COUNT(*) AS "Número de pedidos"
FROM customers c
INNER JOIN orders o ON c.customer_id = o.customer_id
INNER JOIN employees e ON o.employee_id = e.employee_id
GROUP BY c.customer_id
HAVING COUNT(*) > 1
ORDER by "Número de pedidos" DESC;

-- 10.	Quiero saber los clientes que hayan hecho más de un pedido y que hayan sido registrado por un Empleado cuyo nombre sea Margaret.
SELECT 
	e.first_name,
    c.customer_id AS "ID Cliente",
    COUNT(*) AS "Número de pedidos"
FROM customers c
INNER JOIN orders o ON c.customer_id = o.customer_id
INNER JOIN employees e ON o.employee_id = e.employee_id
GROUP BY c.customer_id, e.first_name
HAVING COUNT(*) > 1 and e.first_name = 'Margaret'
ORDER by "Número de pedidos" DESC;

select * from customers order by contact_name;

-------- Ejercicios con Subconsultas -------- 
-- 1.	¿Cuál es el producto con el precio mínimo más bajo? (usando subconsultas)
select * from products where unit_price in (select MIN(unit_price) from products);

-- 2.	¿Cuál es el producto cuyo precio sea al menos 10 veces el pedido mínimo (quantity) de los pedidos (OrderDetails)?
select * from products where unit_price in (select MIN(unit_price)*10  from products);

-- 3.	¿Cuáles son los registros de productos (Products) cuyo precio (price) sea mayor que el máximo de los precios de los productos cuyo id sea 3, 6, 9 y 10?
select * from products where unit_price >( SELECT MAX(unit_price) FROM products 
WHERE product_id IN (3, 6, 9, 10));

-- 4.	¿Cuáles son los registros de productos (Products) cuyo ProductID sea un valor que esté en Shippers?ShipperID?
SELECT * FROM products WHERE product_id IN (SELECT shipper_id FROM shippers);

-- 5.	¿Qué clientes (Customers) tenemos registrados, que estén en ciudades de nuestros proveedores (Suppliers)?
select * from customers where city in (select city from suppliers);

-- 6.	Seleccionar el nombre de la compañía del cliente, nombre del
-- contacto, el código de la orden de compra, la fecha de la orden de
-- compra, el código del producto,cantidad pedida del producto, nombre
-- del producto y el nombre de la compañía proveedora, usas
-- JOIN.Solamente las compañías proveedoras que comienzan con la
-- letra de la A hasta la letra G, además la cantidad pedida del producto
-- debe estar entre 23 y 187.

select company_name, contact_name,  from suppliers; select * from orders;
