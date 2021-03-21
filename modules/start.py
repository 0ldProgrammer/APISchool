#coding:utf-8

import subprocess

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

        if(passing_parameter[4] == "1"):
                bool_data = True
        elif(passing_parameter[4] == "2"):
                bool_data = False

        return bool_data

def StartMachinePCT(number_of_machine):
  
        send_command = ["pct", "start", number_of_machine]
  
        if(type(name_of_machine) != str):
                raise IncorrectToStartMachine("Incorrect to start machine, sorry!")

        if(IdentityOfMachine(number_of_machine) == True):
                subprocess.run(send_command)

def StartMachineQM(number_of_machine):
        if(type(name_of_machine) != str):
                raise IncorrectToStartMachine("Incorrect to start machine, sorry!")

if __name__ == "__main__":
        StartMachinePCT("4")
