select p.firstName,p.lastName,a.city,a.state  From person p left join Address a on p.personid=a.personid  ;
