# sudo .venv/bin/python ping.py "larycxpajorj h bnpdarmjm nw anmnb"

import sys
from scapy.all import IP, ICMP, Raw, sr1, wrpcap
import time

if len(sys.argv) > 1:
    arg1 = sys.argv[1]
    print(f"Argumento 1: {arg1}")

palabra_cifrada = arg1
packet_dst = "192.168.1.1"
paquetes_enviados = []

for i, letter in enumerate(palabra_cifrada):
    codigo_ascii = ord(letter)

    # Payload estándar de ping Linux: 0x10 a 0x37 (40 bytes)
    payload = list(range(0x10, 0x38))  # 40 bytes: 0x10..0x37

    # Letra en el primer byte del payload (posición 0x10)
    payload[0] = codigo_ascii

    payload_bytes = bytes(payload)

    packet = IP(dst=packet_dst) / ICMP(id=0x0001, seq=i) / Raw(load=payload_bytes)

    respuesta = sr1(packet, timeout=2)
    paquetes_enviados.append(packet)

wrpcap("cap_cifrado.pcap", paquetes_enviados)