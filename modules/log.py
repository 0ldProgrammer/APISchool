#coding:utf-8

import os
import re
import json
import subprocess
from datetime import datetime

def recover_name_of_machine(argument_of_machine):
        """
        """
        for j in os.listdir("/etc/pve/nodes"):
                node_name = j

        with open("/etc/pve/nodes/" + node_name + "/lxc/" + str(argument_of_machine) + ".conf", "r") as read_conf_file:
                read_conf_file = read_conf_file.read()
                read_conf_file = re.findall('hostname\: .+', read_conf_file)[0].split(":")[1].replace(' ', '')
        return read_conf_file

def log_time(id_of_user, id_of_machine):
        path_of_variable = "log/" + str(id_of_user)
        try:
                os.mkdir(path_of_variable)
        except FileExistsError as exception_error_file_directory:
                pass

        update_time = path_of_variable + "/" + str(id_of_user) + "_" + str(datetime.now().strftime('%m-%d-%Y-%H-%M-%S')) + ".json"
        date_time   = datetime.now().strftime('%H:%M:%S')
        with open(update_time, "w") as create_json_file:
                data = {'information': [{'id_user': str(id_of_user), 'id_machine': id_of_machine,
                        'name_machine': str(recover_name_of_machine(id_of_machine)),
                        "time_start":str(date_time), 'status':'on'}]}
                create_json_file.write(json.dumps(data, indent=4))
