/*
Enter your query below.
Please append a semicolon ";" at the end of the query
*/
select accounts.username, 
        accounts.email, 
        count(*), 
        sum(items.weight) 
    from accounts_items
    join accounts
    on account_id = accounts.id
    join items
    on item_id = items.id
    group by accounts.username, accounts.email
    having sum(items.weight) > 20
    order by sum(items.weight) desc, username asc;
