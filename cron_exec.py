#coding:utf-8

import phpserialize
import mysql.connector
import sys
import re

if(len(sys.argv) < 2):
  sys.exit('miss argument roles!')

def check_checkpoint(name_of_argument):
        checkpoint_re = re.findall('checkpoint0[1-4]', name_of_argument)
        if(checkpoint_re != []):
                return True
        return False
def update_values():
        contact_mysql = mysql.connector.connect(user='x', password='x', 
                                                host='x', database='x')
        send_command = contact_mysql.cursor()
        query_request = ("SELECT wp_users.ID, wp_users.user_login, wp_usermeta.meta_value FROM wp_users INNER JOIN wp_usermeta ON wp_users.ID = wp_usermeta.user_id WHERE wp_usermeta.meta_key = 'wp_capabilities';")
        send_command.execute(query_request)

        list_append = {}
        for j in send_command.fetchall():
                id, user, roles = j
                if("administrator" not in roles):
                        dict = phpserialize.unserialize(bytes(roles, encoding='utf8'))
                        argument_called = "um_" + sys.argv[1]
                        dict.update({argument_called: True})
                        list_append[id] = phpserialize.serialize(dict)

        return list_append

                return True
        return False

def update_values():
        contact_mysql = mysql.connector.connect(user='x', password='x',
                host='x', database='x')
        send_command = contact_mysql.cursor()
        query_request = ("SELECT wp_users.ID, wp_users.user_login, wp_usermeta.meta_value FROM wp_users INNER JOIN wp_usermeta ON wp_users.ID = wp_usermeta.user_id WHERE wp_usermeta.meta_key = 'wp_capabilities';")        send_command.execute(query_request)

        list_append = {}

        for j in send_command.fetchall():
                id, user, roles = j
                if("administrator" not in roles):
                        dict = phpserialize.unserialize(bytes(roles, encoding='utf8'))
                        argument_called = "um_" + sys.argv[1]
                        dict.update({argument_called: True})
                        list_append[id] = phpserialize.serialize(dict)

        return list_append

class ExceptionErrorMySQL(Exception):
        def __init__(self, error=None):
                self.error = error

def send_mysql():
        var = update_values()
        for j in var:
                contact_mysql = mysql.connector.connect(user='x', password='x', host='x', database='x')
                send_command = contact_mysql.cursor()

                query_request = ("UPDATE wp_usermeta SET meta_value = '%s' WHERE user_id = '%s' && meta_key = 'wp_capabilities';" %(var[j].decode('utf8'), str(j)))
                send_command.execute(query_request)
                contact_mysql.commit()

if __name__ == "__main__":
        send_mysql()
