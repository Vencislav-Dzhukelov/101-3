select *
from Employees

select FirstName, LastName, Title
from Employees

select *
from Employees
where city =  'Seattle'

select *
from Employees
where city =  'London'

select *
from Employees
where title like '% Sales %' and (titleofcourtesy = 'Ms.' or titleofcourtesy = 'Mrs.')

select *
from Employees
order by birthdate
limit 5

select *
from Employees
order by hiredate
limit 5

select *
from Employees
where reportsto is null

select a.firstname, a.lastname, b.firstname, b.lastname
from employees a, employees b
where b.employeeid = a.reportsto

select count(*)  number
from employees
where titleofcourtesy = 'Ms.' or titleofcourtesy = 'Mrs.'

select count(*)  number
from employees
where titleofcourtesy != 'Ms.' and titleofcourtesy != 'Mrs.'

select city, count(*)
from employees
group by city

select orderid, firstname, lastname
from employees e, orders o
where o.employeeid = e.employeeid

select e.orderid, s.companyname
from orders e , shippers s
where s.shipperid = e.shipvia

select country, count(*)
from customers c join orders o on c.customerid = o.customerid
group by country

select firstname, lastname, count(orderid)
from employees e join orders o on o.employeeid = e.employeeid
group by firstname, lastname
order by count(orderid) desc
limit 1

select contactname, count (orderid)
from customers c join orders o on c.customerid = o.customerid
group by contactname
order by count(orderid) desc
limit 1
