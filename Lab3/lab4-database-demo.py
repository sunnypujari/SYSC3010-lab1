#!usr/bin/env python3
import sqlite3
dbconnect =sqlite3.connect("mydatabase.db");
dbconnect.row_factory = sqlite3.Row;
cursor = dbconnect.cursor();
cursor.execute('''insert into temp value (2020-10-08,07:40:51,"kitchen",20.1)''');
dbconnect.commit();
cursor.execute('SELECT*FROM temps WHERE zone="kitchen"');
for row in cursor:
	print(row['tdate'],row['ttime'],row['zone'],row['temperature']);
dbconnect.close();
