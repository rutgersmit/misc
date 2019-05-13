#! /usr/bin/env python
import sys
import mysql.connector
import config as cfg

connection = mysql.connector.connect(host=cfg.mysql['host'],database=cfg.mysql['database'],user=cfg.mysql['user'],password=cfg.mysql['password'])
cursor = connection.cursor(prepared=True)

tsql =('CREATE TABLE IF NOT EXISTS temperatures ('
    'id INT AUTO_INCREMENT, '
    'datetime DATETIME, '
    'location VARCHAR(50) NOT NULL, '
    'temperature DECIMAL(4,2), '
    'humidity DECIMAL(4,2), '
    'PRIMARY KEY (id)'
');')
cursor.execute(tsql)
connection.commit()
connection.close()
