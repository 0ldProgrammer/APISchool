#coding:utf-8

import subprocess
import re
from random import randint

class IncorrectToStartMachine(Exception):
        def __init__(self, error=None):
                self.error = error

def StartMachinePCT(number_of_machine, user_id):
        '''
                This function will start the
                containers and virtual machines. __StartMachinePCT()__.
        '''

        network_setting = f"name=eth0,bridge=vmbr2,ip=172.30.10.{user_id}/24,gw=172.30.10.254,type=veth"
        user_machine = str(int(200 + int(user_id)))

        send_command    = [["pct", "unlock", str(number_of_machine)], ["pct", "clone", str(number_of_machine), str(user_machine), "--pool", "Users_Pentest"], ["pct", "set", str(user_machine), "-net0", network_setting], ["pct", "start", str(user_machine)]]

        for j in send_command:
                subprocess.run(j)

        return

def StartMachineQM(number_of_machine):
        if(type(number_of_machine) != str):
                raise IncorrectToStartMachine("Incorrect to start machine, sorry!")
