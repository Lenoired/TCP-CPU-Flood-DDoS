# TCP-CPU Flood/DDoS Script

Python script for DDoSing/flooding open TCP ports. Vulnerable systems may be CPU exhausted.

</br>

## Installation
NOTE: This command might not work for every system.
```bash

git clone https://github.com/Lenoired/TCP-CPU-Flood-DDoS.git flood-tcp-cpu && cd flood-tcp-cpu && python3 flood.py

```

## Usage

```bash
python3 flood.py <IP> <port> <threads> <duration, in seconds> <optional: max packets per second, default: 1000>
```

## Examples

- _Flood port 80 with target IP 1.1.1.1 with 2 threads for 30 seconds_

```bash

python3 flood.py 1.1.1.1 80 2 30

```
