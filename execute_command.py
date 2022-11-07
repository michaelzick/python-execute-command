#!/usr/bin/env python3

import subprocess

command = 'msg * You have been pwnd'

subprocess.Popen(command, shell=True)
