# coding=utf8

import MySQLdb
from skylark import Database, Model, Field

class Message(Model):
    title = Field()
    content = Field()
    create_at = Field()


Database.set_dbapi(MySQLdb)
Database.config(**app.config['DB_CONN_CFG'])
