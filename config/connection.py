import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    port = 3306,
    password="wellk4mp",
    auth_plugin='mysql_native_password',
    database='adonis_metrics'
)


def get_connection():
    return db