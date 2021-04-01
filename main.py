#!/usr/env/python
#coding:utf-8

import os
from random import randint
from flask import Flask, request, redirect

from modules import start
from modules import connect_and_create_interface as interfaces

app = Flask(__name__)
WEB_DOMAIN = "www.whs.fr"

@app.route("/", methods=["GET"])
def get_url():
        '''
                In this function, we start and stop and even
                reset the virtual machines and container. __get_url__().
        '''
        id_vm   = request.args.get('vm')
        id_user = request.args.get('user')

        random_numbers = randint(200, 900)

        if(start.IdentityOfMachine(id_vm) == True):
                start.StartMachinePCT(request.args.get('vm')[:3], request.args.get('user'), str(random_numbers))

        return ""


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True, threaded=False, processes=8)
