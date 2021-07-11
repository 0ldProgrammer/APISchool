#coding:utf-8

import re
import os
import sys
import subprocess

def StopMachinePCT(id_user):
        os.remove("/root/APISchool/status/" + id_user + ".qf")
        id_users  = 200 + int(id_user)
        pct_exec = [["pct", "stop", str(id_users)], ["pct", "destroy", str(id_users), "--purge", "1"]]

        for j in pct_exec:
               subprocess.run(j)
