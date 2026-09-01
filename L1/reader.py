
from scapy.all import rdpcap, Raw, ICMP

alfabeto = ['a','b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u','v', 'w', 'x', 'y', 'z']
palabras_comunes = {" de ", " en ", " el ", " la ", " con ", " para "}

def extraer_mensaje_cifrado(pcap_file):
    paquetes = rdpcap(pcap_file)
    mensaje = ""
    for pkt in paquetes:
        if pkt.haslayer(ICMP) and pkt.haslayer(Raw):
            payload = bytes(pkt[Raw].load)
            if len(payload) >= 1:
                codigo_ascii = payload[0]
                if 97 <= codigo_ascii <= 122:
                    mensaje += chr(codigo_ascii)
                elif codigo_ascii == 32:
                    mensaje += " "
    return mensaje



def decode_rot(texto, key):
    output = ""
    for letra in texto:
        if letra in alfabeto:
            posi = alfabeto.index(letra) - key
            posi = posi % len(alfabeto)
            output += alfabeto[posi]
        else:
            output += letra
    return output

def prGreen(s): print("\033[92m {}\033[00m".format(s)) # Imprimir en verde

mensaje_cifrado = extraer_mensaje_cifrado("cap_cifrado.pcap")

rot = 0
for rot in range(26):
    candidato = decode_rot(mensaje_cifrado, rot)
    match = any(f" {palabra.strip()} " in f" {candidato} " for palabra in palabras_comunes)

    if match:
        prGreen(f"[key={rot:2}] {candidato}")
    else:
        print(f"[key={rot:2}] {candidato}")
