#!/usr/env/python
#coding:utf-8

import os
from flask import Flask, request, redirect

from modules import randomID
from modules import start

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

        if(start.IdentityOfMachine(id_vm) == True):
            if(id_user not in list_users_id):
                # Fonction qui monte la carte réseau virtuel dans proxmox
                start.StartMachinePCT(request.args.get('vm')[:3], request.args.get('user'))
            else:
                start.StartMachinePCT(request.args.get('vm')[:3], request.args.get('user'))
        return ""


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
