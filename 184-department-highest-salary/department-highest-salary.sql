
select d.name as department, e.name as employee, e.salary
From employee e
join department d
on d.id = e.departmentid
where (e.departmentid, e.salary) IN 
    (select departmentid, MAX(salary)
    From employee
    GROUP BY departmentid)