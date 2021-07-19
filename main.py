#!/usr/env/python
#coding:utf-8

__author__  = ["Selim", "Thomas"]

import os
import re
import sys
import subprocess
import time
import random

from random import randint
from flask import Flask, request, redirect

from modules import start
from modules import restore
from modules import stop
from modules import machine
from modules import log



app = Flask(__name__)
WEB_DOMAIN = "www.whs.fr"

@app.route("/", methods=["GET"])
def get_url():
        """
                In this function, we start and stop and even
                reset the virtual machines and container. __get_url__().
        """
        id_vm = request.args.get('vm')

        with open('status/' + str(request.args.get('user')) + ".qf", "w") as f_write:
                f_write.write('pid=' + str(random.randint(5555,9999)) + "\n")

        if(int(machine.IdentityOfMachine(id_vm)) == 1):
                log.log_time(str(request.args.get('user')), str(request.args.get('vm')[:3]))
                start.StartMachinePCT(request.args.get('vm')[:3], request.args.get('user'))

        elif(int(machine.IdentityOfMachine(id_vm)) == 2):
                log.log_stop(str(request.args.get('user')), '/root/APISchool/log/')
                stop.StopMachinePCT(request.args.get('user'))

        elif(int(machine.IdentityOfMachine(id_vm)) == 3):
                if(machine.check_machine_list(request.args.get('user')) == 1):
                        log.log_restore(str(request.args.get('user')), '/root/APISchool/log/')
                        stop.StopMachinePCT(request.args.get('user'))
                        start.StartMachinePCT(request.args.get('vm')[:3], request.args.get('user'))
        return ""

@app.route("/sonde", methods=["GET"])
def prtg_check():
        return ""

if __name__ == "__main__":
    app.run(host="172.30.0.1", port=5000, debug=True, threaded=False, processes=8)
