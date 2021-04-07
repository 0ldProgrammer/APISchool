#coding:utf-8

import subprocess

def RestoreMachinePCT(id_user):
        id_user = 200 + int(id_user)
        pct_exec = [["pct", "stop", str(id_user)], ["pct", "rollback", str(id_user), "backup"], ["pct", "start", str(id_user)]]

        for j in pct_exec:
                subprocess.run(j)
