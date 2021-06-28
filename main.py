#!/usr/env/python
#coding:utf-8

import os
import re
import subprocess
import time
from random import randint
from flask import Flask, request, redirect

from modules import autoshut
from modules import start
from modules import restore
from modules import stop
from modules import machine

app = Flask(__name__)
WEB_DOMAIN = "www.whs.fr"

@app.route("/", methods=["GET"])
def get_url():
        """
                In this function, we start and stop and even
                reset the virtual machines and container. __get_url__().
        """
        id_vm = request.args.get('vm')

        with open('status/' + request.args.get('user') + ".qf", "w") as f_write:
                f_write.write(' ')

        if(int(machine.IdentityOfMachine(id_vm)) == 1):
                start.StartMachinePCT(request.args.get('vm')[:3], request.args.get('user'))

        elif(int(machine.IdentityOfMachine(id_vm)) == 2):
                stop.StopMachinePCT(request.args.get('user'))

        return ""

@app.route("/sonde", methods=["GET"])
def prtg_check():
        return ""

if __name__ == "__main__":
    app.run(host="172.30.0.1", port=5000, debug=True, threaded=False, processes=8)
