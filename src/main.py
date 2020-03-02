# Resolve the problem!!
import re



def run():
    with open ('encoded.txt', 'r', encoding='utf-8') as f:
        texto_cifrado = f.read()
    mensaje = ""
    mensaje = re.findall("[a-z]", texto_cifrado)
    mensaje_oculto = ''.join(mensaje)
    print(mensaje_oculto)


if __name__ == '__main__':
    run()
