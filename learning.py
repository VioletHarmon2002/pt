import mysql.connector
import mysql.connector

connection = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='people',
         user='dbuser',
         password='pAs5w_0rD',
         autocommit=True
         )