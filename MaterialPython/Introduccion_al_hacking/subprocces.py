#!/usr/bin/env python
#_*_ coding: utf8 _*_

import os
import subprocess

a = open(os.devnull,'w') # Pozo sin fondo
p = subprocess.call(['ping','1.1.1.1'],stdout=a,stderr=subprocess.STDOUT)

if p == 0:
	print("El comando se ejecuto correctamente")
else:
	print("Fallo la ejecucion del comando")