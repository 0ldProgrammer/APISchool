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

def create_interface_vmbr(id_of_users, new_list=[]):
    '''
        This function __create_interface_vmbr()__.
    '''
    with open("/etc/network/interfaces", "r") as read_interfaces:
        read_interfaces = read_interfaces.readlines()

    vmbr_settings =  f"auto vmbr{id_of_users}\n"
    vmbr_settings += f"iface vmbr{id_of_users} inet manual\n"
    vmbr_settings += "\tbridge-ports none\n"
    vmbr_settings += "\tbridge-stp off\n"
    vmbr_settings += "\tbridge-fd 0\n"
    vmbr_settings += f"#OPT{id_of_users}\n"

    new_list.append(vmbr_settings)

    for j in new_list:
        read_interfaces.append(j)

    file_open_interfaces = open("/etc/network/interfaces", "w")

    for write_interfaces in read_interfaces:
        write_interfaces = write_interfaces.rstrip("\n\r")
        file_open_interfaces.write(write_interfaces + "\n")

    return id_of_users
