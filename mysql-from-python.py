import os
import datetime
import pymysql

username = "root"

# Connect to the database
connection = pymysql.connect(host='localhost',
                             user=username,
                             password='',
                             db='Chinook')

try:
    # Run a query
    with connection.cursor() as cursor:
        list_of_names = ['John','Stephen']
        #Prepare a string with the same number of placeholders as the variable above
        format_strings = ','.join(['%s']*len(list_of_names))
        cursor.execute("DELETE FROM Friends WHERE name IN ({});".format(format_strings), list_of_names)
        connection.commit()    
    
    #with connection.cursor() as cursor:
    #    names = ['John','Stephen']
    #    cursor.execute("DELETE FROM Friends WHERE name IN (%s,%s)", names)
    #    print(rows)
    #    connection.commit()    
    
    #with connection.cursor() as cursor:
    #    rows = cursor.executemany("DELETE FROM Friends WHERE name = %s;",['Dave','Stephen','John'])
    #    print(rows)
    #    connection.commit()

    #with connection.cursor() as cursor:
    #     rows = cursor.execute("DELETE FROM Friends WHERE name = %s;",'Dave')
    #     print(rows)
    #     connection.commit()

    #with connection.cursor() as cursor:
    #    rows = cursor.execute("DELETE FROM Friends WHERE name = 'Fred';")
    #    print(rows)
    #    connection.commit()

    #with connection.cursor() as cursor:
    #    rows = [(21, 'John'),
    #            (22, 'Fred'),
    #            (23, 'Dave')]
    #    cursor.executemany("UPDATE Friends SET age = %s WHERE name = %s;",
    #                    rows)
    #    connection.commit()

    #with connection.cursor() as cursor:
    #    cursor.execute("UPDATE Friends SET age = %s WHERE name = %s;",
    #                    (56,'John'))
    #    connection.commit()

    #with connection.cursor() as cursor:
    #    cursor.execute("UPDATE Friends SET age = 21 WHERE name = 'John';")
    #    connection.commit()
    
    #with connection.cursor() as cursor:
    #    rows = [("Fred", 56, "1963-11-28 15:47:00"),
    #            ("Dave", 56, "1963-11-28 15:47:00"),
    #            ("Stephen", 56, "1963-11-28 15:47:00"),
    #            ("John", 56, "1963-11-28 15:47:00")]
    #    cursor.executemany("INSERT INTO Friends VALUES (%s,%s,%s);", rows)
    #    print(rows)
    #    connection.commit()
    
    #with connection.cursor() as cursor:
    #    row = ("John", 56, "1963-11-28 15:47:00")
    #    cursor.execute("INSERT INTO Friends VALUES (%s,%s,%s);", row)
    #    connection.commit()

    #with connection.cursor() as cursor:
    #    cursor.execute("""CREATE TABLE IF NOT EXISTS
    #                    Friends(name char(20),age int,DOB datetime);""")

    #with connection.cursor(pymysql.cursors.DictCursor) as cursor:
    #    sql = "SELECT * FROM Genre;"
    #    cursor.execute(sql)
    #    for row in cursor:
    #        print(row)
        
        #result = cursor.fetchall()
        #print(result)
finally:
    # Close the connection, regardless of whether or not the above was successful
    connection.close()