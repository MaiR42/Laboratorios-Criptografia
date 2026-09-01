# sudo .venv/bin/python ping.py "larycxpajorj h bnpdarmjm nw anmnb"
import sys, struct, time
from scapy.all import IP, ICMP, Raw, sr1, wrpcap

if len(sys.argv) > 1:
    arg1 = sys.argv[1]
    print(f"Argumento 1: {arg1}")

palabra_cifrada = arg1
packet_dst = "192.168.1.1"
paquetes_enviados = []

for i, letter in enumerate(palabra_cifrada):
    codigo_ascii = ord(letter)

    # 8 bytes de timestamp (timeval, little-endian)
    ts_sec = int(time.time()) + i
    ts_usec = 0
    timestamp_bytes = struct.pack('<II', ts_sec, ts_usec)

    # Patrón estándar 0x10..0x37 (40 bytes), letra escondida en primer byte
    patron = list(range(0x10, 0x38))
    patron[0] = codigo_ascii
    
    payload = timestamp_bytes + bytes(patron)  # total 48 bytes

    packet = IP(dst=packet_dst) / ICMP(id=0x0001, seq=i) / Raw(load=payload)
    respuesta = sr1(packet, timeout=2)
    paquetes_enviados.append(packet)

wrpcap("cap_cifrado.pcap", paquetes_enviados)