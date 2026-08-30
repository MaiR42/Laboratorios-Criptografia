import sys

if len(sys.argv) > 2: # Debug
    arg1 = sys.argv[1]
    arg2 = int(sys.argv[2])
    print(f"Argumento 1: {arg1}")
    print(f"Argumento 2: {arg2}")

alfabeto = ['a','b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u','v', 'w', 'x', 'y', 'z']

palabra = arg1
rot = arg2

#palabra = "criptografia y seguridad en redes"
#rot = 9

def CifradoCesar(message, key):
    output_text = ""
    for letter in message:
        if letter in alfabeto:
            posi = alfabeto.index(letter) + key
            posi = posi % len(alfabeto)
            output_text = output_text + alfabeto[posi]
        else:
            output_text += letter
    print("Texto Cifrado: ", output_text)
    return output_text

palabra_cifrada = CifradoCesar(palabra, rot)