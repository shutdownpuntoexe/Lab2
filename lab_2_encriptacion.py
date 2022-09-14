import hashlib

def leer():
    archivo=open('mensajedeentrada.txt.','r')
    a=archivo.read()
    archivo.close()
    return a

def escribir(texto,hash_):
    final=texto+';'+hash_
    archivo=open('mensajeseguro.txt','w')
    archivo.write(final)
    archivo.close()
def hashing(texto):
    md5 = hashlib.md5(texto.encode()) 
    return md5.hexdigest()

def rot (message, key, mode):
    message    = message.upper()
    translated = ""
    LETTERS    = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for symbol in message:
        if symbol in LETTERS:
            num = LETTERS.find(symbol)
            if mode ==   "cifrar":
                num = num + key
            elif mode == "descifrar":
                num = num - key

            if num >= len(LETTERS):
                num -= len(LETTERS)
            elif num < 0:
                num += len(LETTERS)

            translated += LETTERS[num]
        else:
            translated += symbol
    return translated

def vigenere(clave,mensa,accion):
    LETRAS = ("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    traducido=[]
    indice_clave=0
    clave=clave.upper()

    for symbol in mensa:
        num=LETRAS.find(symbol.upper())
        if num!=-1:
            if accion=='encriptar':
                num+=LETRAS.find(clave[indice_clave])
            elif accion=='descifrar':
                num-=LETRAS.find(clave[indice_clave])
            num%=len(LETRAS)
            if symbol.isupper():
                traducido.append(LETRAS[num])
            elif symbol.islower():
                traducido.append(LETRAS[num].lower())
            indice_clave+=1
            if indice_clave==len(clave):
                indice_clave=0

        else:
            traducido.append(symbol)
    return ('').join(traducido)

texto=leer().upper()
hash_md5=hashing(texto)
texto=rot(texto,8,'cifrar')
texto=vigenere('superpassword',texto,'encriptar')
texto=rot(texto,12,'cifrar')
escribir(texto, hash_md5)