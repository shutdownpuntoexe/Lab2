import hashlib

def leer():
    archivo=open('mensajeseguro.txt.','r')
    a=archivo.read()
    archivo.close()
    a=a.split(';')
    return a[0],a[1]

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


texto,hash_md5=leer()
texto=rot(texto,12,'descifrar')
texto=vigenere('superpassword',texto,'descifrar')
texto=rot(texto,8,'descifrar')
hash_de_verificacion=hashing(texto)
if hash_de_verificacion==hash_md5:
    print('El mensaje es seguro, no ha sido modificado')
else:
    print('el mensaje ha sido vulnerado')
