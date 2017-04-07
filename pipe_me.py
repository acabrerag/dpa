#!/usr/bin/env python
# coding: utf-8

import re
import sys

# n = int(sys.argv[1]) # Leemos un entero como argumento (opcional)

while True:
  linea = sys.stdin.readline()

  if not linea:
    break
  # Hacemos algo con la línea
  print("Linea desde python: {}".format(linea))
