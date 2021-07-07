#!/usr/bin/python
#coding:utf-8

import re
import os
import sys
import subprocess

def delete_files_qf(files):
        '''
                This will delete the temporary files.

                Function: __delete_files_qf()__.
        '''
        for j in os.listdir("/root/APISchool/status"):
                if(j.endswith(".qf") == True):
                        os.remove("/root/APISchool/status/" + files)

def container_check_uptime():
        for j in os.listdir("/root/APISchool/status/"):
                if(j.endswith(".qf") == True):
                        sys.path.append('/root/APISchool/modules/')
                        __import__('log').log_stop(str(j.split('.')[0]), "/root/APISchool/log/")
                        '''
                                This function detects the time of containers started,
                                and switched off and removes the container after 6 hours.

                                Function: __container_check_uptime()__.
                        '''
                        f_split = 200 + int(j.split(".")[0])
                        p_check_command = ["/usr/sbin/pct", "status", str(f_split), "--verbose"]
                        j_execu_command = subprocess.check_output(p_check_command).decode('utf-8')

                        m_match_value   = re.findall('uptime\: [0-9]{0,}', j_execu_command)
                        j_update_uptime = int("".join(m_match_value).split(' ')[1])

                        print(j_update_uptime)

                        if(int(j_update_uptime) >= 120):
                                pct_exec = [["/usr/sbin/pct", "stop", str(f_split)], ["/usr/sbin/pct", "destroy", str(f_split), "--purge", "1"]]

                                for p in pct_exec:
                                        subprocess.run(p)

                                delete_files_qf(j)

if __name__ == "__main__":
        container_check_uptime()
