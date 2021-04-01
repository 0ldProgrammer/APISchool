#coding:utf-8

import subprocess
import re
from random import randint

class IncorrectToStartMachine(Exception):
        def __init__(self, error=None):
                self.error = error

def IdentityOfMachine(passing_parameter):
        '''
                This function tests the
                value of the function __IdentityOfMachine()__.
        '''
        if(len(passing_parameter) != 4):
                raise IncorrectToStartMachine("Incorrect to start machine, sorry!")

        if(passing_parameter[3] == "1"):
                bool_data = True
        elif(passing_parameter[3] == "2"):
                bool_data = False

        return bool_data

def StartMachinePCT(number_of_machine, user_id, random_numbers):
        '''
                This function will start the
                containers and virtual machines. __StartMachinePCT()__.
        '''

        network_setting = f"name=eth0,bridge=vmbr2,ip=172.30.10.{user_id}/24,gw=172.30.10.254,type=veth"
        number_of_machine = str(int(200 + number_of_machine))

        send_command    = [["pct", "unlock", str(number_of_machine)], ["pct", "clone", str(200 + number_of_machine), str(random_numbers)], ["pct", "set", str(random_numbers), "-net0", network_setting], ["pct", "start", str(random_numbers)]]

        for j in send_command:
                subprocess.run(j)
        return


def StartMachineQM(number_of_machine):
        if(type(number_of_machine) != str):
                raise IncorrectToStartMachine("Incorrect to start machine, sorry!")
