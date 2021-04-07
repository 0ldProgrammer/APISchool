#!/usr/env/python
#coding:utf-8

import os
from random import randint
from flask import Flask, request, redirect

from modules import start
from modules import restore
from modules import stop
from modules import machine

app = Flask(__name__)
WEB_DOMAIN = "www.whs.fr"

@app.route("/", methods=["GET"])
def get_url():
        '''
                In this function, we start and stop and even
                reset the virtual machines and container. __get_url__().
        '''
        
        if(int(machine.IdentityOfMachine(id_vm)) == 1):
                start.StartMachinePCT(request.args.get('vm')[:3], request.args.get('user'))

        elif(int(machine.IdentityOfMachine(id_vm)) == 2):
                stop.StopMachinePCT(request.args.get('user'))

        elif(int(machine.IdentityOfMachine(id_vm)) == 3):
                restore.RestoreMachinePCT(request.args.get('user'))

        return ""


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True, threaded=False, processes=8)
