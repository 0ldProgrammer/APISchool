#!/usr/env/python
#coding:utf-8
import os
from flask import Flask, request, redirect
from modules import randomID

app = Flask(__name__)
WEB_DOMAIN = "www.whs.fr"

@app.route("/", methods=["GET"])
def get_url():
    id_vm = request.args.get('vm', '')
    id_user = request.args.get('user', '')
    syntax = f"pct start {id_vm[:3]}"
    os.system(syntax)
    return ""

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
