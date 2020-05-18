import mysql.connector
from mysql.connector import Error


def create_connection(host_name, user_name, user_password):
    connect = None
    try:
        connect = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password
        )
        print("Connection to MySQL DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")

    return connect



connection = create_connection("music-web.mysql.database.azure.com", "DataAdmin@music-web", "Kriegel2021")

#mycursor.execute("CREATE DATABASE whyisthisnotworking")
