Write a script that lists all databases of your MySQL server.

Write a script that creates the database hbtn_0c_0 in your MySQL server.

Write a script that deletes the database hbtn_0c_0 in your MySQL server.

Write a script that lists all the tables of a database in your MySQL server.

Write a script that creates a table called first_table in the current database in your MySQL server.

Write a script that prints the full description of the table first_table from the database hbtn_0c_0 in your MySQL server.

Write a script that lists all rows of the table first_table from the database hbtn_0c_0 in your MySQL server.

Write a script that inserts a new row in the table first_table (database hbtn_0c_0) in your MySQL server.

New row:
id = 89
name = Best School
The database name will be passed as an argument of the mysql command

Write a script that displays the number of records with id = 89 in the table first_table of the database hbtn_0c_0 in your MySQL server.

Write a script that creates a table second_table in the database hbtn_0c_0 in your MySQL server and add multiples rows.

second_table description:
id INT
name VARCHAR(256)
score INT
The database name will be passed as an argument to the mysql command
If the table second_table already exists, your script should not fail
You are not allowed to use the SELECT and SHOW statements
Your script should create these records:
id = 1, name = “John”, score = 10
id = 2, name = “Alex”, score = 3
id = 3, name = “Bob”, score = 14
id = 4, name = “George”, score = 8

Write a script that lists all records of the table second_table of the database hbtn_0c_0 in your MySQL server.

Write a script that lists all records with a score >= 10 in the table second_table of the database hbtn_0c_0 in your MySQL server.

Write a script that updates the score of Bob to 10 in the table second_table

Write a script that removes all records with a score <= 5 in the table second_table of the database hbtn_0c_0 in your MySQL server.

Write a script that computes the score average of all records in the table second_table of the database hbtn_0c_0 in your MySQL server.
The result column name should be average

Write a script that lists the number of records with the same score in the table second_table of the database hbtn_0c_0 in your MySQL server.

The result should display:
the score
the number of records for this score with the label number
The list should be sorted by the number of records (descending)

Write a script that lists all records of the table second_table of the database hbtn_0c_0 in your MySQL server.
Don’t list rows without a name value
