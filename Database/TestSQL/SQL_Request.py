import mysql.connector
from mysql.connector import Error


def create_connection(host_name, user_name, user_password, database):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
            database=database
        )
        print("Connection to MySQL DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")

    return connection


connection = create_connection("music-web.mysql.database.azure.com", "DataAdmin@music-web", "Kriegel2021", "testdatabaseandy")

mycursor = connection.cursor()

mycursor.execute("CREATE DATABASE whyisthisnotworking")

#mycursor.execute("CREATE TABLE testtable (name VARCHAR(255), address VARCHAR(255))")

#mycursor.execute("SHOW TABLES")

mycursor.execute("SHOW DATABASES")

for x in mycursor:
    print(x)

