### SQLite

1. SQlite is small, lite, and realiable.
2. It has one database file which is store in pc.
3. Multiple read at a time. Single read at a time.
4. http://sqlitebrowser.org
5. The following is the simple example of SQLite in python 
```
import sqlite3
connection = sqlite3.connect('data.db')
cursor = connection.cursor()

cursor.execute('YOUR SQL query')
connection.commit()

connection.close()
```