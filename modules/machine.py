#coding:utf-8

import os
import re

def check_machine_list(id_user):
        """
                This function will allow you to see
                the availability of the machine.

                Function: __check_machine_list__()
        """
        for j in os.listdir('/etc/pve/nodes/'):
                j = j

        pct_list = []

        for h in os.listdir('/etc/pve/nodes/' + j + '/lxc'):
                sum = 200 + int(id_user)
                if(str(sum) in h.replace('.conf', '')):
                        pct_list.append(1)
                        break

                pct_list.append(0)
        return pct_list[-1]

def IdentityOfMachine(qct):
        """
                This function will allow you to identify if the
                user wants to start, stop or restore a machine.

                Function: __IdentityOfMachine__()
        """
        if(qct[3] == 1):
                qct = 1
        if(qct[3] == 2):
                qct = 2
        if(qct[3] == 3):
                qct = 3

        return int(qct[3])
