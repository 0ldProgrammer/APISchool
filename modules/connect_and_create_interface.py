#coding:utf-8

import os, mysql.connector
import re

list_users_id = []

def get_id_from_db():
    '''
      We connect to the SQL database
      to make changes. __get_id_from_db()__.
    '''
    connect_db = mysql.connector.connect(user='d', password='d', host='d', database="d")
    request_db = connect_db.cursor()
    request_db.execute("SELECT `id` FROM pentest_network")
    result_req = request_db.fetchall()
    
    for x in result_req:
        number = str(x)
        id = number.strip("(,)")
        list_users_id.append(id)

def create_interface_vmbr(id):
    with open("/etc/network/interfaces", "r") as conf:
        data = conf.readlines()

    one = f"auto vmbr{id}\n"
    one += f"iface vmbr{id} inet manual\n"
    one += "\tbridge-ports none\n"
    one += "\tbridge-stp off\n"
    one += "\tbridge-fd 0\n"
    one += f"#OPT{id}\n"

    v = []

    temp_list = v.append(one)
    for j in v:
        data.append(j)

    f = open("int", "w")

    for i in data:
        i = i.rstrip("\n\r")
        f.write(i + "\n")
