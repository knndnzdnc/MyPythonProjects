import mysql.connector


connection = mysql.connector.connect(host ="localhost",user= "root", password = "12345", database= "users")
cursor = connection.cursor()