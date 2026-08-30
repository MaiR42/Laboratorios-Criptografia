import sys

if len(sys.argv) > 1: # Debug
    arg1 = sys.argv[1]
    print(f"Argumento 1: {arg1}")

palabra_cifrada = arg1 # larycxpajorj h bnpdarmjm nw anmnb

from scapy.all import IP, ICMP, sr1,wrpcap
import time

packet_dst = "192.168.1.1" # IP destino
paquetes_enviados = []

for i,letter in enumerate(palabra_cifrada):
    Codigo_ASCII = ord(letter)
    segundos = int(time.time())+i
    microsegundos = Codigo_ASCII
    timestamp = segundos + (microsegundos / 1_000_000)
    packet = IP(dst=packet_dst)/ICMP()
    packet.time = timestamp
    respuesta = sr1(packet, timeout=2)
    paquetes_enviados.append(packet)

wrpcap("cap_cifrado.pcap", paquetes_enviados)