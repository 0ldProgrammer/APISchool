#coding:utf-8

import subprocess
from random import randint

class IncorrectToStartMachine(Exception):
        def __init__(self, error=None):
                self.error = error

def IdentityOfMachine(identity_machine):
        '''
                This function tests the
                value of the function __IdentityOfMachine()__.
        '''
        if(len(identity_machine) != 4):
                raise IncorrectToStartMachine("Incorrect to start machine, sorry!")

        if(identity_machine[3] == "1"):
                bool = True
        elif(identity_machine[3] == "2"):
                bool = False

        return bool

def StartMachinePCT(number_of_machine, user_id):
        '''
                This function will start the
                containers and virtual machines. __StartMachinePCT()__.
        '''
        random_numbers  = randint(200,900)

        network_setting = f"name=eth0,bridge=vmbr{user_id},ip=dhcp,type=veth"
        send_command    = [["pct", "clone", str(number_of_machine), str(random_numbers)], ["pct", "set", str(random_numbers), "-net0", network_setting]]

        if(type(number_of_machine) != str):
                raise IncorrectToStartMachine("Incorrect to start machine, sorry!")
        for j in send_command:
                subprocess.run(j)
        return

def StartMachineQM(number_of_machine):
        if(type(number_of_machine) != str):
                raise IncorrectToStartMachine("Incorrect to start machine, sorry!")
        return

