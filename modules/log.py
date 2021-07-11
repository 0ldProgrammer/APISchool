#coding:utf-8

import os
import re
import json
import subprocess
import mysql.connector
from datetime import datetime

def recover_username(id_of_user):
        """
                This function will make it possible to retrieve the name of the
                user using the identifier and this contacts the SQL database.

                Function: __recover_username__().
        """
        contact_mysql = mysql.connector.connect(user='x', password='x',
                              host='x',
                              database='x')

        send_command = contact_mysql.cursor()
        query_request = ("SELECT user_login FROM wp_users WHERE ID=" + id_of_user)
        send_command.execute(query_request)

        list_append = []

        for user_pass in send_command:
                for j in user_pass:
                        list_append.append(j)
        return list_append[0]

def recover_name_of_machine(argument_of_machine):
        """
                This function will allow us to read the configuration
                file, and to retrieve the name of the machine.

                Function: __recover_name_of_machine()__
        """
        for j in os.listdir("/etc/pve/nodes"):
                node_name = j

        with open("/etc/pve/nodes/" + node_name + "/lxc/" + str(argument_of_machine) + ".conf", "r") as read_conf_file:
                read_conf_file = read_conf_file.read()
                read_conf_file = re.findall('hostname\: .+', read_conf_file)[0].split(":")[1].replace(' ', '')
        return read_conf_file

def log_time(id_of_user, id_of_machine):
        """
                This function will create the folder, and configure the necessary
                things related to the user and the machine by creating a log file.

                Function: __log_time()__
        """
        path_of_variable = "/root/APISchool/log/" + str(id_of_user)
        try:
                os.mkdir(path_of_variable)
        except FileExistsError as exception_error_file_directory:
                pass

        update_time = path_of_variable + "/" + str(id_of_user) + "_" + str(datetime.now().strftime('%m-%d-%Y-%H-%M-%S')) + ".json"
        date_time   = datetime.now().strftime('%H:%M:%S')
        with open(update_time, "w") as create_json_file:
                data = {'information': [{'id_user': str(id_of_user), 'username': recover_username(id_of_user), 'id_machine': id_of_machine,
                        'name_machine': str(recover_name_of_machine(id_of_machine)),
                        "time_start":str(date_time), 'status':'on', "time_end":"None"}]}
                create_json_file.write(json.dumps(data, indent=4, sort_keys=True))

def log_stop(id_of_user, path_file):
        """
                This function will update the file when the client stops
                the machine, and update the time and status of the machine.

                Function: __log_stop()__
        """
        json_path_file = []
        for j in os.listdir(path_file + str(id_of_user)):
                if(j.endswith("json") == True):
                        json_path_file.append(j)

        date_time   = datetime.now().strftime('%H:%M:%S')

        with open(path_file + str(id_of_user) + "/" + json_path_file[-1], "r") as expend_file:
                json_object = json.loads(expend_file.read())
                json_object["information"][0]["status"]   = "off"
                json_object["information"][0]["time_end"] = str(date_time)

        with open(path_file + str(id_of_user) + "/" + json_path_file[-1], "w") as overwrite_file:
                overwrite_file.write(json.dumps(json_object, indent=4, sort_keys=True))
                
           
