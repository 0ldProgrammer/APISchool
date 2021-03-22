#coding:utf-8

import subprocess
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


def AttributeFirewallQT(id_of_user):
        network_setting       = f"-net{id_of_user}"
        bridge_setting        = f"bridge=vmbr{id_of_user},model=e1000"
        send_command_firewall = ["qm", "set", "100", network_setting, bridge_setting]

        subprocess.run(send_command_firewall)

        return


def StartMachineQM(number_of_machine):
        if(type(number_of_machine) != str):
                raise IncorrectToStartMachine("Incorrect to start machine, sorry!")
               
