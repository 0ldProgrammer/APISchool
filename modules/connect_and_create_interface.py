#coding:utf-8

import os, mysql.connector
import re

list_users_id = []

class Hello():
    def __init__(self):
        pass

def get_id_from_db():
    '''
      We connect to the SQL database
      to make changes. __get_id_from_db()__.
    '''
    connect_db = mysql.connector.connect(user='x', password='x', host='x', database="x")
    request_db = connect_db.cursor()
    request_db.execute("SELECT `id` FROM pentest_network")
    result_req = request_db.fetchall()

    for x in result_req:
        number = str(x)
        id = number.strip("(,)")
        list_users_id.append(id)

    return list_users_id
