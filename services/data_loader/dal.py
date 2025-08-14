import os
import mysql.connector

class DataLoader:
    def __init__(self):
        self.details = {
            "host": os.getenv("DB_HOST", "mysql-service"),
            "port": int(os.getenv("DB_PORT", "3306")),
            "database": os.getenv("DB_NAME", "sampledb"),
            "user": os.getenv("DB_USER", "appduser"),
            "password": os.getenv("DB_PASSWORD", "appdpass"),
        }

    def select_all(self):
        conn = mysql.connector.connect(**self.details)
        try:
            cur = conn.cursor()
            cur.execute("SELECT * FROM data")
            return cur.fetchall()
        finally:
            conn.close()