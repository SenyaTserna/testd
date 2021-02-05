SELECT max(t.CREATED_ON) as date, c.ID, t.AMOUNT FROM code as c JOIN transact as t on c.ID = t.CODE_ID GROUP BY c.ID;
