#coding:utf-8

import subprocess

def RestoreMachinePCT(id_user):
        id_user = 200 + int(id_user)
        pct_exec = [["/usr/sbin/pct", "stop", str(id_user)], ["/usr/sbin/pct", "rollback", str(id_user), "backup"], ["/usr/sbin/pct", "start", str(id_user)]]

        for j in pct_exec:
                subprocess.run(j)
