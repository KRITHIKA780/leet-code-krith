SELECT email as Email
FROM Person
group by email
HAVING COUNT(email) > 1;