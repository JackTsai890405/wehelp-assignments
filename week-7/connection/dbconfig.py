import mysql.connector
from mysql.connector import Error
from mysql.connector import pooling
from mysql.connector import connect

dbconfig = {
    "host": "localhost", 
    "port": "3306", 
    "user": "root", 
    "password": "root1234", 
    "database": "L1_W6"
}

def create_connection_pool():
    cnxpool = mysql.connector.pooling.MySQLConnectionPool(
        pool_name = "mysqlpool2",
        pool_size = 20,
        pool_reset_session= True,
        autocommit = True, 
        **dbconfig
    )

    return cnxpool